<template>
  <div class="outer bg-black">
    <div>
      <h1 style="text-align: center">선호하는 장르를 선택해주세요</h1>
      <br /><br />
      <p style="text-align: right; font-weight: bold">최대 5개 선택</p>
      <div id="genres" style="width: 45rem; text-align: center">
        <button class="genre-button" data-genre="액션">액션</button>
        <button class="genre-button" data-genre="모험">모험</button>
        <button class="genre-button" data-genre="애니메이션">애니메이션</button>
        <button class="genre-button" data-genre="코미디">코미디</button>
        <button class="genre-button" data-genre="범죄">범죄</button>
        <button class="genre-button" data-genre="다큐멘터리">다큐멘터리</button>
        <button class="genre-button" data-genre="드라마">드라마</button>
        <button class="genre-button" data-genre="가족">가족</button>
        <button class="genre-button" data-genre="판타지">판타지</button>
        <button class="genre-button" data-genre="역사">역사</button>
        <button class="genre-button" data-genre="공포">공포</button>
        <button class="genre-button" data-genre="음악">음악</button>
        <button class="genre-button" data-genre="미스터리">미스터리</button>
        <button class="genre-button" data-genre="로맨스">로맨스</button>
        <button class="genre-button" data-genre="SF">SF</button>
        <button class="genre-button" data-genre="TV영화">TV영화</button>
        <button class="genre-button" data-genre="스릴러">스릴러</button>
        <button class="genre-button" data-genre="전쟁">전쟁</button>
        <button class="genre-button" data-genre="서부">서부</button>
      </div>
      <br />
      <br />

      <div class="d-grid gap-2">
        <button @click="submitGenres" class="btn btn-primary" type="button">
          HLC에서 영화 추천받기
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { useAccountStore } from '@/stores/account';

let selectedGenres = ref(new Set());
const movieStore = useMovieStore()
const accountStore = useAccountStore()

const router = useRouter()

// 클릭 이벤트를 처리하는 함수
const handleClick = (event) => {
  const target = event.target;

  console.log(selectedGenres)
  
  // 클릭된 요소가 버튼인 경우에만 실행
  if (target.classList.contains('genre-button')) {
    const genre = target.dataset.genre; // 클릭된 버튼의 장르 가져오기

    // 선택된 장르를 toggle하기
    if (selectedGenres.value.has(genre)) {
      selectedGenres.value.delete(genre);
      target.classList.remove('selected')
    } else {
      // 최대 5개까지만 선택할 수 있도록 제한
      if (selectedGenres.value.size < 5) {
        target.classList.add('selected')
        selectedGenres.value.add(genre);
      } else {
        alert('최대 5개의 장르까지 선택할 수 있습니다.');
      }
    }
  }
};

onMounted(() => {
  const genresContainer = document.getElementById('genres');
  genresContainer.addEventListener('click', handleClick);
});


const submitGenres = async () => {
  // 선택된 장르를 배열로 변환하여 사용
  const selectedGenresArray = Array.from(selectedGenres.value);
  // 스토어에 장르들 저장
  accountStore.favGenres = selectedGenresArray
  
  for (const genre of selectedGenresArray) {
    axios({
      method: 'post',
      url: `${movieStore.API_URL}/api/v1/genres/${genre}/like/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
      .then(res => {
        router.push({ name: 'home' })
      })
      .catch(err => console.log(err))
  }
};
</script>

<style scoped>
/* #app {
  background-color: black;
  color: white;
  height: 100%;
  margin: 0;
}
*/

.outer {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 15rem;
  color: rgb(255, 255, 255);
  height: 100vh;
}

.cards {
  width: 40rem;
}

.genre-button {
  display: inline-block;
  margin: 10px;
  padding: 10px 20px;
  background-color: #ffffff;
  color: rgb(0, 0, 0);
  border: none;
  cursor: pointer;
  border-radius: 5px;
  transition: transform 0.2s ease-in-out;
  font-weight: bold;
}

/* 바로 아래 클래스는 genre-button과 selected 두 클래스가 동시에 있는 경우 선택됨 */
.genre-button.selected {
  background-color: rgb(250, 49, 49);
}

.genre-button:hover {
  transform: scale(1.2);
  background-color: rgb(248, 99, 99);
}

.submitbtn {
  background-color: white;
  width: 200px;
}
.btn-primary {
  background-color: rgb(197, 14, 14);
  border-width: 0;
  font-weight: bold;
}
.btn-primary:hover {
  background-color: darkred;
  border-color: darkred;
}
#app {
  width: 100vw;
  height: 100vh;
}
</style>