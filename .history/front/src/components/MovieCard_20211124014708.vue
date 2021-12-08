<template>
  <div>
    <section>
      <router-link :to="{ name : 'Movie',params:{movieId:movieCard.id }}"
      @dblclick="likeMovie"
      :movieCard="movieCard">
        <!-- <div class="container">
          <div class="card item front" style="width: 18rem;">
            <img :src="`https://image.tmdb.org/t/p/original${movieCard.poster_path}`">
            <div class="card-body">
              <h5>{{ movieCard.title}}</h5>
              <p class="overview">{{ movieCard.overview}}</p>
            </div>
          </div>
        </div> -->
        

    <div data-min="6" data-max="6" data-margin="18" data-pager="true" data-controls="true" class="bxslider bxslider-in" data-noslide="true" style="width: 24215%; position: relative; transition-duration: 0s; transform: translate3d(0px, 0px, 0px);">
        <div num="false" class="movie-item column-6 " aria-hidden="false" style="float: left; list-style: none; position: relative; width: 185px; margin-right: 18px;">
					<a class="movie-item__image ratio-poster" href="/movie/player/M000364541" data-index="1" data-code="M000364541">			
					<div class="tags"><span class="tag__age tag__age-12">12</span>
            <div class="tags-tl">
              <div>
              </div>
              <div>
              </div>
              </div>
              </div>
							<img alt="장화, 홍련" onerror="onErrorVerticalImage(this)" class="image-cover lazy loaded" data-ll-status="loaded" :src="`https://image.tmdb.org/t/p/original${movieCard.poster_path}`">
							<div class="thumb-summary">
								<dl onclick="/movie/player/M000364541">
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