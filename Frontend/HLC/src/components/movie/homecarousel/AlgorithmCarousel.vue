<template>
    <div>
      <div v-if="movies.length > 3">
        <Carousel 
            :itemsToShow="items" 
            :wrapAround="false" 
            :transition="500"
            snapAlign="center"
            navigationNextLabel=""
            navigationPrevLabel=""
        >
            <Slide v-for="movie in movies" :key="movie.id">
            <div 
                class="card bg-black"
                :class="['item', { 'active-item': activeMovie === movie.id }]" 
                @mouseover="showInfo(movie.id)"
                @mouseleave="hideInfo(movie.id)"
            >
                <img class="carousel__item" :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" :alt="movie.title"/>
                <div class="text-field">
                <h5 class="text-white my-5">{{ movie.title }}</h5>
                </div>
                <div class="card-body">
                <div v-if="activeMovie === movie.id" class="info-popup">
                    <iframe 
                    :src="`${movie.youtube_url}?autoplay=1&mute=1&controls=0&modestbranding=1&rel=0`" 
                    width="100%"
                    height="50%"
                    frameborder="0"
                    class="iframe-content"
                    ></iframe>
                    <h5 class="card-title">영화 설명</h5>
                    <p>(chatGPT로 생성됨)</p>
                    <CarouselHover class="mb-3 p-1 border border-danger-subtle" :movie="movie"/>
                    <a href="#" class="btn bg-danger bg-opacity-75 text-white">자세히 보기</a>
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
      <div v-else class="text-center my-5">
        <h5>충분한 영화가 없습니다.</h5>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { Carousel, Navigation, Slide } from 'vue3-carousel'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'
import 'vue3-carousel/dist/carousel.css'
import CarouselHover from '@/components/movie/CarouselHover.vue'

const props = defineProps({
  genre: String
})

const store = useMovieStore()
const movies = ref([])
const items = ref(0)
const activeMovie = ref(null)

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

const getMovies = async function() {
  try {
    const movieData = await store.getMovieByAlgorithm()
    movies.value = movieData
  } catch (error) {
    console.error('Error fetching movies:', error)
  }
}

onMounted(async () => {
  updateItems()
  await getMovies()
  window.addEventListener('resize', updateItems)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateItems)
})
</script>

<style scoped>

</style>