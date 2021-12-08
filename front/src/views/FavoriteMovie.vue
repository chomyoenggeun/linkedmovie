<template>
  <div>
    <h1>내가 좋아하는 영화</h1>
    <div v-for="movieCard in movieCards"
    :key="movieCard">
      <div>
        {{ movieCard.like_users }}
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name:'FavoriteMovie',
  created:function(){ 
    this.$store.dispatch('LoadMovieCards',this.setToken())
  },
  computed:{
    ...mapState(['movieCards']),
  },
}
</script>

<style>

</style>