<template>
    <div>
        <span v-for="msg in messages" :key="msg">{{ msg }}</span>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
    movie: Object
});

const messages = ref([]);

const addMessage = (message) => {
    messages.value.push(message);
};

async function fetchChatGPTResponse(message, updateCallback) {
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${import.meta.env.VITE_GPT_KEY}`,
        },
        body: JSON.stringify({
            model: 'gpt-4',
            messages: [{ role: 'user', content: message }],
            stream: true,
        }),
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder('utf-8');
    let done = false;

    while (!done) {
        const { value, done: readerDone } = await reader.read();
        done = readerDone;

        if (value) {
            const decodedValue = decoder.decode(value, { stream: true });
            const lines = decodedValue.split('\n');
            
            for (const line of lines) {
                if (line.trim() !== '') {
                    const json = JSON.parse(line.slice(6));
                    const content = json.choices[0]?.delta?.content || '';
                    if (content) {
                        updateCallback(content);
                    }
                }
            }
        }
    }
}


fetchChatGPTResponse(`${props.movie.title} 영화의 간략 설명을 50자 이내로 해줘, 정보가 없다면 "정보가 없습니다."만 출력해줘`, addMessage);
</script>

<style scoped>
/* 스타일을 여기에 추가하세요 */
</style>
