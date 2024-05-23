<template>
  <div v-if="movieStore.detailMovie" class="outer bg-black noto-sans-kr">
    <div class="border-top border-bottom border-danger border-opacity-50 border-4 p-5 bg-dark rounded">
      <div class="cards videobox mb-3">
        <iframe v-if="movieStore.detailMovie.youtube_url" :src="movieStore.detailMovie.youtube_url" frameborder="0" width="100%" height="100%"></iframe>
      </div>
      <div class="my-3 p-2">
        <h1 class="text-danger text-opacity-75 fw-bold underline mb-3">Title</h1>
        <div class="infobox title d-flex justify-content-around">
          <span>
            {{ movieStore.detailMovie.title }}
          </span>
          <div class=" hearts">
            <!-- if 내가 좋아요 했다면 빨간하트 ( )-->
            <div v-if="isLiked" class="text-center">
              <p class="redheart fs-1 mb-0" @click="toggleLike">❤️</p>
              <p style="font-size: 13px" class="my-0">{{ movieStore.detailMovie && movieStore.detailMovie.like_users ? movieStore.detailMovie.like_users.length : 0 }}</p>
            </div>
            <!-- else 하얀하트 ( ) -->
            <div v-else class="text-center">
              <p class="whiteheart fs-1 mb-0" @click="toggleLike">❤️</p>
              <p style="font-size: 13px" class="my-0">{{ movieStore.detailMovie && movieStore.detailMovie.like_users ? movieStore.detailMovie.like_users.length : 0 }}</p>
            </div>
            <!-- 하트 누를 때마다 좋아요 했다안했다되고 색깔도 바뀌도록( ) -->
          </div>
        </div>
      </div>

      <div>
        <h1 class="text-danger text-opacity-75 fw-bold underline mb-3">Overview</h1>
        <div class="cards summarybox mb-3">{{ movieStore.detailMovie.overview }}</div>
      </div>

      <h1 class="text-danger text-opacity-75 fw-bold underline mb-3">Review</h1>
      <div class="cards reviewbox mb-3 scrollbar" v-if="detailReviews && detailReviews.length > 0">
        <Review v-for="review in detailReviews" :key="review.id" :review="review"></Review>
      </div>
      <div v-else>
        <h3 class="my-5 text-center p-5">아직 리뷰가 없습니다..! 😐</h3>
      </div>
      <h1 class="text-danger text-opacity-75 fw-bold underline mb-3">Make Your Own</h1>
      <div class="cards createreviewbox">
          <ReviewCreate v-if="movieStore.detailMovie" :movie="movieStore.detailMovie"></ReviewCreate>
      </div>
    </div>
  </div>
</template>

<script setup>
import Review from '@/components/review/Review.vue';
import ReviewCreate from '@/components/review/ReviewCreate.vue';
import { ref, onMounted, computed, watch } from 'vue';
import { onBeforeRouteLeave, useRoute } from 'vue-router';
import { storeToRefs } from 'pinia';
import { useMovieStore } from '@/stores/movie';
import { useAccountStore } from '@/stores/account';
import axios from 'axios';

const route = useRoute();
const movieStore = useMovieStore();
const accountStore = useAccountStore()
const {detailReviews} = storeToRefs(movieStore)

const isLiked = computed(() => {
  if (movieStore.detailMovie && movieStore.detailMovie.like_users) {
    return movieStore.detailMovie.like_users.includes(accountStore.userId);
  }
  return false;
});


const toggleLike = async () => {
  try {
    const response = await axios({
      method: 'post',
      url: `${movieStore.API_URL}/api/v1/movies/${movieStore.detailMovie.id}/like/`,
      headers: {
        Authorization: `Token ${accountStore.token}`,
      },
    })
    // 서버 응답에 따라 like_users 업데이트
    console.log(response.data)

    movieStore.detailMovie.like_users = response.data.like_users;
    // console.log(response.data)

  } catch (error) {
    console.error('Failed to toggle like:', error);
    alert('좋아요를 변경하는 도중 오류가 발생했습니다. 다시 시도해주세요.');
  }
};

