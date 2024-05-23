<template>
  <div>
    <div class="d-flex align-items-center mb-1">
      
      <div>
        <!-- 별점 선택 form -->
        <form name="myform" id="myform" @submit.prevent="submitReview" ref="formElem">
          <fieldset>
            <input type="radio" name="rating" value="5" id="rate1" v-model="rate" /><label for="rate1">⭐</label>
            <input type="radio" name="rating" value="4" id="rate2" v-model="rate" /><label for="rate2">⭐</label>
            <input type="radio" name="rating" value="3" id="rate3" v-model="rate"/><label for="rate3">⭐</label>
            <input type="radio" name="rating" value="2" id="rate4" v-model="rate"/><label for="rate4">⭐</label>
            <input type="radio" name="rating" value="1" id="rate5" v-model="rate"/><label for="rate5">⭐</label>

            <div class="userimgname">
              <!-- 내사진으로 img src 바꾸기 -->
              <img :src="accountStore.userInfo.image" alt="img" class="roundimg" />
              <p class="m-0">{{accountStore.userInfo.username}}</p>
            </div>
          </fieldset>

          <!-- 리뷰 작성 텍스트 에어리어 -->
          <textarea name="myreview" id="myreview" cols="69" rows="4" class="mb-1" v-model="content"></textarea>  
          <input type="submit" value="작성" style="width: 80px; height: 28px" />

        </form>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { computed, ref } from 'vue';
import { useMovieStore } from '@/stores/movie';
import { useAccountStore } from '@/stores/account';
import axios from 'axios';
import { defineProps } from 'vue';  // defineProps 사용하기

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
});

// const emit = defineEmits(['reviewSubmitted']);

const rate = ref('')
const content = ref('')
const movieStore = useMovieStore()
const accountStore = useAccountStore()
const formElem = ref(null)

const findUserReviewIndex = () => {
  return movieStore.detailReviews.findIndex(review => {
    return review.user.id === accountStore.userId
  });
};

// const isReviewCheck = computed(() => {
//   return findUserReviewIndex() !== -1;
// });

const submitReview = async () => {
  if (!rate.value || !content.value) {
    alert('평점과 리뷰 내용을 작성해주세요');
    return;
  }

  const reviewIndex = findUserReviewIndex();
  const reviewId = reviewIndex !== -1 ? movieStore.detailReviews[reviewIndex].id : -1


  movieStore.createOrUpdateReview(reviewId, rate.value, content.value).then(() => {
    if (formElem.value) {
      formElem.value.reset();
    }
    rate.value = '';
    content.value = '';
  }).catch(error => {
    console.error('There was an error!', error);
    alert('리뷰를 제출하는 도중 오류가 발생했습니다. 다시 시도해주세요.')
  });
};


</script>

<style scoped>
.userimgname {
  display: flex inline;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  margin: 0 8px 0 0;
}
</style>