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
  const isSignUp = ref(false)

  // Movie Detail 에서 사용
  const detailMovie = ref({})
  const detailReviews = ref([])
  
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

  const getMoviesByGenre = async function (genre) {
    try {
      const response = await axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        params: {
          mode: 'genre',
          inputGenre: `${genre}`
        },
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
        isSignUp.value = true
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
        token.value = res.data.key
        if (isSignUp.value === true) {
          isSignUp.value = false
          router.push({ name: 'select' })
        } else {
          router.push({ name: 'home' })
        }
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

  const getUserInfo = function() {
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
      detailMovie.value =  response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  // 영화에 연결된 리뷰 리스트 조회
  const takeMovieDetailReview = async function (movie_pk) {
    try {
      const response = await axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movie_pk}/reviews`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      });
      detailReviews.value = response.data
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  // review 생성 , 업데이트  동시에 할 수 있게해주는 함수
  const createOrUpdateReview = async function(reviewId, rate, content) {
    let response;
    try {
      console.log('reviewId---', reviewId)
      if (reviewId !== -1) {
        // Update existing review
          response = await axios({
          method: 'patch',
          url: `${API_URL}/api/v1/movies/${detailMovie.value.id}/reviews/${reviewId}/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
          data: {
            rate,
            content
          }
        });
        console.log('DB에서 리뷰 수정 작업이 완료되었습니다.');
  
        // Update the local review list
        detailReviews.value = detailReviews.value.map((review) => {
          if (review.id === reviewId) {
            review.rate = rate;
            review.content = content;
          }
          return review;
        });
      } else {
        // Create new review
        response = await axios({
          method: 'post',
          url: `${API_URL}/api/v1/movies/${detailMovie.value.id}/reviews/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
          data: {
            rate,
            content
          }
        });
        // Add the new review to the local review list
        detailReviews.value.push(response.data);
        console.log('리뷰가 성공적으로 작성되었습니다.');
      }
  
    } catch (error) {
      console.error('There was an error!', error);
      alert('리뷰를 제출하는 도중 오류가 발생했습니다. 다시 시도해주세요.');
    }
  };

  const deleteReview = function (reviewId) {
    axios({
      method:'delete',
      url: `${API_URL}/api/v1/movies/${detailMovie.value.id}/reviews/${reviewId}/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
      .then(res => console.log('DB에서 리뷰 삭제 작업이 완료되었습니다.'))
      .catch(err => console.log(err))
    
      const index = detailReviews.value.findIndex((review) => review.id === reviewId)
      detailReviews.value.splice(index, 1)
  }

  

  return { movies, API_URL, getMovies, getMoviesByGenre, signUp, logIn, token, isLogin, genres, 
    getUserInfo, userId, userInfo,
    detailMovie, detailReviews, takeMovieDetail, takeMovieDetailReview, createOrUpdateReview, deleteReview }
}, { persist: true })
