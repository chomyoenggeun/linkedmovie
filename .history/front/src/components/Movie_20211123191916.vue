<template>
  <div>
    <h1>영화 디테일 페이지</h1>
    <div
    v-for="movieCard in movieCards"
    :key="movieCard.id"
    :movieCard="movieCard">
      <div v-if="movieCard.id == movieUrlNum">
        <img :src="`https://image.tmdb.org/t/p/original${movieCard.poster_path}`">
        <h1>{{ movieCard.title }}</h1>
        <p>장르 : {{ movieCard.genres[0] }}</p>
        <p>개봉일 : {{ movieCard.release_date }}</p>
        <p>스토리: {{ movieCard.overview }}</p>
        <p>이 영화를 좋아하는 사람 : {{ like_users }}</p>
      </div>
      <div v-else>
        <!-- {{ movieCard.title}} -->
      </div>
    </div>
    <movie-review></movie-review>
  </div>
</template>

<script>
import MovieReview from '@/components/MovieReview.vue'
import { mapState } from 'vuex'

export default {
  name: 'Movie',
  components:{
    MovieReview,
  },
  data:function(){
    return{
      movieUrlNum : null
    }
  },
  created: function(){
  this.$store.dispatch('LoadMovieCards',this.setToken())

  let movieUrl = window.location.href.split("movie/")[1]
  this.movieUrlNum = movieUrl

  },
  methods :{
    setToken : function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
    computed:{
    ...mapState(['movieCards']),
  },
}
</script>

<style>
img {
  width:400px;

}
</style>