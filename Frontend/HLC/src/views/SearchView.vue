<template>
  <h1 class="m-5 do-hyeon-regular">{{ keyword }} 에 대한 검색 결과</h1>
  <div v-if="movies.length > 0">
    <div class="container">
      <div class="row row-cols-2 row-cols-md-4 row-cols-lg-5 g-4">
        <div v-for="movie in movies" :key="movie.id" class="col">
          <div class="card bg-black text-white text-center m-3">
            <div v-if="movie.poster_path">
              <img :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" height="300px">
            </div>
            <div v-else>
              <img src="@/icons/No-Image.png" alt="" class="object-fit-cover" width="200px" height="300px">
            </div>
            <h5 class="mt-3">{{ movie.title }}</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="no-results">
    <div class="text-center">
      <h2 data-shadow='webs!'>Oops!</h2>
      <h3 class="mt-5">검색결과가 없습니다..!</h3>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import axios from 'axios';
import { ref, onMounted, watch } from 'vue';

const route = useRoute()
const movies = ref([])
const keyword = ref('')
const apiKey = import.meta.env.VITE_TMDB_KEY

const fetchMovies = async (query) => {
  try {
    const res = await axios.get('https://api.themoviedb.org/3/search/movie', {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      params: {
        query: query,
        include_adult: 'false',
        language: 'ko-KR'
      }
    })
    movies.value = res.data.results
    console.log(res.data.results)
  } catch (error) {
    console.error(error)
  }
}

watch(() => route.params.keyword, (newKeyword) => {
  if (newKeyword) {
    keyword.value = newKeyword
    fetchMovies(newKeyword)
  }
})

onMounted(() => {
  const initialKeyword = route.params.keyword
  if (initialKeyword) {
    keyword.value = initialKeyword
    fetchMovies(initialKeyword)
  }
})
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Righteous);

*, *:before, *:after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  position: relative;
  }

html, body {
  height: 100%;
}
body {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: hsla(230,40%,50%,1);
}
  body:before {
    content: '';
    display: inline-block;
    vertical-align: middle;
    font-size: 0;
    height: 100%;
    }

h2 {
  display: inline-block;
  color: rgb(194, 194, 194);
  font-family: 'Righteous', serif;
  font-size: 12em; 
  text-shadow: .03em .03em 0 hsla(230,40%,50%,1);
  }
  h2:after {
    content: attr(data-shadow);
    position: absolute;
    top: .06em; left: .06em;
    z-index: -1;
    text-shadow: none;
    background-image:
      linear-gradient(
        45deg,
        transparent 45%,
        hsla(48,20%,90%,1) 45%,
        hsla(48,20%,90%,1) 55%,
        transparent 0
        );
    background-size: .05em .05em;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  
    animation: shad-anim 15s linear infinite;
    }

@keyframes shad-anim {
  0% {background-position: 0 0}
  0% {background-position: 100% -100%}
  }

.do-hyeon-regular {
  font-family: "Do Hyeon", sans-serif;
  font-weight: 400;
  font-style: normal;
}

.no-results {
  height: 50vh;
}

.container {
  width: 80%;
}
</style>