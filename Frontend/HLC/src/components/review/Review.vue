<template>
  <div class="d-flex align-items-center">
    <div class="userimgname">
      <!-- img src 리뷰쓴 유저이미지로 고치기( ) -->
      <img :src="review.user.image" alt="img" class="roundimg" /> 
      <p class="m-0">{{ review.user.username }}</p>
    </div>
    <div style="width: 160px">
      <!-- for 문으로 이 유저가 준 별점만큼 바로 아래의 span태그를 반복하기 ( )-->
      <span class="redstar" v-for="n in review.rate">⭐</span>
      <!-- for문으로 (5-별점)만큼 바로 아래의 span태그를 반복하기( ) -->
      <span class="whitestar" v-for="n in (5 - review.rate)">⭐</span>
    </div>
    <div class="reviews">
      <div class="reviewcontent">{{ review.content}}</div>
      <div style="font-size: 13px">{{ review.formatted_updated_at }}</div>
    </div>
    <div class="d-flex hearts">
      <!-- if 내가 좋아요 했다면 빨간하트 ( )-->
      <span class="redheart" v-if="isLiked" @click="toggleLike">❤️</span>
      <!-- else 하얀하트 ( ) -->
      <span class="whiteheart" v-else @click="toggleLike">❤️</span>
      <!-- 하트 누를 때마다 좋아요 했다안했다되고 색깔도 바뀌도록( ) -->
      <span style="font-size: 13px">{{ review.like_users.length }}</span>
    </div>
  </div>
  
</template>

<script setup>
import { computed } from 'vue';
import { useMovieStore } from '@/stores/movie';
import axios from 'axios';

const store = useMovieStore()

const props = defineProps({
  review:Object,
})

const isLiked = computed(() => {
  return props.review.like_users.includes(store.userId);
});

const toggleLike = async () => {
  try {
    const response = await axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/reviews/${props.review.id}/like/`,
      headers: {
        Authorization: `Token ${store.token}`,
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


</script>

<style scoped>

</style>