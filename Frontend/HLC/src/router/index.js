import { createRouter, createWebHistory } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import { useAccountStore } from '@/stores/account'
// movie
import HomeView from '@/views/HomeView.vue'
import MovieView from '@/views/MovieView.vue'
import MovieDetailView from '@/components/movie/MovieDetail.vue'
import FavoriteMovieView from '@/views/FavoriteMovieView.vue'
// review
import ReviewView from '@/components/review/Review.vue'
import ReviewCreate from '@/components/review/ReviewCreate.vue'
// account
import ProfileView from '@/views/ProfileView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
// genreselect
import GenreSelectView from '@/views/GenreSelectView.vue'
// search
import SearchView from '@/views/SearchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/select',
      name: 'select',
      component: GenreSelectView,
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/movie',
      name: 'movie',
      component: MovieView,
    },
    {
      path: '/favorite',
      name: 'favorite',
      component: FavoriteMovieView,
    },
    {
      path: '/movie/:moviePk',
      name: 'movieDetail',
      component: MovieDetailView,
    },
    {
      path: '/movie/:moviePk/review',
      name: 'review',
      component: ReviewView,
    },
    {
      path: '/movie/:moviePk/create',
      name: 'reviewCreate',
      component: ReviewCreate
    },
    {
      path: '/profile/:userPk',
      name: 'profile',
      component: ProfileView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/search/:keyword',
      name: 'search',
      component: SearchView
    }
  ]
})

router.beforeEach((to, from) => {
  const movieStore = useMovieStore()
  const accountStore = useAccountStore()
  accountStore.getUserInfo()

  if (to.name !== 'login' && to.name !== 'signup' && to.name !== 'select') {
    movieStore.navFootView = true
  } else {
    movieStore.navFootView = false
  }

  if (to.name === 'home') {
    accountStore.getGenres()
  }
})

export default router
