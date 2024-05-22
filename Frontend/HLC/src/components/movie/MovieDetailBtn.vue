<template>
    <div>
        <!-- 모달 구현 실패 -->
        <!-- <button type="button" class="btn bg-danger bg-opacity-75 text-white" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
            자세히 보기
        </button>
    
        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-xl">
                <div class="modal-content custom-modal-size">
                    <div class="modal-header bg-black">
                        <h1 class="modal-title fs-5 text-white" id="staticBackdropLabel">영화 상세 정보</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body bg-black no-scrollbar">
                        <MovieDetail :movie-info="movie"></MovieDetail>
                    </div>
                </div>
            </div>
        </div> -->

        <button type="button" class="btn bg-danger bg-opacity-75 text-white" @click="goToMovieDetail(movie.id)">
            자세히 보기
        </button>
    </div>


</template>

<script setup>
import MovieDetail from '@/components/movie/MovieDetail.vue'
import { useRouter } from 'vue-router';

const props = defineProps({
    movie:Object,
})

const router = useRouter()

const goToMovieDetail = (moviePk) => {
  router.push({ name: 'movieDetail', params: { moviePk } });
};



</script>

<style scoped>
/* Hide scrollbar for WebKit browsers */
.no-scrollbar::-webkit-scrollbar {
  display: none;
}

.modalwidth{
    width: 800px;
    
}

.modal-xl {
  max-width: 800px; /* Adjust the max-width as needed */
}

.custom-modal-size {
  width: 100%; /* Full width of the container */
  height: 90vh; /* 90% of the viewport height */
}

.btn-close {
  filter: invert(1); /* Changes the color to white */
}

</style>