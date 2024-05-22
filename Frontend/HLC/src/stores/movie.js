import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const token = ref(null)
  const userId = ref(0)
  const userInfo = ref({})


  const genres = ref([
      "액션",
      "모험",
      "애니메이션", 
      "코미디",
      "범죄",
      "다큐멘터리",
      "드라마",
      "가족",
      "판타지",
      "역사",
      "공포",
      "음악",
      "미스터리",
      "로맨스",
      "SF",
      "TV 영화",
      "스릴러",
      "전쟁",
      "서부"
  ])

  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      params: {
        mode: 'popularity',
      }
    })
      .then(res => {
        movies.value = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }


  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/registration/`,
      data: {
        username, password1, password2
      }
    })
      .then(res => {
        const password = password1
        logIn({ username, password })
      })
      .catch(err => console.log(err))
  }


  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        // console.log(res.data)
        token.value = res.data.key
        router.push({ name: 'home' })
      })
      .catch(err => console.log(err))
  }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {        
      return true
    }
  })

  const getFavMoview = function() {
    axios ({
      method: 'get',
      url: `${API_URL}/accounts/user/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
      .then(res => {
        userId.value = res.data.pk
        
        axios ({
          method: 'get',
          url: `${API_URL}/accounts/${userId.value}/`,
          headers: {
            Authorization: `Token ${token.value}`
          },
        })
          .then(res => {
            userInfo.value = res.data
          })
          .catch(err => console.log(err))
      })
      .catch(err => console.log(err))
  }

  // MoviesList (영화 리스트 조회)
  // const takeMoviesList = function 



  // MovieDetail (영화 단일 조회)
  const takeMovieDetail = async function (movie_pk) {
    try {
      const response = await axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movie_pk}`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      });
      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  const takeMovieDetailReview = async function (movie_pk) {
    try {
      const response = await axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movie_pk}/reviews`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      });
      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };
  

  return { movies, API_URL, getMovies, signUp, logIn, token, isLogin, genres, takeMovieDetail, takeMovieDetailReview, getFavMoview, userId, userInfo }
}, { persist: true })
