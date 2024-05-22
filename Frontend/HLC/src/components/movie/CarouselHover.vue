<template>
    <span>
      {{ messages }}
    </span>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const apiKey = import.meta.env.VITE_GPT_KEY

const props = defineProps({
  movie: Object
});

const messages = ref('');

const data = {
  model: 'gpt-3.5-turbo',
  messages: [
    { role: 'system', content: '너는 영화를 설명하는 전문가야' },
    { role: 'user', content: `${props.movie.title}의 스토리에 대한 설명을 반드시 15자 이내로 해줘` }
  ],
  max_tokens: 50,
  n: 1,
  stop: null,
  temperature: 0.7
};

axios.post('https://api.openai.com/v1/chat/completions', data, {
  headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`
  }
})
  .then(res => {
    messages.value = res.data.choices[0].message.content
  })
  .catch(err => console.log(err))
</script>

<style scoped>
/* 스타일을 여기에 추가하세요 */
</style>
