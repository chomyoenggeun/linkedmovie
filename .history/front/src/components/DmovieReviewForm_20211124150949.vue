<template>
  <div>
    <h1>영화 리뷰 작성 폼</h1>
    <div>
      <v-autocomplete
        v-model="product"
        :items="products"
        label="Product"
        prepend-icon="work"
        chips
        color="blue"
      >
      </v-autocomplete>
      <v-autocomplete 
      :items="movieCards"
      item-text="title"
      item-value="movie_pk"
      filled
      rounded
      solo
      ></v-autocomplete>

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
      product:null
      products: [
        'Samson', 'Wichita', 'Combustion', 'Triton',
        'Helios', 'Wimbeldon', 'Brixton', 'Iguana',
        'Xeon', 'Falsy', 'Armagedon', 'Zepellin'],
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
  },
  computed:{
    ...mapState(['movieCards']),
  },
}
</script>

<style>

</style>