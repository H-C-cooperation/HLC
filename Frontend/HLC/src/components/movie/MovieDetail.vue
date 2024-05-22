<template>
  <div v-if="store.detailMovie" class="outer bg-black">
    <div>
      <div class="cards videobox mb-3">
        <iframe v-if="store.detailMovie.youtube_url" :src="store.detailMovie.youtube_url" frameborder="0" width="100%" height="100%"></iframe>
      </div>
      <div class="cards d-flex mb-3">
        <div class="infobox title">{{ store.detailMovie.title }}</div>
        <div class="infobox cast">{{ store.detailMovie.actors && store.detailMovie.actors.length > 0 ? store.detailMovie.actors[0].name : 'Unknown' }}</div>
      </div>
      <div class="cards summarybox mb-3 scrollbar">{{ store.detailMovie.overview }}</div>

      <div class="cards reviewbox mb-3 scrollbar" v-if="detailReviews && detailReviews.length > 0">
          <Review v-for="review in detailReviews" :key="review.id" :review="review"></Review>
      </div>
      <div class="cards createreviewbox">
          <ReviewCreate v-if="store.detailMovie" :movie="store.detailMovie"></ReviewCreate>
      </div>
    </div>
  </div>
</template>

<script setup>
import Review from '@/components/review/Review.vue';
import ReviewCreate from '@/components/review/ReviewCreate.vue';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { storeToRefs } from 'pinia';
import { useMovieStore } from '@/stores/movie';
import axios from 'axios';

const route = useRoute();
const store = useMovieStore();
const {detailReviews} = storeToRefs(store)
// const props = defineProps({
//   movieInfo:Object
// })


// const loadMovieDetail = async () => {
//   try {
//     movie.value = await store.takeMovieDetail(props.movieInfo.id);
//   } catch (error) {
//     console.error('Failed to load movie detail:', error);
//   }
// };
// const loadReviews = async () => {
//   try {
//       reviews.value = await store.takeMovieDetailReview(props.movieInfo.id)
//   } catch (error) {
//       console.error('Failed to load reviews:', error);
//   }
// };

// const addReview = (review) => {
//   reviews.value.push(review);
// };

onMounted(() => {
  store.takeMovieDetail(route.params.moviePk);
  store.takeMovieDetailReview(route.params.moviePk);
  store.getUserInfo()
});

</script>

<style>
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
  width: 40rem;
}
/* 유튜브 영상 div */
.videobox {
  height: 20rem;
  border-radius: 15px 15px 0px 0px;
  background-color: rgb(231, 227, 227);
  color: black;
}
/* 영화제목, 출연진 div */
.infobox {
  border: solid white 2px;
  height: 5rem;
}
/* 영화제목 박스 글자스타일 */
.title {
  width: 27rem;
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
  border: solid white 2px;
  height: 10rem;
  padding: 15px;
  font-weight: bold;
  letter-spacing: 1px;
  line-height: 150%;
  overflow-y: scroll;
}

/* 리뷰 div */
.reviewbox {
  border: solid white 2px;
  height: 20rem;
  padding: 15px 30px;
  overflow-y: scroll;
}
/* 리뷰 작성 div */
.createreviewbox {
  border: solid white 2px;
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