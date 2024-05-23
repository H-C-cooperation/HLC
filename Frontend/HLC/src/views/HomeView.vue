<template>
  <div v-if="genres.length > 0" class="main m-5">
    <HomeCarousel 
      v-for="genre in genres"
      :key="genre"
      :genre="genre"
    />
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import { useAccountStore } from '@/stores/account';
import { ref, onMounted } from 'vue';
import HomeCarousel from '@/components/movie/homecarousel/HomeCarousel.vue'
import axios from 'axios';

const movieStore = useMovieStore()
const accountStore = useAccountStore()

const genres = accountStore.favGenres
</script>

<style scoped>
</style>