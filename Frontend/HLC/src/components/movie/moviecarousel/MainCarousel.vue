<template>
  <div class="mx-auto video">
    <Carousel id="gallery" :items-to-show="1" :wrap-around="false" v-model="currentSlide">
      <Slide v-for="movie in movies" :key="movie.id">
        <div style="width: 80%;" @mouseover="hovering = movie.id" @mouseleave="hovering = null">
          <div v-if="hovering !== movie.id" class="image-overlay">
            <h5>👇 마우스를 올려보세요</h5>
            <img :src="`https://image.tmdb.org/t/p/original/${movie.backdrop_path}`" alt="" width="100%" class="opacity-75">
            <div class="overlay-text do-hyeon-regular">
              <h1>TOP {{ movies.indexOf(movie) + 1 }}</h1>
              <h1>{{ movie.title }}</h1>
            </div>
          </div>
          <div v-else>
            <div class="iframe-container">
              <iframe 
                :src="movie.youtube_url + '?autoplay=1&mute=1&controls=0&loop=1'" 
                width="100%"
                height="100%"
                frameborder="0"
                class="iframe-content"
              ></iframe>
            </div>
            <div class="text-container">
              <h2>TOP {{ movies.indexOf(movie) + 1 }}</h2>
              <p>{{ movie.title }}</p>
              <button class="btn btn-danger mt-3">
                자세히 보기
              </button>
          </div>
          </div>
        </div>
      </Slide>
      <template #addons>
        <navigation>
          <template #next>
            <img src="@/icons/arrow_forward.png" alt="arrow" width="30px" height="30px">
          </template>
          <template #prev>
            <img src="@/icons/arrow_back.png" alt="arrow" width="30px" height="30px">
          </template>
        </navigation>
      </template>
    </Carousel>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { ref, onMounted } from 'vue'
import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'

const currentSlide = ref(0)
const hovering = ref(null)

const store = useMovieStore()
const movies = store.movies.slice(0, 10)

onMounted(() => {
  store.getMovies()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Freeman&family=Gasoek+One&display=swap');

.do-hyeon-regular {
  font-family: "Do Hyeon", sans-serif;
  font-weight: 500;
  font-style: normal;
}


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

.image-overlay {
  position: relative;
  width: 100%;
}

.overlay-text {
  position: absolute;
  top: 90%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: white;
  z-index: 1;
}

.image-overlay::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 40%; /* 그라데이션의 높이 조절 */
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.8)); /* 그라데이션 설정 */
}

h2 {
  margin: 5px 0;
}

p {
  margin: 0;
}
</style>
