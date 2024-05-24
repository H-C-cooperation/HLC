<template>
  <div class="m-5">
    <div class="text-center p-5 m-5">
      <img src="@/icons/logo.png" alt="" width="500px">
      <h1 class="my-4">HLC</h1>
      <h3>안녕하세요</h3>
      <h3>사용자 취향 장르의 영화들을 TMDB로 부터 받아와 추천해 주는 서비스 HLC 입니다.</h3>
      <h3>조금 전 수집한 당신의 취향 장르 정보를 가지고, 영화들을 준비해 보았습니다.</h3>
      <h3 class="mt-4">🎉🎉 부디 즐겨주세요 🎉🎉</h3>
    </div>
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