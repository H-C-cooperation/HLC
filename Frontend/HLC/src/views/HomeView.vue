<template>
  <h1>홈</h1>
  <HomeCarouel 
    v-for="genre in genres"
    :key="genre.id"
    :genre="genre"
  />
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { ref, onMounted } from 'vue';
import HomeCarouel from '@/components/movie/homecarousel/HomeCarousel.vue'
import axios from 'axios';

const store = useMovieStore()
const genres = ref([])

const getGenres = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/${store.userId}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      for (const obj of res.data.like_genres) {
        genres.value.push(obj.name)
      }
      console.log(genres)
    })
    .catch(err => console.log(err))
}

onMounted(() => {
  store.getUserInfo()
  getGenres()
})
</script>

<style scoped>
</style>
