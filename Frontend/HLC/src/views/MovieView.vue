<template>
  <div class="m-5">
    <div class="m-3 text-center">
      <h1 class="m-3">⭐Top10 영화들⭐</h1>
      <MainCarousel />
    </div>
    <div>
      <h3>화끈한 액션영화 🔥</h3>
      <hr style="border: solid 2px #fff;">
      <SubCarousel1 class="mb-5"/>
      <h3>모험을 시작할까요? 🚀</h3>
      <hr style="border: solid 2px #fff;">
      <SubCarousel2 class="mb-5"/>
      <h3>애니메이션 세계로! 🏰</h3>
      <hr style="border: solid 2px #fff;">
      <SubCarousel3 class="mb-5"/>
      <h3>배터지게 웃고싶은 날 😂</h3>
      <hr style="border: solid 2px #fff;">
      <SubCarousel4 class="mb-5"/>
      <h3>짜릿한 범죄영화 🕵</h3>
      <hr style="border: solid 2px #fff;">
      <SubCarousel5 class="mb-5"/>
      <h3>가족과 함께 👨‍👩‍👧‍👦</h3>
      <hr style="border: solid 2px #fff;">
      <SubCarousel6 class="mb-5"/>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import MainCarousel from '@/components/movie/MainCarousel.vue'
import SubCarousel1 from '@/components/movie/SubCarousel1.vue'
import SubCarousel2 from '@/components/movie/SubCarousel2.vue'
import SubCarousel3 from '@/components/movie/SubCarousel3.vue'
import SubCarousel4 from '@/components/movie/SubCarousel4.vue'
import SubCarousel5 from '@/components/movie/SubCarousel5.vue'
import SubCarousel6 from '@/components/movie/SubCarousel6.vue'

const store = useMovieStore()

const movies = store.movies
const genres = store.genres
</script>

<style scoped>
.main-carousel {
  width: 1000px;
  height: 500px;
  text-align: center
}
</style>
