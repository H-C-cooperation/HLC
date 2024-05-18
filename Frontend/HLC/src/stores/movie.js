import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`,
      headers: {
        Authorization: `Token ${token.value}`
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
    const { userId, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/registration/`,
      data: {
        userId, password1, password2
      }
    })
      .then(res => {
        const password = password1
        logIn({ userId, password })
      })
      .catch(err => console.log(err))
  }

  const token = ref(nul)

  const logIn = function (payload) {
    const { userId, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        userId, password
      }
    })
      .then(res => {
        token.value = res.data.key
        router.push({ name: 'movie' })
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

  return { movies, API_URL, getMovies, signUp, logIn, token, isLogin }
}, { persist: true })
