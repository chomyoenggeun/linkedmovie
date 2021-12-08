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
          <div class="item back">
            <p>왜 안나오지</p>
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
    likeMovie:function(){
      this.$store.dispatch('LikeMovie',this.setToken())
    }
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
/* .flip-card {
  background-color: transparent;
  width: 100%;
  height: 200px;
  border: 1px solid #f1f1f1;
  perspective: 1000px;
  margin: auto;
} */

/* This container is needed to position the front and back side */
/* .flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
} */

/* Do an horizontal flip when you move the mouse over the flip box container */
/* .flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
} */

/* Position the front and back side */
/* .flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
} */

/* Style the front side (fallback if image is missing) */
/* .flip-card-front {
  background-color: #bbb;
  color: black;
} */

/* Style the back side */
/* .flip-card-back {
  background-color: dodgerblue;
  color: white;
  transform: rotateY(180deg);
} */
.container{
  width:150px;
  height: 200px;
  perspective: 300px;
  margin-bottom: 500px;
}
.container .item{
  width:150px;
  height: 200px;
  backface-visibility: hidden;
  transition: 1s;
}
.container .item.front{
  position: absolute;
  transform: rotateY(0deg);
}
.container:hover .item.front{
  transform: rotateY(180deg);
}
.container .item.back{
  transform: rotateY(-180deg);
}

</style>