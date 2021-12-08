<template>
  <div>
    <h1>영화 디테일 페이지</h1>
    <div
    v-for="movieCard in movieCards"
    :key="movieCard.id"
    :movieCard="movieCard">
      <div v-if="movieCard.id == movieUrlNum" class="movie-box">
        <div class="movie-poster">
          <img :src="`https://image.tmdb.org/t/p/original${movieCard.poster_path}`">
        </div>
        <div class="movie-overview">
          <h1>{{ movieCard.title }}</h1>
          <p v-for="genre in movieCard.genres"
          :key="genre">장르 : {{ genre }}</p>
          {{ movieCard.genres.length }}
          <p>개봉일 : {{ movieCard.release_date }}</p>
          <p>스토리: {{ movieCard.overview }}</p>
          <!-- <p>이 영화를 좋아하는 사람 : {{ like_users }}</p> -->
        </div>
      </div>
    </div>
    <div class="review-box">
      <!-- <movie-review></movie-review> -->
      <dmovie-review-list></dmovie-review-list>
    </div>
  </div>
</template>

<script>
import DmovieReviewList from '@/components/DmovieReviewList.vue'
import { mapState } from 'vuex'

export default {
  name: 'Movie',
  components:{
    DmovieReviewList
    // MovieReview,
  },
  data:function(){
    return{
      movieUrlNum : null,
      // genre : []
    }
  },
  created: function(){
  this.$store.dispatch('LoadMovieCards',this.setToken())
  // this.$store.dispatch('LoadGenreData',this.setToken())

  let movieUrl = window.location.href.split("movie/")[1]
  this.movieUrlNum = movieUrl

  console.log(this.movieCard)

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
.movie-poster{
  float: left;
}
.movie-ovierview{
  float: left;
}
.movie-box{
  clear: both;
}
.review-box{
  clear:both;

}
</style>