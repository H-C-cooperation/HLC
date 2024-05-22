<template>
    
    <!-- Button trigger modal -->
    <button type="button" class="btn bg-danger bg-opacity-75 text-white" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
        자세히 보기
    </button>

    <!-- Modal -->
    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <MovieDetail :movie-info="movie"></MovieDetail>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>

import MovieDetail from '@/components/movie/MovieDetail.vue'

const props = defineProps({
    movie:Object,
})


</script>

<style scoped>

</style>