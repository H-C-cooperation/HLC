import { createRouter, createWebHistory } from 'vue-router'
// movie
import HomeView from '@/views/HomeView.vue'
import MovieView from '@/views/MovieView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import FavoriteMovieView from '@/views/FavoriteMovieView.vue'
// review
import ReviewView from '@/views/ReviewView.vue'
import ReviewCreate from '@/components/review/ReviewCreate.vue'
// recommend
import Recommendation from '@/components/movie/MovieRecommendation.vue'
// account
import ProfileView from '@/views/ProfileView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
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
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
  ]
})

export default router
