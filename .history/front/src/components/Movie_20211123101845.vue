<template>
  <div>
    <h1>영화 디테일 페이지</h1>
    <div
    v-for="movieCard in movieCards"
    :key="movieCard.id"
    :movieCard="movieCard">
      <div v-if="movieCard.id == movieUrlNum">
        {{ movieCard.title }}
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
      movieUrlNum = null
    }
  },
  created: function(){
  this.$store.dispatch('LoadMovieCards',this.setToken())

  let movieUrlNum = window.location.href.split("movie/")[1]
    console.log(movieUrlNum)
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

</style>