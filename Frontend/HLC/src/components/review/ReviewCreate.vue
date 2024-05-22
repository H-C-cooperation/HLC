<template>
  <div>
    <div class="d-flex align-items-center mb-1">
      
      <div>
        <!-- 별점 선택 form -->
        <form name="myform" id="myform" @submit.prevent="handleSubmit">
          <fieldset>
            <input type="radio" name="rating" value="5" id="rate1" v-model="rate" /><label for="rate1">⭐</label>
            <input type="radio" name="rating" value="4" id="rate2" v-model="rate" /><label for="rate2">⭐</label>
            <input type="radio" name="rating" value="3" id="rate3" v-model="rate"/><label for="rate3">⭐</label>
            <input type="radio" name="rating" value="2" id="rate4" v-model="rate"/><label for="rate4">⭐</label>
            <input type="radio" name="rating" value="1" id="rate5" v-model="rate"/><label for="rate5">⭐</label>

            <div class="userimgname">
              <!-- 내사진으로 img src 바꾸기 -->
              <img :src="store.userInfo.image" alt="img" class="roundimg" />
              <p class="m-0">{{store.userInfo.username}}</p>
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
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';
import axios from 'axios';
import { defineProps } from 'vue';  // defineProps 사용하기

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['reviewSubmitted']);

const rate = ref(null)
const content = ref('')
const store = useMovieStore()

const handleSubmit = async () => {
  try {
    const response = await axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/movies/${props.movie.id}/reviews/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
      data: {
        rate: rate.value,
        content: content.value
      }
    })
    // 서버 응답에 따른 처리
    console.log(response.data);
    alert('리뷰가 성공적으로 제출되었습니다.');

    // 받은 응답을 emit로 부모에게 넘기고 부모가 추가된 review를 reviews에 저장시킴
    emit('reviewSubmitted', response.data);

    // 입력 필드 초기화 <== 이 부분은 이제 리뷰가 작성되어있습니다가 되야하는데.. 일단 이렇게 작성
    rate.value = null;
    content.value = '';

  } catch (error) {
    console.error('There was an error!', error);
    alert('리뷰를 제출하는 도중 오류가 발생했습니다. 다시 시도해주세요.');
  }
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