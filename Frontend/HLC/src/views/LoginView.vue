<template>
  <div class="d-flex justify-content-center align-items-center back">
    <div class="bg-body-secondary bg-opacity-75 text-white p-5 text-center border border-dark border-2">
      <div class="blank"></div>
      <a href="#" id="title">HLC</a>
      <br>
      <form @submit.prevent="logIn">
        <p>아이디가 있으신가요?</p>
        <div class="m-3">
          <p>
            <input class="mx-2" id="ID" type="text" placeholder="ID" v-model.trim="username">
          </p>
          <p>
            <input class="mx-2" id="PW" type="password" placeholder="PW" v-model.trim="password">
          </p>
        </div>
        <div class="text-center">
          <input class="me-3 btn btn-dark" type="submit" value="로그인">
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

@keyframes tipsy {
  0% {
    transform: translateX(-50%) translateY(-50%) rotate(0deg);
  }
  100% {
    transform: translateX(-50%) translateY(-50%) rotate(360deg);
  }
}

body {
  font-family: helvetica, arial, sans-serif;
  background-color: #2e2e31;
}

#title {
  color: #000000;
  text-shadow: 0 20px 25px #2e2e31, 0 40px 60px #2e2e31;
  font-size: 50px;
  font-weight: bold;
  text-decoration: none;
  letter-spacing: -3px;
  margin: 0;
  position: absolute;
  top: 38%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
}

#title:before,
#title:after {
  content: '';
  padding: .9em .4em;
  position: absolute;
  left: 50%;
  width: 100%;
  top: 50%;
  display: block;
  border: 15px solid red;
  transform: translateX(-50%) translateY(-50%) rotate(0deg);
  animation: 10s infinite alternate ease-in-out tipsy;
}

#title:before {
  border-color: #e50914 #e50914 rgba(0, 0, 0, 0) rgba(0, 0, 0, 0);
  z-index: -1;
}

#title:after {
  border-color: rgba(0, 0, 0, 0) rgba(0, 0, 0, 0) #e50914 #e50914;
  box-shadow: 25px 25px 25px rgba(46, 46, 49, .8);
}

.blank {
  height: 150px;
}
</style>