<template>
  <div id="detail">
    <h1>영화 디테일 페이지</h1>
    <div
    v-for="movieCard in movieCards"
    :key="movieCard.id"
    :movieCard="movieCard">
    <div class="container">
      <div v-if="movieCard.id == movieUrlNum" class="movie-box"> 
        <div class="poster-box">
          <div class="movie-poster">
            <img :src="`https://image.tmdb.org/t/p/original${movieCard.poster_path}`">
          </div>
        </div>
        <div class="overview-box container">
          <div class="movie-overview">
            <h1>{{ movieCard.title }}</h1>

            <!-- 장르 -->
            <div
            v-for="genre in movieCard.genres"
            :key='genre'>
              <div
              v-for="genreDataItem in genreData"
              :key="genreDataItem">
                <div v-if="genre == genreDataItem">
                  {{ genreDataItem }}
                </div>
              </div>
            </div>


            <p>개봉일 : {{ movieCard.release_date }}</p>
            <p>스토리: {{ movieCard.overview }}</p>
            <!-- <p>이 영화를 좋아하는 사람 : {{ like_users }}</p> -->
          </div>
          <div class="like-button">
            <button>좋아요</button>
          </div>
        </div>
      </div>
    </div>
    </div>
    <div class="review-box">
      <!-- <movie-review></movie-review> -->
      <movie-review></movie-review>
    </div>
  </div>
</template>

<script>
import MovieReview from '@/components/MovieReview.vue'
import { mapState } from 'vuex'

export default {
  name: 'Movie',
  components:{
    MovieReview
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
  this.$store.dispatch('LoadGenreData',this.setToken())

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
  ...mapState(['movieCards','genreData']),
  },
}
</script>

<style>
body{
  background-image:url(`https://image.tmdb.org/t/p/original${movieCard.poster_path}`);
}
img {
  width:400px;
}
.movie-poster{
  float: left;
}
.movie-ovierview{
  float: left;
  padding: 20px;
  color: aliceblue;
  background-color: blueviolet;
}
.movie-box{
  clear: both;
}
.review-box{
  clear:both;
}
.overview-box{
  padding: 20px;
  color: #dddddd;
  background: rgb(6,5,87);
  background: linear-gradient(180deg, rgba(6,5,87,1) 0%, rgba(43,12,69,1) 100%);
}
.like-button{
  float:left;
  padding: auto;
  background-color: rgb(6,5,87);
}
</style>