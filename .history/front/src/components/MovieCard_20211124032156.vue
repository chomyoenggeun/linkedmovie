<template>
  <div>
    <section class="list">
      <router-link :to="{ name : 'Movie',params:{movieId:movieCard.id }}"
      @dblclick="likeMovie"
      :movieCard="movieCard">
        <div class="container card-align">
          <div class="item card-align" style="width: 18rem;">
            <img :src="`https://image.tmdb.org/t/p/original${movieCard.poster_path}`" class="image-size">
          </div>
          <div class="overview">
            <h5>{{ movieCard.title}}</h5>
            <p class="">{{ movieCard.overview}}</p>
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

<style scoped>
.image-size{
  width: 100%;
}
.card-align{
  float: left;
}
img:hover {
  background: #0a0a0a;
  opacity: 50%;
}
img:hover > .oberview{
  opacity: 100%;
}
.overview{
  color: #dddddd;
  visibility: hidden;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  line-height: 1.2;
  width: 230px;
  height:450px;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  position: absolute;
  margin: 20px;
  text-align: center;
}
/* .overview:hover{
  color: #dddddd;
  visibility: visible;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  line-height: 1.2;
  width: 230px;
  height:450px;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  position: absolute;
  margin: 20px;
  text-align: center;
} */
/* .card-body{
  background: rgb(6, 21, 66);
  color: aliceblue;
}

.movie-item .thumb-summary {
    display: block;
    opacity: 0;
    -webkit-transition: visibility 0s linear .2s,opacity .2s,-webkit-transform .2s;
    transition: visibility 0s linear .2s,opacity .2s,-webkit-transform .2s;
    transition: visibility 0s linear .2s,opacity .2s,transform .2s;
    transition: visibility 0s linear .2s,opacity .2s,transform .2s,-webkit-transform .2s;
    -webkit-transform: translateZ(0);
    transform: translateZ(0);
    cursor: pointer;
    background: #2e2e2e;
    position: absolute;
    top: 0;
    left: 0;
    padding: 1.5625rem 0.875rem;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: 100;
}
.movie-item .thumb-summary dl {
    overflow: hidden;
}
.movie-item__image {
    display: block;
    position: relative;
    overflow: hidden;
    background-color: #0a0a0a;
    border-radius: 0.25rem;
    -webkit-transition: box-shadow .4s;
    transition: box-shadow .4s;
}
dl {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
}
section.lists .lists-wrap>* {
    padding-left: 0.5625rem;
    padding-right: 0.5625rem;
    pointer-events: visible;
}
section.lists .lists-wrap {
    position: relative;
    overflow: hidden;
    margin: -30px -0.5625rem 0;
    padding: 1.875rem 0 0;
    pointer-events: none;
}
.movie-item__info {
    padding: 1rem 1.25rem 0 0.25rem;
    font-weight: 400;
    font-size: 0;
}
.movie-item__image.ratio-poster:before {
    padding-top: 144.44%;
}
.movie-item__image:before {
    content: "";
    padding-top: 56.25%;
    float: left;
}
.movie-item__image.ratio-poster:before {
    padding-top: 144.44%;
}
.movie-item__image:after {
    content: "";
    display: block;
    clear: both;
}
.movie-item__image img.image-cover:after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    z-index: 1;
    background-color: #000;
} */
</style>