<template>
  <div>
    <section>
      <router-link :to="{ name : 'Movie',params:{movieId:movieCard.id }}"
      @dblclick="likeMovie"
      :movieCard="movieCard">
        <div class="container">
          <div class="card item front" style="width: 18rem;">
            <img :src="`https://image.tmdb.org/t/p/original${movieCard.poster_path}`">
            <div class="card-body">
              <h5>{{ movieCard.title}}</h5>
              <p class="overview">{{ movieCard.overview}}</p>
            </div>
          </div>
        </div>
      </router-link>
    </section>  
  </div>
</template>

<script>

export default {
  name: 'MovieCard',
  props:{
    movieCard : Object
  },
  methods:{
    setToken : function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    // likeMovie:function(){
    //   this.$store.dispatch('LikeMovie',this.setToken())
    // }
  }
}
</script>

<style>
.overview{
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  line-height: 1.2;
  width: 230px;
  height:58px;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}
.card-body{
  background: rgb(6, 21, 66);
  color: aliceblue;
}


</style>