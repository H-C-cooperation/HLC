<template>
  <nav class="navbar navbar-expand-lg border-bottom border-body text-white" data-bs-theme="dark">
    <div class="container-fluid">
      <img src="./icons/logo.png" alt="logo" width="30" height="30" class="d-inline-block align-text-top" :to="{ name: 'home' }">
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
            <div class="favorites text-center">
              <RouterLink 
              class="nav-link text-black"
              :to="{ name: 'favorite' }"
              >찜</RouterLink>    
            </div>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn" type="submit">
            <img src="./icons/search.png" alt="search" width="30" height="30">
          </button>
        </form>
        <RouterLink
          class="btn"
          :to="{ name: 'profile' }"
        >
          <img src="./icons/person.png" alt="유저 프로필" width="30" height="30">
        </RouterLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
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