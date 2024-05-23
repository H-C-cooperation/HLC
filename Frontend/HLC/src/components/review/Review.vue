<template>
  <div class="d-flex align-items-center justify-content-between">
    <div class="userimgname" @click="goProfile(review.user.id)">
      <!-- img src 리뷰쓴 유저이미지로 고치기( ) -->
      <img :src="review.user.image" alt="img" class="roundimg" /> 
      <p class="m-0">{{ review.user.username }}</p>
    </div>
    <div>
      <!-- for 문으로 이 유저가 준 별점만큼 바로 아래의 span태그를 반복하기 -->
      <template v-if="review.rate > 0">
        <span class="redstar" v-for="n in review.rate">⭐</span>
      </template>
      <!-- for문으로 (5-별점)만큼 바로 아래의 span태그를 반복하기 -->
      <template v-if="review.rate < 5">
        <span class="whitestar" v-for="n in (5 - review.rate)">⭐</span>
      </template>
    </div>
    <div class="reviews">
      <div>
        <div class="reviewcontent">{{ review.content}}</div>
        <div style="font-size: 13px">{{ review.formatted_updated_at }}</div>
      </div>
    </div>
    <div class="d-flex text-center align-items-center">
      <div>
        <div v-if="isLiked">
          <!-- if 내가 좋아요 했다면 빨간하트 ( )-->
          <span class="redheart" @click="toggleLike">❤️</span>
          <p style="font-size: 13px">{{ review.like_users.length }}</p>
        </div>
        <div v-else>
          <!-- else 하얀하트 ( ) -->
          <span class="whiteheart"  @click="toggleLike">❤️</span>
          <p style="font-size: 13px">{{ review.like_users.length }}</p>
        </div>
      </div>
      <div data-bs-theme="dark" class="ms-2 mb-2">
        <button @click="movieStore.deleteReview(review.id)" v-if="accountStore.userId === review.user.id" class="btn-close text-white" aria-label="Close"></button>
        <div v-else class="ms-4"></div>
      </div>
    </div>
  </div>
  
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useMovieStore } from '@/stores/movie';
import { useAccountStore } from '@/stores/account';
import { useRouter } from 'vue-router';

import axios from 'axios';

const router = useRouter()
const movieStore = useMovieStore()
const accountStore = useAccountStore()

onMounted(() => {
  accountStore.getUserInfo()
});

const props = defineProps({
  review:Object,
})

const isLiked = computed(() => {
  return props.review.like_users.includes(accountStore.userId);
});

const toggleLike = async () => {
  try {
    const response = await axios({
      method: 'post',
      url: `${movieStore.API_URL}/api/v1/reviews/${props.review.id}/like/`,
      headers: {
        Authorization: `Token ${accountStore.token}`,
      },
      
    })
    // 서버 응답에 따라 like_users 업데이트
    props.review.like_users = response.data.like_users;
    console.log(response.data)

  } catch (error) {
    console.error('Failed to toggle like:', error);
    alert('좋아요를 변경하는 도중 오류가 발생했습니다. 다시 시도해주세요.');
  }
};

const goProfile = (userId) => {
  router.push({ name: 'profile', params:{userPk:userId}})
}

</script>

<style scoped>
.userimgname:hover {
  background-color: rgba(255, 255, 255, 0.1); /* 호버 시 배경색 변경 */
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* 그림자 효과 추가 */
  cursor: pointer; /* 커서를 손가락 모양으로 변경하여 클릭 가능함을 강조 */
}
</style>