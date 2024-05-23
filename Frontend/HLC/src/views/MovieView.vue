<template>
  <div class="m-5">
    <div class="m-3 text-center">
      <h1 class="m-5">⭐Top10 영화들⭐</h1>
      <MainCarousel />
    </div>
    <div class="sub-carousel">
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
      <h3>스낵처럼 짧은 영화를 원하시나요? 🥨</h3>
      <hr style="border: solid 2px #fff;">
      <ShortCarousel />
      <h3>적당한 시간이 있으시다면... 🍳</h3>
      <hr style="border: solid 2px #fff;">
      <MiddleCarousel />
      <h3>영화를 음미할 줄 아는 분이라면..! 🥂</h3>
      <hr style="border: solid 2px #fff;">
      <LongCarousel />
    </div>
  </div>
</template>

<script setup>
import MainCarousel from '@/components/movie/moviecarousel/MainCarousel.vue'
import SubCarousel1 from '@/components/movie/moviecarousel/SubCarousel1.vue'
import SubCarousel2 from '@/components/movie/moviecarousel/SubCarousel2.vue'
import SubCarousel3 from '@/components/movie/moviecarousel/SubCarousel3.vue'
import SubCarousel4 from '@/components/movie/moviecarousel/SubCarousel4.vue'
import SubCarousel5 from '@/components/movie/moviecarousel/SubCarousel5.vue'
import SubCarousel6 from '@/components/movie/moviecarousel/SubCarousel6.vue'
import ShortCarousel from '@/components/movie/moviecarousel/ShortCarousel.vue'
import MiddleCarousel from '@/components/movie/moviecarousel/MiddleCarousel.vue'
import LongCarousel from '@/components/movie/moviecarousel/LongCarousel.vue'
</script>

<style scoped>
.main-carousel {
  width: 1000px;
  height: 500px;
  text-align: center
}

.sub-carousel {
  overflow: visible;
}
</style>
