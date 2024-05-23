<template>
  <div class="outer bg-black" v-if="targetInfo">
    <div class="outline">
      <header>
        <!-- 1. v-if 내프로필이라면 ( ) -->
        <h1 v-if="isMyProfile">{{staticUserName}} 님의 프로필 수정</h1>
        <!-- 2. v-if 다른사람 프로필이라면 ( ) -->
        <h1 v-else><!--다른사람이름--> {{ targetInfo.username }} 님의 프로필</h1>

        <hr />
      </header>
      <nav>
        <!-- 1. v-if 내 프로필이라면 -->
        <div class="d-flex align-items-center" v-if="isMyProfile">
          <!-- 내프로필 이미지로 img src 고쳐야함 ( ) -->
          <img :src="accountStore.userInfo.image" alt="my img" class="m-3" />
          <div class="inputbox d-flex flex-column">
            <input type="file" @change="onFileChange" class="inputbox bg-secondary-subtle m-2"/>
              <input
                type="text"
                placeholder="유저 이름"
                v-model="accountStore.userInfo.username"
                class="inputbox bg-secondary-subtle m-2"
              />
              <input
                type="text"
                placeholder="유저 이메일"
                v-model="accountStore.userInfo.email"
                class="inputbox bg-secondary-subtle m-2"
              />
          </div>
        </div>

        <!-- 2. v-if 다른사람 프로필이라면 -->
        <div class="d-flex align-items-center" v-else>
          <!-- 프로필 이미지로 img src 고쳐야함 ( ) -->
          <img :src="targetInfo.image" alt="my img" class="m-3" />
          <div class="d-flex flex-column align-content-start">
            <!-- 이름, 이메일 넣기 ( ) -->
              <h3 style=" padding: 5px; ">NAME : {{ targetInfo.username }}</h3>
              <h3 style=" padding: 5px;" >EMAIL : {{ targetInfo.email }}</h3>
          </div>
        </div>
        <template v-if="!isMyProfile">
          <button class="f-btn" v-if="isFollowing" @click="toggleFollow"> Following</button>
          <button class="f-btn ms-2" v-else @click="toggleFollow">Follow</button>  
        </template>

      </nav>
      <br />
      <main class="d-flex">
        <article class="articlestyle">
          <h3>Followers</h3>
          <hr />
          <div class="d-flex" style="height: 110px;">
            <!-- 위의 div 안에다가 바로 아래의 p(img, p 담고있음)가 반복되도록 만들기. followers의 img, username 반복되도록 ( ) -->
            <!-- img src, username 고쳐야함 -->

            <p class="d-flex flex-column me-3 align-items-center" v-for="person in targetInfo.followers">
              <img :src="person.image" alt="follower img" />
              <p class="fs-5">{{ person.username }}</p>
            </p>
          </div>

          <br>
          <br />

          <h3>Followings</h3>
          <hr />
          <div class="d-flex" style="height: 130px;">
            <!-- 위의 div 안에다가 바로 아래의 p(img, p 담고있음)가 반복되도록 만들기. followings의 img, username 반복되도록 ( ) -->
            <!-- img src, username 고쳐야함 -->
            <p class="d-flex flex-column me-3 align-items-center" v-for="person in targetInfo.followings">
              <img :src="person.image" alt="following img" />
              <p class="fs-5">{{ person.username }}</p>
            </p>
          </div>

          <br />
          <h3>{{targetInfo.username}} 님이 좋아하는 장르</h3>
          <hr />
          <div class="d-flex">
          <!-- 위의 div태그 안에 아래의 p가 반복되도록. genre 여러개 나오도록 ( ) -->
            <p class="fs-5 me-3" v-for="genre in targetInfo.like_genres">
              {{ genre.name }}
            </p>
          </div>
          <!-- v-if 본인 프로필이라면 edit 버튼 사용 ( ) -->
          <button v-if="isMyProfile">EDIT</button><br><br><br>

          <h3>{{ targetInfo.username }} 님이 찜한 영화</h3>
          <hr />
          <div class="d-flex">
          <!-- 위의 div태그 안에 아래의 p가 반복되도록. genre 여러개 나오도록 ( ) -->
            <p class="fs-5 me-3" v-for="movie in targetInfo.like_movies">
              <img :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" alt="movie img" style="width: 200px; height: 300px;"/>
              <p class="fs-5 text-center">{{ movie.title }}</p>
            </p>
          </div>
        </article>
      </main>
      <nav v-if="isMyProfile">
        <hr />
        <!-- save, cancel 버튼 연결 -->
        <button class="me-3" @click="saveProfile">SAVE</button>
        <button class="cancelbtn" @click="cancelEdit">CANCEL</button>
      </nav>
    </div>
  </div>
