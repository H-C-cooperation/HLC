<template>
  <Carousel :itemsToShow="3.95" :wrapAround="true" :transition="500">
    <Slide v-for="movie in movies" :key="movie.id">
      <img class="carousel__item" :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" :alt="movie.title" />
    </Slide>

    <template #addons>
      <Navigation />
    </template>
  </Carousel>
</template>

<script>
import { defineComponent } from 'vue';
import { Carousel, Navigation, Slide } from 'vue3-carousel'
import { useMovieStore } from '@/stores/movie';

import 'vue3-carousel/dist/carousel.css'

export default defineComponent({
  name: 'Autoplay',
  components: {
    Carousel,
    Slide,
    Navigation,
  },

  setup() {
    const store = useMovieStore()
    const movies = store.movies

    return {
      movies
    }
  }
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

.carousel__prev, .carousel__next {
  color: #fff;
}
</style>
