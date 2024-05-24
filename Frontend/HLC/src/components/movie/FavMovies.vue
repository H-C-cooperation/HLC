<template>
  <div class="row row-cols-1 row-cols-md-3 row-cols-lg-5 g-4">
    <div v-for="movie in store.userInfo.like_movies" :key="movie.id">
      <div class="col">
        <div 
          style="width: 10rem;"
          class="card bg-black"
        >
          <button class="btn" @click="movieStore.goToMovieDetail(movie.id)">
            <img :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" :alt="movie.title" width="190px" height="270px"/>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAccountStore } from '@/stores/account';
import { useMovieStore } from '@/stores/movie';

const store = useAccountStore()
const movieStore = useMovieStore()

onMounted(() => {
  store.getUserInfo()
})

</script>

<style scoped>
.card:hover {
  transform: scale(1.2);
  transition: transform 0.3s ease;
}
</style>