</template>

<script setup>
import { ref ,onMounted, watch, computed } from 'vue';
import { useRoute, onBeforeRouteLeave } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { useAccountStore } from '@/stores/account';
import axios from 'axios';

const movieStore = useMovieStore()
const accountStore = useAccountStore()
const route = useRoute()
const targetInfo = ref([])
const isMyProfile = ref(false)
const staticUserName = accountStore.userInfo.username

// 이미지 업로드
const image = ref(null);
const imageUrl = computed(() => accountStore.userInfo.image);


const isFollowing = computed(() => {
  const followers = targetInfo.value.followers || [];
  return followers.some(follower => follower.id === accountStore.userId);
});

const onFileChange = (e) => {
  const file = e.target.files[0];
  image.value = file;
  accountStore.userInfo.image = URL.createObjectURL(file);
};

const uploadImage = async () => {
  if (!image.value) {
    alert('이미지를 먼저 선택해 주세요.');
    return;
  }

  const formData = new FormData();
  formData.append('image', image.value);

  try {
    const response = await axios.post(`${accountStore.API_URL}/accounts/profile/${accountStore.userInfo.id}/upload_image/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Token ${accountStore.token}`,
      },
    });
    accountStore.userInfo.image = response.data.image;
  } catch (error) {
    console.error('Error uploading image:', error);
  }
};

const saveProfile = async () => {
  if (image.value) {
    await uploadImage();
  }
  try {
    const { username, email } = accountStore.userInfo;
    const response = await axios.put(
      `${accountStore.API_URL}/accounts/${accountStore.userInfo.id}/`,
      { username, email }, // 필요한 정보만 전송
      {
        headers: {
          Authorization: `Token ${accountStore.token}`,
        },
      }
    );
    console.log('Profile updated:', response.data);
    window.location.reload()
  } catch (error) {
    console.error('Error updating profile:', error);
  }
};

const cancelEdit = () => {
  // 편집 취소 로직 (필요한 경우 추가)
  window.location.reload()

};



const toggleFollow = async () => {
  try {
    const response = await axios ({
      method: 'post',
      url: `${accountStore.API_URL}/accounts/${targetInfo.value.id}/follow/`,
      headers: {
        Authorization: `Token ${accountStore.token}`,
      },
    })
    // 서버 응답에 따라 isFollowing 업데이트
    console.log(response.data)
    // console.log(response.data) => 비동기 구현 실패...
    targetInfo.value.followers = response.data.followers
    // window.location.reload()
  } catch (error) {
    console.error('Failed to toggle following', error)
    alert('팔로잉을 변경하는 중 오류가 발생')
  }
}

// 타켓 유저 정보 가져오기 : route.params.userPk
const getTargetUserInfo = async () => {
  try {
      const response = await axios({
        method: 'get',
        url: `${accountStore.API_URL}/accounts/${route.params.userPk}/`,
        headers: {
          Authorization: `Token ${accountStore.token}`
        },
      });
      targetInfo.value = response.data
      isMyProfile.value = accountStore.userId === response.data.id
    } catch (error) {
      console.error(error);
      throw error;
  }
}

onMounted(() => {
  accountStore.getUserInfo,
  getTargetUserInfo()
})

onBeforeRouteLeave((to, from) => {
  targetInfo.value = null
})

watch(
  () => route.params.userPk,
  (newUserPk, oldUserPk) => {
    if (newUserPk !== oldUserPk) {
      getTargetUserInfo();
    }
  }
);

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