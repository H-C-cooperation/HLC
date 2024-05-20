<template>
  <main class="bg-black text-white">
    <div v-if="store.isLogin">
      <NavBar />
      <RouterView />
      <Footer />
    </div>
    <div v-else>
      <RouterView />
    </div>
  </main>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
import LoginView from './views/LoginView.vue';
import SignUpView from './views/SignUpView.vue';
import ProfileView from './views/ProfileView.vue';
import { RouterView } from 'vue-router';
import { useMovieStore } from './stores/movie';

const store = useMovieStore()
const currentUrl = window.location.pathname
</script>

<style scoped>
</style>
