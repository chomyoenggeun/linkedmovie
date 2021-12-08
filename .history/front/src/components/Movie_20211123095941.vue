<template>
  <div>
    <h1>영화 디테일 페이지</h1>
    <div
    v-for="movieCard in movieCards"
    :key="movieCard.id"
    :movieCard="movieCard">
      <!-- <div v-if="movieCard.id === ">

      </div> -->
    </div>
    <movie-review></movie-review>
  </div>
</template>

<script>
import MovieReview from '@/components/MovieReview.vue'

export default {
  name: 'Movie',
  components:{
    MovieReview,
  },
  props:{
    movieCard : Object
  },
    created: function(){
    this.$store.dispatch('LoadMovieCards',this.setToken())

    let url = window.location.href
    console.log(url)
  },
  methods :{
    setToken : function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  }
}
</script>

<style>

</style>