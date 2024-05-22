<template>
  <div class="main m-5">
    <HomeCarousel 
      v-for="genre in genres"
      :key="genre"
      :genre="genre"
    />
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import { ref, onMounted } from 'vue';
import HomeCarousel from '@/components/movie/homecarousel/HomeCarousel.vue'
import axios from 'axios';

const store = useMovieStore()
const genres = ref([])

const getGenres = async function () {
  try {
    const res = await axios({
      method: 'get',
      url: `${store.API_URL}/accounts/${store.userId}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    genres.value = res.data.like_genres.map(obj => obj.name)
    console.log(genres.value)
  } catch (err) {
    console.log(err)
  }
}

onMounted(async () => {
  await store.getUserInfo()
  await getGenres()
})
</script>

<style scoped>
</style>
