import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useMovieStore } from './movie'
import axios from 'axios'


export const useAccountStore = defineStore('account', () => {
  const movieStore = useMovieStore()

  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const token = ref(null)
  const userId = ref(0)
  const userInfo = ref({})
  const isSignUp = ref(false)
  const favGenres = ref([])

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
          router.push({ name: 'home', params: { genres: movieStore.favGenres } })
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

  const getGenres = async function () {
    try {
      const res = await axios({
        method: 'get',
        url: `${API_URL}/accounts/${userId.value}/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      favGenres.value = res.data.like_genres.map(obj => obj.name)
    } catch (err) {
      console.log(err)
    }
  }
  
  return { API_URL, signUp, logIn, token, isLogin, getUserInfo, userId, userInfo, favGenres, getGenres }
}, { persist: true })
