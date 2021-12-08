<template>
  <div>
    <router-link :to="{name:'MovieReviewCommunity',params:{ reviewId:moviereview.id }}" >
      
      <div v-if="movievreview.movie_pk === ">
        영화 작성 글 : {{ moviereview.content }}
        <br>
        영화 제목 : {{ moviereview.movie_title }}
        <br>
        랭크 : {{ moviereview.rank }}
        <br>
        내용 : {{ moviereview.title }}
        <br>
        작성유저 : {{ moviereview.user }}
        
      </div>
    </router-link>    
      
        <!-- <span v-if="user === review.user">
        </span> -->
          <!-- <button @click="updateReview">
            <v-expansion-panel-header>
              수정
            </v-expansion-panel-header>
          </button> -->
          <button @click="deleteReview">
            삭제
          </button>
      
    <br>
  </div>
</template>

<script>
export default {
  name : 'DmovieReviewItem',
  props: {
    moviereview: {
      type: Object,
      required: true
    }
  },
  data(){
    return{
      reviewItem:{
        title: this.moviereview.title,
        movie: this.moviereview.movie_title,
        rank: this.moviereview.rank,
        content: this.moviereview.content
      },
    }
  },
  // created: function(){
  //   this.$store.dispatch('getLoginUser',this.setToken())
  // },
  methods:{
    setToken(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    updateReview(){
      const reviewItemSet = {
        reviewItem : this.reviewItem,
        review_id : this.moviereview.id,
        token: this.setToken()
      }
      console.log(reviewItemSet)
      this.$store.dispatch('updateReview',reviewItemSet)
    },
    deleteReview(){
      const reviewItemSet = {
        review_id : this.moviereview.id,
        token: this.setToken()
      }
      
      this.$store.dispatch('deleteReview',reviewItemSet)
    }
  },
  created(){
    console.log(this.moviereview)
    let movieUrl = window.location.href.split("movie/")[1]
    this.movieUrlNum = movieUrl
  }
}
</script>

<style>

</style>