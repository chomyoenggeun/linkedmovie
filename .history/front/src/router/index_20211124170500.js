import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Account from '../views/accounts/Account.vue'
import Login from '../views/accounts/Login.vue'
import Signup from '../views/accounts/Signup.vue'
import FavoriteMovie from '../views/FavoriteMovie.vue'
import Mypage from '../views/Mypage.vue'
import Movie from '../components/Movie.vue'
import Review from '../views/Review.vue'
import MovieReviewForm from '../components/MovieReviewForm.vue'
import MovieReviewCommunity from '../components/MovieReviewCommunity.vue'
// import MovieReviewCreate from '../components/MovieReviewCreate.vue'
import DmovieReviewDetail from '../components/DmovieReviewDetail.vue'
import DmovieReviewForm from '../components/DmovieReviewForm.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/favorite-movie',
    name: 'FavoriteMovie',
    component : FavoriteMovie
  },
  /////////////////////////////////
  //account//
  {
    path: '/account',
    name: 'Account',
    component : Account,
  },
  {
    path: '/account/login',
    name: 'Login',
    component : Login,
  },
  {
    path: '/account/signup',
    name: 'Signup',
    component : Signup,
  },
  //account//
  /////////////////////////////////  
  {
    path: '/mypage',
    name: 'Mypage',
    component : Mypage,
  },
  {
    path: '/home/movie/:movieId',
    name: 'Movie',
    component : Movie
  },
///////////////////////////////////////////////////
//////////리뷰작성///////////
  {
    path: '/review',
    name: 'Review',
    component : Review
  },
  {
    path: '/review/create',
    name: 'MovieReviewForm',
    component : MovieReviewForm
  },
  {
    path: '/review/detail/:reviewId',
    name: 'MovieReviewCommunity',
    component: MovieReviewCommunity
  },
  ////////////////////////////////////////////////////////
  // {
  //   path: '/movie-review-create',
  //   name: 'MovieReviewCreate',
  //   component : MovieReviewCreate
  // },
  {
    path: '/movie/review/detail/:movieReviewId/:movieTitle',
    name: 'DmovieReviewDetail',
    component:DmovieReviewDetail
  },
  {
    path: '/movie/review/create',
    name: 'DmovieReviewForm',
    component: DmovieReviewForm
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
