import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useAccountStore } from './account'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const accountStore = useAccountStore()
  // 좋아하는 장르 리스트

  // Movie Detail 에서 사용
  const detailMovie = ref({})
  const detailReviews = ref([])

  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      },
      params: {
        mode: 'popularity',
      }
    })
      .then(res => {
        movies.value = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }

  const getMoviesByGenre = async function (genre) {
    try {
      const response = await axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        params: {
          mode: 'genre',
          inputGenre: `${genre}`
        },
        headers: {
          Authorization: `Token ${accountStore.token}`,
        },
      });
      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  // 알고리즘으로 영화 가져오기 (군집 알고리즘)
  const getMovieByAlgorithm = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`,
      params: {
        mode: 'algorithm'
      },
      headers: {
        Authorization: `Token ${accountStore.token}`,
      }
    })
      .then(res => {
        return res.data
      })
      .catch(err => console.log(err))
  }

  // 런타임으로 영화 가져오기
  const getMovieByRuntime = function (runtime) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`,
      params: {
        mode: 'runtime',
        inputRuntime: runtime
      },
      headers: {
        Authorization: `Token ${accountStore.token}`,
      }
    })
      .then(res => {
        return res.data
      })
      .catch(err => console.log(err))
  }

  // MovieDetail (영화 단일 조회)
  const takeMovieDetail = async function (movie_pk) {
    try {
      const response = await axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movie_pk}`,
        headers: {
          Authorization: `Token ${accountStore.token}`,
        },
      });
      detailMovie.value =  response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  // 영화에 연결된 리뷰 리스트 조회
  const takeMovieDetailReview = async function (movie_pk) {
    try {
      const response = await axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movie_pk}/reviews`,
        headers: {
          Authorization: `Token ${accountStore.token}`,
        },
      });
      detailReviews.value = response.data
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  // review 생성 , 업데이트  동시에 할 수 있게해주는 함수
  const createOrUpdateReview = async function(reviewId, rate, content) {
    let response;
    try {
      console.log('reviewId---', reviewId)
      if (reviewId !== -1) {
        // Update existing review
          response = await axios({
          method: 'patch',
          url: `${API_URL}/api/v1/movies/${detailMovie.value.id}/reviews/${reviewId}/`,
          headers: {
            Authorization: `Token ${accountStore.token}`,
          },
          data: {
            rate,
            content
          }
        });
        console.log('DB에서 리뷰 수정 작업이 완료되었습니다.');
  
        // Update the local review list
        detailReviews.value = detailReviews.value.map((review) => {
          if (review.id === reviewId) {
            review.rate = rate;
            review.content = content;
          }
          return review;
        });
      } else {
        // Create new review
        response = await axios({
          method: 'post',
          url: `${API_URL}/api/v1/movies/${detailMovie.value.id}/reviews/`,
          headers: {
            Authorization: `Token ${accountStore.token}`,
          },
          data: {
            rate,
            content
          }
        });
        // Add the new review to the local review list
        detailReviews.value.push(response.data);
        console.log('리뷰가 성공적으로 작성되었습니다.');
      }
  
    } catch (error) {
      console.error('There was an error!', error);
      alert('리뷰를 제출하는 도중 오류가 발생했습니다. 다시 시도해주세요.');
    }
  };

  const deleteReview = function (reviewId) {
    axios({
      method:'delete',
      url: `${API_URL}/api/v1/movies/${detailMovie.value.id}/reviews/${reviewId}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`,
      },
    })
      .then(res => console.log('DB에서 리뷰 삭제 작업이 완료되었습니다.'))
      .catch(err => console.log(err))
    
      const index = detailReviews.value.findIndex((review) => review.id === reviewId)
      detailReviews.value.splice(index, 1)
  }
  
  return { movies, API_URL, getMovies, getMoviesByGenre, detailMovie, detailReviews, takeMovieDetail, takeMovieDetailReview, createOrUpdateReview, deleteReview, 
    getMovieByAlgorithm, getMovieByRuntime }
}, { persist: true })