onMounted(() => {
  movieStore.takeMovieDetail(route.params.moviePk);
  movieStore.takeMovieDetailReview(route.params.moviePk);
  accountStore.getUserInfo();
});

onBeforeRouteLeave((to, from) => {
  movieStore.detailMovie.value = null
  movieStore.detailReviews.values = null
})

watch(
  () => route.params.moviePk,
  (newMoviePk, oldMoviePk) => {
    if (newMoviePk !== oldMoviePk) {
      movieStore.takeMovieDetail(route.params.moviePk);
      movieStore.takeMovieDetailReview(route.params.moviePk);
    }
  }
);

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Noto+Sans+KR:wght@100..900&display=swap');

.scrollbar::-webkit-scrollbar {
  display: none;
}

.outer {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 70px;
  color: white;
  
}

.cards {
  width: 50rem;
}
/* 유튜브 영상 div */
.videobox {
  height: 30rem;
  border-radius: 15px 15px 0px 0px;
  background-color: rgb(231, 227, 227);
  color: black;
}
/* 영화제목, 출연진 div */
.infobox {
  width: 100%;
  border: solid wite 2px;
  height: 5rem;
}
/* 영화제목 박스 글자스타일 */
.title {
  width: 100%;
  font-size: 30px;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* 출연진 박스 글자스타일 */
.cast {
  width: 13rem;
  padding: 10px;
  font-size: 15px;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* 영화 줄거리 div */
.summarybox {
  padding: 20px 10px;
  font-size: 18px;
  font-weight: bold;
  letter-spacing: 1px;
  line-height: 150%;
}

/* 리뷰 div */
.reviewbox {
  height: 20rem;
  padding: 15px 30px;
  overflow-y: scroll;
}
/* 리뷰 작성 div */
.createreviewbox {
  border-radius: 0px 0px 15px 15px;
  height: 15rem;
  padding: 15px 30px;
}

.roundimg {
  width: 43px;
  height: 43px;
  border-radius: 50%;
}

.reviews {
  display: flex;
  flex-direction: column;
  justify-content: center;
  font-size: 16px;
  width: 320px;
}
.reviewcontent {
  width: 310px;
  font-weight: bold;
  overflow: hidden;
  word-wrap: break-word;
}
.hearts {
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.redstar {
  font-size: 1.3em; /* 이모지 크기 */
  color: transparent; /* 기존 이모지 컬러 제거 */
  text-shadow: 0 0 0 #a00;
}
.whitestar {
  font-size: 1.3em; /* 이모지 크기 */
  color: transparent; /* 기존 이모지 컬러 제거 */
  text-shadow: 0 0 0 #f0f0f0;
}
.redheart {
  font-size: 1.3em; /* 이모지 크기 */
  color: transparent; /* 기존 이모지 컬러 제거 */
  text-shadow: 0 0 0 #a00;
}
.whiteheart {
  font-size: 1.3em; /* 이모지 크기 */
  color: transparent; /* 기존 이모지 컬러 제거 */
  text-shadow: 0 0 0 #f0f0f0;
}

.underline {
  text-decoration: underline;
  text-underline-offset: 15px;
}

.noto-sans-kr {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-weight: 200;
  font-style: normal;
}

/* 별점 선택 */
#myform fieldset {
  display: inline-block; /* 하위 별점 이미지들이 있는 영역만 자리를 차지함.*/
  direction: rtl; /* 이모지 순서 반전 */
  border: 0; /* 필드셋 테두리 제거 */
}
#myform input[type="radio"] {
  display: none; /* 라디오박스 감춤 */
}
#myform label {
  font-size: 1.3em; /* 이모지 크기 */
  color: transparent; /* 기존 이모지 컬러 제거 */
  text-shadow: 0 0 0 #f0f0f0; /* 새 이모지 색상 부여 */
}
#myform label:hover {
  text-shadow: 0 0 0 #a00; /* 마우스 호버 */
}
#myform label:hover ~ label {
  text-shadow: 0 0 0 #a00; /* 마우스 호버 뒤에오는 이모지들 */
}
#myform input[type="radio"]:checked ~ label {
  text-shadow: 0 0 0 #a00; /* 마우스 클릭 체크 */
}
</style>