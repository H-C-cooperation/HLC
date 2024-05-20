<template>
  <div class="d-flex justify-content-center align-items-center back">
    <div class="bg-body-secondary bg-opacity-75 text-white p-5 text-center border border-dark border-2">
      <h1>HLC</h1>
      <br>
      <form @submit.prevent="signUp">
        <h2>회원가입</h2>
        <div class="m-3">
          <p>
            <input class="mx-2" id="ID" type="text" placeholder="ID" v-model.trim="username">
          </p>
          <p>
            <input class="mx-2" id="PW" type="text" placeholder="PW"v-model.trim="password1">
          </p>
          <p>
            <input class="mx-2" id="PW2" type="text" placeholder="PW Confirm"v-model.trim="password2">
          </p>
        </div>
        <div class="text-center">
          <input class="btn btn-dark" type="submit" value="회원가입">
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const store = useMovieStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
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