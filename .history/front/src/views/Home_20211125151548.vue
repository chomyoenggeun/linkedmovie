<template>
  <div>
    <div>
    <div>
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls

        indicators
        background="#ababab"
        img-width="1024"
        img-height="480"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <!-- Text slides with image -->
        <!-- <b-carousel-slide
          caption="First slide"
          text="Nulla vitae elit libero, a pharetra augue mollis interdum."
          img-src="https://picsum.photos/1024/480/?image=55"
        ></b-carousel-slide> -->

        <!-- Slides with custom text -->
        <b-carousel-slide class="slide-image" img-src="https://www.themoviedb.org/t/p/original/cinER0ESG0eJ49kXlExM0MEWGxW.jpg">
          <h1>샹치와 텐 링즈의 전설</h1>
        </b-carousel-slide>
        <b-carousel-slide class="slide-image" img-src="https://www.themoviedb.org/t/p/original/dK12GIdhGP6NPGFssK2Fh265jyr.jpg">
          <h1>레드 노티스</h1>
        </b-carousel-slide>
        <b-carousel-slide class="slide-image" img-src="https://www.themoviedb.org/t/p/original/70nxSw3mFBsGmtkvcs91PbjerwD.jpg">
          <h1>007 노 타임 투 다이</h1>
        </b-carousel-slide>

        <!-- Slides with img slot -->
        <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
        <!-- <b-carousel-slide>
          <template #img>
            <div>
              <img
                class="d-block img-fluid w-100"
                width="1024"
                height="480"
                :src="`https://image.tmdb.org/t/p/original${movieCard.backdrop_path}`"
                alt="image slot"
              >
            </div>
          </template>
        </b-carousel-slide> -->

        <!-- Slide with blank fluid image to maintain slide aspect ratio -->
        <!-- <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt
            a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
          </p>
        </b-carousel-slide> -->
      </b-carousel>

      <!-- <p class="mt-4">
        Slide #: {{ slide }}<br>
        Sliding: {{ sliding }}
      </p> -->
    </div>
    <div>
      <h2> 장르별 무비 </h2>
      <div>
        <div>
          <b-button @click="random">random movie</b-button>
          <div v-for="randomMovieItem in randomMovie"
          :key="randomMovieItem">
            <img :src="`https://image.tmdb.org/t/p/original${randomMovieItem.poster_path}`" class="image-size">
          </div>
        </div>
      </div>
    </div>
    </div>
    <section>
      <h2> 전체 무비 </h2>
      <div class="justify-center card-align row row-cols-4">
        <movie-card
        v-for="movieCard in movieCards"
        :key="movieCard.id"
        :movieCard="movieCard"></movie-card>
      </div>
    </section>
  </div>
</template>

<script>

import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  data(){
    return{
      slide : 0,
      sliding : null
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
    onSlideStart(){
      this.sliding = true
    },
    onSlideEnd(){
      this.sliding = false
    },
    random : function(){
      this.$store.dispatch('random',this.setToken())
    }
  },
  created: function(){
    this.$store.dispatch('LoadMovieCards',this.setToken())
  },
  computed:{
    movieCards: function(){
      return this.$store.state.movieCards
    },
    randomMovie: function(){
      return this.$store.state.randomMovie
    }
  }
}

</script>

<style>
  /* .menubt{
  padding : 20px;
  background: #255ca3;
  list-style:none;
} */
.slide-image{
  max-height: 500px;
}
.card-align{
  display: inline-block;
}
</style>