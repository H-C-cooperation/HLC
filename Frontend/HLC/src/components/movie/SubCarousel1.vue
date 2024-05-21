<template>
  <Carousel 
    :itemsToShow="items" 
    :wrapAround="true" 
    :transition="500"
    navigationNextLabel=""
    navigationPrevLabel=""
  >
    <Slide v-for="movie in movies" :key="movie.id">
      <div 
        class="item" 
        @mouseover="showInfo(movie.id)"
        @mouseleave="hideInfo(movie.id)"
      >
        <img class="carousel__item" :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" :alt="movie.title" />
        <div v-if="activeMovie === movie.id" class="info-popup">
          <h3>{{ movie.title }}</h3>
          <p>{{ movie.overview }}</p>
        </div>
      </div>
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
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'
import 'vue3-carousel/dist/carousel.css'

const store = useMovieStore()
const movies = ref([])
const items = ref(0)
const activeMovie = ref(null)

const getMovies = function() {
  axios({
  method: 'get',
  url: `${store.API_URL}/api/v1/movies/`,
  headers: {
    Authorization: `Token ${store.token}`
  },
  params: {
    mode: 'genre',
    inputGenre: '액션'
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

const showInfo = (movieId) => {
  activeMovie.value = movieId
}

const hideInfo = () => {
  activeMovie.value = null
}


const initializePopovers = () => {
  nextTick(() => {
    movieRefs.value.forEach(ref => {
      new bootstrap.Popover(ref, {
        trigger: 'hover'
      })
    })
  })
}

onMounted(() => {
  getMovies()
  updateItems()
  window.addEventListener('resize', updateItems)
  initializePopovers()
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

.item {
  position: relative;
  cursor: pointer;
}

.item:hover {
  transform: scale(1.05);
}

.info-popup {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.item:hover .info-popup {
  opacity: 1;
}
</style>