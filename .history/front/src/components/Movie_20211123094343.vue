<template>
  <div>
    <h1>영화 디테일 페이지</h1>
    <div>
      {{ movieCard }}
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
  },
}
</script>

<style>

</style>