<template>
  <div class="d-flex justify-content-center align-items-center back">
    <div class="bg-body-secondary bg-opacity-75 text-white p-5 text-center border border-dark border-2">
      <h1>HLC</h1>
      <br>
      <form @submit.prevent="logIn">
        <p>아이디가 있으신가요?</p>
        <div class="m-3">
          <p>
            <input class="mx-2" id="ID" type="text" placeholder="ID" v-model.trim="username">
          </p>
          <p>
            <input class="mx-2" id="PW" type="text" placeholder="PW" v-model.trim="password">
          </p>
        </div>
        <div class="text-center">
          <input class="me-5 btn btn-dark" type="submit" value="로그인">
          <button class="btn" @click="goSignUp">가입하기</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie';

const router = useRouter()
const store = useMovieStore()

const goSignUp = function () {
  router.push({ name: 'signup' })
}

const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
.back {
  background-image: url('../assets/background.png');
  background-size: cover;
  height: 100vh;
}

h1{
  text-transform:uppercase;
  font-size:60px;
  font-family:'Verdana';
  padding:10px;
  text-decoration: overline underline dashed;
  color: rgb(223, 41, 41);
  text-underline-offset: 15px;
}
</style>