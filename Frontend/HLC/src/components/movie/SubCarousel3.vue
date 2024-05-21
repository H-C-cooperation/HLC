<template>
  <Carousel 
    :itemsToShow="items" 
    :wrapAround="true" 
    :transition="500"
    navigationNextLabel=""
    navigationPrevLabel=""
  >
    <Slide v-for="movie in movies" :key="movie.id">
      <img class="carousel__item" :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" :alt="movie.title" />
    </Slide>

    <template #addons>
      <navigation>
        <template #next>
          <img src="../icons/arrow_forward.png" alt="arrow" width="30px" height="30px">
        </template>
        <template #prev>
          <img src="../icons/arrow_back.png" alt="arrow" width="30px" height="30px">
        </template>
      </navigation>
    </template>
  </Carousel>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'
import 'vue3-carousel/dist/carousel.css'

const store = useMovieStore()
const movies = ref([])
const items = ref(0)

const getMovies = function() {
  axios({
  method: 'get',
  url: `${store.API_URL}/api/v1/movies/`,
  headers: {
    Authorization: `Token ${store.token}`
  },
  params: {
    mode: 'genre',
    inputGenre: '애니메이션'
  }
})
  .then(res => {
    movies.value = res.data
  })
  .catch(err => {
    console.log(err)
  })
}

const updateItems = () => {
  if (window.innerWidth >= 1400) {
    items.value = 8
  } else if (window.innerWidth >= 1200) {
    items.value = 7
  } else if (window.innerWidth >= 992) {
    items.value = 6
  } else if (window.innerWidth >= 768) {
    items.value = 5
  } else if (window.innerWidth >= 576) {
    items.value = 4
  } else {
    items.value = 3
  }
}

onMounted(() => {
  getMovies()
  updateItems()
  window.addEventListener('resize', updateItems)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateItems)
})
</script>

<style scoped>

.carousel__slide {
  padding: 5px;
}

.carousel__viewport {
  perspective: 2000px;
}

.carousel__track {
  transform-style: preserve-3d;
}

.carousel__slide--sliding {
  transition: 0.5s;
}

.carousel__slide {
  opacity: 0.9;
  transform: rotateY(-20deg) scale(0.9);
}

.carousel__slide--active ~ .carousel__slide {
  transform: rotateY(20deg) scale(0.9);
}

.carousel__slide--prev {
  opacity: 1;
  transform: rotateY(-10deg) scale(0.95);
}

.carousel__slide--next {
  opacity: 1;
  transform: rotateY(10deg) scale(0.95);
}

.carousel__slide--active {
  opacity: 1;
  transform: rotateY(0) scale(1.1);
}
</style>
