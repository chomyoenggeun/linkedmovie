<template>
  <div>

  </div>
</template>

<script>
export default {
  name : 'GenreNovies',
  created: function(){
    this.$store.dispatch('LoadGenreData',this.setToken())
    this.$store.dispatch('LoadMovieCards',this.setToken())
  },

}
</script>

<style>

</style>