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

const genres = ref([])

const getGenres = async function () {
  genres.value.splice(0, genres.value.length)
  try {
    const res = await axios({
      method: 'get',
      url: `${movieStore.API_URL}/accounts/${accountStore.userId}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
    genres.value = res.data.like_genres.map(obj => obj.name)
  } catch (err) {
    console.log(err)
  }
}

onMounted(async () => {
  await accountStore.getUserInfo()
  await getGenres()
})
</script>

<style scoped>
</style>
