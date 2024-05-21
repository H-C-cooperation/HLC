<template>
  <main class="bg-black text-white">
    <div v-if="store.navFootView">
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
import { RouterView } from 'vue-router';
import { useMovieStore } from './stores/movie';

const store = useMovieStore()

</script>

<style scoped>
</style>
