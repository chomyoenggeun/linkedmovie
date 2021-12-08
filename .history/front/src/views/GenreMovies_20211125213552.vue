<template>
  <div>
    {{ genreData.length }}
    <div v-for="genreDataItem in genreData"
    :key="genreDataItem.id">
      <div v-for="movieCard in movieCards"
      :key="movieCard.id">

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name : 'GenreNovies',
  methods:{
    setToken : function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
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