<template>
  <div class="outer bg-black" v-if="targetInfo">
    <div class="outline">
      <header>
        <!-- {{ store.userInfo }} 
        <hr>
        {{ targetInfo }} -->
        <!-- 1. v-if 내프로필이라면 ( ) -->
        <h1 v-if="isMyProfile">프로필 수정</h1>
        <!-- 2. v-if 다른사람 프로필이라면 ( ) -->
        <h1 v-else><!--다른사람이름--> {{ targetInfo.username }} 님의 프로필</h1>

        <hr />
      </header>
      <nav>
        <!-- 1. v-if 내 프로필이라면 -->
        <div class="d-flex align-items-center" v-if="isMyProfile">
          <!-- 내프로필 이미지로 img src 고쳐야함 ( ) -->
          <img :src="store.userInfo.image" alt="my img" class="m-3" />
          <div class="inputbox d-flex flex-column">
              <input
                type="text"
                placeholder="유저 이름"
                v-model="store.userInfo.username"
                class="inputbox bg-secondary-subtle m-2"
              />
              <input
                type="text"
                placeholder="유저 이메일"
                v-model="store.userInfo.email"
                class="inputbox bg-secondary-subtle m-2"
              />
          </div>
        </div>

        <!-- 2. v-if 다른사람 프로필이라면 -->
        <div class="d-flex align-items-center" v-else>
          <!-- 프로필 이미지로 img src 고쳐야함 ( ) -->
          <img :src="targetInfo.image" alt="my img" class="m-3" />
          <div class="d-flex flex-column align-content-center">
            <!-- 이름, 이메일 넣기 ( ) -->
              <p style="margin:auto; padding: 5px; ">NAME : {{ targetInfo.username }}</p>
              <p style="margin:auto; padding: 5px;">EMAIL : {{ targetInfo.email }}</p>
          </div>
        </div>
        <button class="f-btn ms-3">Follow</button>  <button class="f-btn"> Following</button>



      </nav>
      <br />
      <main class="d-flex">
        <article class="articlestyle">
          <h3>Followers</h3>
          <hr />
          <div class="d-flex" style="height: 110px;">
            <!-- 위의 div 안에다가 바로 아래의 p(img, p 담고있음)가 반복되도록 만들기. followers의 img, username 반복되도록 ( ) -->
            <!-- img src, username 고쳐야함 -->
            <p class="d-flex flex-column me-3 align-items-center">
              <img src="" alt="follower img" />
              <p class="fs-5">username</p>
            </p>
          </div>

          <br>
          <br />

          <h3>Followings</h3>
          <hr />
          <div class="d-flex" style="height: 130px;">
            <!-- 위의 div 안에다가 바로 아래의 p(img, p 담고있음)가 반복되도록 만들기. followings의 img, username 반복되도록 ( ) -->
            <!-- img src, username 고쳐야함 -->
            <p class="d-flex flex-column me-3 align-items-center">
              <img src="" alt="following img" />
              <p class="fs-5">username</p>
            </p>
          </div>

          <br />
          <h3>Your Favorite Genres</h3>
          <hr />
          <div class="d-flex">
          <!-- 위의 div태그 안에 아래의 p가 반복되도록. genre 여러개 나오도록 ( ) -->
            <p class="fs-5 me-3">
              Genre1
            </p>
          </div>
          <!-- v-if 본인 프로필이라면 edit 버튼 사용 ( ) -->
          <button>EDIT</button>

        </article>
      </main>
      <nav>
        <hr />
        <!-- save, cancel 버튼 연결 -->
        <button class="me-3">SAVE</button>
        <button class="cancelbtn">CANCEL</button>
      </nav>
    </div>
  </div>
</template>

<script setup>
import { ref ,onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import axios from 'axios';

onMounted(() => {
  store.getUserInfo,
  getTargetUserInfo()
})

const store = useMovieStore()
const route = useRoute()
const targetInfo = ref([])
const isMyProfile = ref(false)

// 타켓 유저 정보 가져오기 : route.params.userPk
const getTargetUserInfo = () => {
  axios({
    method:'get',
    url: `${store.API_URL}/accounts/${route.params.userPk}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      console.log(res.data)
      targetInfo.value = res.data
      isMyProfile.value = store.userId === res.data.id
    })
    .catch(err => console.log(err))
} 



</script>

<style scoped>

.outer {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 70px;
  color: white;
}

.outline {
  width: 80%;
}

.articlestyle {
  margin-left: 120px;
  width: 100%;
}

.inputbox {
  width: 80%;
}

.cancelbtn {
  border: solid white 1px;
  background-color: black;
  color: white;
}
.f-btn {
  background-color: red;
  color: white;
  height: 30px;
  width: 100px;
}

img {
  width: 80px;
  height: 80px;
}

button {
  width: 100px;
}
</style>