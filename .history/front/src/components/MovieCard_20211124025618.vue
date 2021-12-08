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
        
      <!-- <div class="lists-wrap" id="movieList" style="padding-top: 30px">
        <div data-min="6" data-max="6" data-margin="18" data-pager="true" data-controls="true" class="bxslider bxslider-in" data-noslide="true" style="width: 24215%; position: relative; transition-duration: 0s; transform: translate3d(0px, 0px, 0px);">
          <div num="false" class="movie-item column-6 " aria-hidden="false" style="float: left; list-style: none; position: relative; width: 185px; margin-right: 18px;">
            <a class="movie-item__image ratio-poster" href="/movie/player/M000364541" data-index="1" data-code="M000364541">			
            <div class="tags">
              <div class="tags-tl">
                <div>
                </div>
                <div>
                </div>
              </div>
            </div>
            <img alt="장화, 홍련" onerror="onErrorVerticalImage(this)" class="image-cover lazy loaded" data-ll-status="loaded" :src="`https://image.tmdb.org/t/p/original${movieCard.poster_path}`">
            <div class="thumb-summary">
              <dl>
                <dt>
                  장화, 홍련
                  <span>스릴러</span>
                </dt>
                <dd>
                  <ul>
                    <li><strong>감독</strong>김지운</li>
                    <li><strong>배우</strong>임수정,염정아,김갑수,문근영</li>
                  </ul>
                  <p>인적이 드문 시골, 이름 모를 들꽃들이 소담하게 피어 있는 신작로 끝에  ···</p>
                </dd>
              </dl>
            </div>
            </a>
            <div class="movie-item__info">
          
              <a href="/movie/player/M000364541" class="movie-item__info-title" data-index="1" data-code="M000364541">
                장화, 홍련
              </a>
            </div>
          </div>	
        </div>
      </div> -->


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
.image-size{
  width: 100%;
}
.card-align{
  float: left;
}
img :hover{
  background: #0a0a0a;
}
.overview{
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
  /* position: absolute; */
  margin: auto;
}
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