<!-- <template>
  <div class="mx-auto video">
    <Carousel id="gallery" :items-to-show="1" :wrap-around="false" v-model="currentSlide">
      <Slide v-for="(movie) in movies" :key="movie.id">
        <div>
          <iframe 
            :src="movie.youtube_url + '?autoplay=1&mute=1&controls=0'" 
            width="1080px"
            height="500px"
            frameborder="0"
            class="mb-3 center-block"
          >
          </iframe>
          <h2>TOP {{ movies.indexOf(movie) + 1 }}</h2>
          <p>{{ movie.title }}</p>
        </div>
  
      </Slide>
  
      <template #addons>
        <navigation>
          <template #next>
            <img src="@/components/icons/arrow_forward.png" alt="arrow" width="30px" height="30px">
          </template>
          <template #prev>
            <img src="@/components/icons/arrow_back.png" alt="arrow" width="30px" height="30px">
          </template>
        </navigation>
      </template>
    </Carousel>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { ref } from 'vue'
import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'

const currentSlide = ref(0)

const slideTo = (val) => {
  currentSlide.value = val
}

const store = useMovieStore()
const movies = store.movies.slice(0, 10)

</script>

<style scoped>
.video {
  width: 80%;
}
</style> -->

<template>
  <div class="mx-auto video">
    <Carousel id="gallery" :items-to-show="1" :wrap-around="false" v-model="currentSlide">
      <Slide v-for="(movie) in movies" :key="movie.id">
        <div style="width: 80%;">
          <div class="iframe-container">
            <iframe 
              :src="movie.youtube_url + '?autoplay=1&mute=1&controls=0'" 
              width="100%"
              height="100%"
              frameborder="0"
              class="iframe-content"
            ></iframe>
          </div>
          <div class="text-container">
            <h2>TOP {{ movies.indexOf(movie) + 1 }}</h2>
            <p>{{ movie.title }}</p>
          </div>
        </div>
      </Slide>
      <template #addons>
        <navigation>
          <template #next>
            <img src="@/components/icons/arrow_forward.png" alt="arrow" width="30px" height="30px">
          </template>
          <template #prev>
            <img src="@/components/icons/arrow_back.png" alt="arrow" width="30px" height="30px">
          </template>
        </navigation>
      </template>
    </Carousel>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { ref } from 'vue'
import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'

const currentSlide = ref(0)

const slideTo = (val) => {
  currentSlide.value = val
}

const store = useMovieStore()
const movies = store.movies.slice(0, 10)

</script>

<style scoped>
.video {
  width: 80%;
  margin: 0 auto;
}

.iframe-container {
  position: relative;
  width: 100%;
  height: 0;
  padding-top: 56.25%; /* 16:9 비율의 비디오를 위한 값 */
}

.iframe-content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.text-container {
  margin-top: 10px;
  text-align: center; 
}

h2 {
  margin: 5px 0;
}

p {
  margin: 0;
}
</style>