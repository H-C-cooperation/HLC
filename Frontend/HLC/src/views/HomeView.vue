<template>
  <h1>홈</h1>
  <div class="movie-carousel">
    <swiper :slides-per-view="5" :space-between="20" :breakpoints="breakpoints">
      <swiper-slide v-for="movie in movies" :key="movie.id">
        <div class="movie-card">
          <img :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" :alt="movie.title" />
          <p>{{ movie.title }}</p>
        </div>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import { useMovieStore } from '@/stores/movie'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { onMounted } from 'vue';
import 'swiper/swiper-bundle.css'

export default {
  components: {
    Swiper,
    SwiperSlide
  },
  setup() {
    const store = useMovieStore()
    const movies = store.movies

    const breakpoints = {
      320: { slidesPerView: 1, spaceBetween: 10 },
      480: { slidesPerView: 2, spaceBetween: 20 },
      640: { slidesPerView: 3, spaceBetween: 20 },
      768: { slidesPerView: 4, spaceBetween: 20 },
      1024: { slidesPerView: 5, spaceBetween: 20 }
    }

    onMounted(() => {
      store.getMovies()
    })

    return {
      movies,
      breakpoints
    }
  }
}
</script>

<style scoped>
.movie-carousel {
  width: 100%;
  margin: auto;
  overflow: hidden;
}

.movie-card {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.movie-card img {
  width: 200px;
  height: 300px;
  object-fit: cover;
  border-radius: 10px;
}

.movie-card p {
  text-align: center;
  margin-top: 5px;
  font-size: 1rem;
  color: #fff;
}
</style>
