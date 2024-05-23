<template>
  <nav class="navbar navbar-expand-lg border-bottom border-body text-white" data-bs-theme="dark">
    <div class="container-fluid">
      <img src="@/icons/logo.png" alt="logo" width="30" height="30" class="d-inline-block align-text-top" :to="{ name: 'home' }">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarScroll">
        <ul class="navbar-nav me-auto my-2 mx-3 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
          <li class="nav-item mx-1">
            <RouterLink 
              class="nav-link text-white"
              :to="{ name: 'home' }"
            >홈</RouterLink>
          </li>
          <li class="nav-item mx-1">
            <RouterLink 
              class="nav-link text-white"
              :to="{ name: 'movie' }"
            >영화</RouterLink>
          </li>
          <li class="nav-item mx-1">
            <div class="favorites text-center d-flex justify-content-center align-items-center">
              <RouterLink 
                class="nav-link text-black"
                :to="{ name: 'favorite' }"
              >찜</RouterLink>   
              <span v-if="accountStore.userInfo.like_movies" class="nav-link text-black">{{ accountStore.userInfo.like_movies.length }}</span>
              <span v-else>0</span>
            </div>
          </li>
        </ul>
        <form class="d-flex" role="search" @submit.prevent="search">
          <input id="input" class="form-control me-2" type="search" placeholder="Search" aria-label="Search" onfocus="this.placeholder=''" onblur="this.placeholder='Search'" :value="inputText" @input="onInput">
          <button class="btn" type="submit">
            <img src="@/icons/search.png" alt="search" width="30" height="30">
          </button>
        </form>
        <RouterLink
          class="btn"
          :to="{ name: 'profile', params:{userPk:accountStore.userId}}"
        >
          <div class="dropdown">
            <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img src="@/icons/person.png" alt="유저 프로필" width="30" height="30">
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" @click="goProfile">프로필</a></li>
              <li><a class="dropdown-item" @click="logOut">로그아웃</a></li>
            </ul>
          </div>
        </RouterLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useRouter } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { useAccountStore } from '@/stores/account';
import axios from 'axios';
import { ref, onMounted } from 'vue';

const router = useRouter()
const movieStore = useMovieStore()
const accountStore = useAccountStore()

const goProfile = function () {
  router.push({ name: 'profile', params:{userPk:accountStore.userId}})
}

const logOut = function () {
  
  axios({
    method: 'post',
    url: `${movieStore.API_URL}/accounts/logout/`,
    headers: {
      Authorization: `Token ${accountStore.token}`
    }
  })
  .then(res => {
    router.push({ name: 'login' })
    accountStore.token = null
  })
  .catch(err => console.log(err))
}

const inputText = ref('')
const onInput = function (event) {
  inputText.value = event.currentTarget.value
}

const search = function () {
  const keyword = inputText.value
  if (keyword) {
    router.push({ name: 'search', params: { keyword } })
    inputText.value = null
  }
}

onMounted(() => {
  accountStore.getUserInfo()
})
</script>

<style scoped>
.favorites {
  background-color: white;
  border-radius: 50px;
  width: 60px;
}

.navbar {
  background-color: #1f1f1f;
}
</style>