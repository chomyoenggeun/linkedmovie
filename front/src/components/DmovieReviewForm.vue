<template>
  <div>
    <h1>영화 리뷰 작성 폼</h1>
    <div
    v-for="movieCard in movieCards"
    :key="movieCard">
      
    </div>
    <div>
      <v-autocomplete 
      :items="movieCards"
      item-text="title"
      item-value="movie_pk"
      filled
      rounded
      solo
      v-model="movieReviewItem.movie_pk"
      ></v-autocomplete>
      <p>글제목</p>
      <input type="text"
      v-model="movieReviewItem.title">
      <p>평점</p>
      <input type="text"
      v-model="movieReviewItem.rank">
      <p>내용</p>
      <input type="text"
      v-model="movieReviewItem.content">
      <button @click="createMovieReveiw">저장</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name:'DmovieReviewForm',
  data(){
    return{
      movieReviewItem:{
        title : null,
        movie_title : null,
        rank : 5,
        content : null,
        movie_pk : null
      },
      movieData:[]
    }
  },
  methods:{
    setToken : function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
  created:{
    getMovieData : function(){
      this.$store.dispatch('LoadMovieCards',this.setToken())
    },
    // for(let movieTitlePk in movieCards){
    //   console.log(movieTitlePk)
    // }
    // createMovieReview
  },
  computed:{
    ...mapState(['movieCards']),
  },
}
</script>

<style>

</style>