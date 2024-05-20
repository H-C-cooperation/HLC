import { createRouter, createWebHistory } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
// movie
import HomeView from '@/views/HomeView.vue'
import MovieView from '@/views/MovieView.vue'
import MovieDetailView from '@/components/movie/MovieDetail.vue'
import FavoriteMovieView from '@/views/FavoriteMovieView.vue'
// review
import ReviewView from '@/components/review/Review.vue'
import ReviewCreate from '@/components/review/ReviewCreate.vue'
// recommend
import Recommendation from '@/views/RecommendationView.vue'
// account
import ProfileView from '@/views/ProfileView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movie',
      name: 'movie',
      component: MovieView
    },
    {
      path: '/favorite',
      name: 'favorite',
      component: FavoriteMovieView
    },
    {
      path: '/movie/:moviePk',
      name: 'movieDetail',
      component: MovieDetailView
    },
    {
      path: '/movie/:moviePk/review',
      name: 'review',
      component: ReviewView
    },
    {
      path: '/movie/:moviePk/create',
      name: 'reviewCreate',
      component: ReviewCreate
    },
    {
      path: '/recommendation',
      name: 'recommend',
      component: Recommendation
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useMovieStore()
  if (to.name !== 'login' && to.name !== 'signup' && store.isLogin === false) {
    window.alert('로그인이 필요합니다.')
    return { name: 'login' }
  } else {
    store.getMovies()
  }
})

export default router
