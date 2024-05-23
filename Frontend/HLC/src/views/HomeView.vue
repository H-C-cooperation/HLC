<template>
  <div class="m-5">
    <div v-if="genres.length > 0" class="main">
      <GenreCarousel 
        v-for="genre in genres"
        :key="genre"
        :genre="genre"
      />
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import { useAccountStore } from '@/stores/account';
import { ref, onMounted } from 'vue';
import GenreCarousel from '@/components/movie/homecarousel/GenreCarousel.vue'
import axios from 'axios';

const movieStore = useMovieStore()
const accountStore = useAccountStore()

const genres = accountStore.favGenres
</script>

<style scoped>
</style>