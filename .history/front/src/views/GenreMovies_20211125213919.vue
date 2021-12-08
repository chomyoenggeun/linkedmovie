<template>
  <div>
    <div v-for="content in genreData.length"
    :key="content">
      <div v-for="genreDataItem in genreData"
      :key="genreDataItem.id">
        <div v-for="movieCard in movieCards"
        :key="movieCard.id">
          <div for v-if="genreId in movieCard.genres"
          :key="genreId.id">
            <div v-if="genreId == genreDataItem">
              <img :src="`https://image.tmdb.org/t/p/original${movieCard.poster_path}`" class="image-size-random">
            </div>
          </div>
        </div>
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