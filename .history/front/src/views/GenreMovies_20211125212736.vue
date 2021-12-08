<template>
  <div>
    {{ genreData }}
    <div >

    </div>
  </div>
</template>

<script>
export default {
  name : 'GenreNovies',
  created: function(){
    this.$store.dispatch('LoadGenreData',this.setToken())
    this.$store.dispatch('LoadMovieCards',this.setToken())
  },
  computed:{
    movieCards: function(){
      return this.$store.state.movieCards
    },
    genreData: function(){
      return this.$store.state.genreData
    }
  }


}
</script>

<style>

</style>