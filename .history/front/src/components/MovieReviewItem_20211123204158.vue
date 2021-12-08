<template>
  <div>
    <router-link :to="{name:'MovieReviewCommunity',params:{ reviewId:review.id }}" >
      
      <div>
        영화 작성 글 : {{ review.content }}
        <br>
        영화 제목 : {{ review.movie_title }}
        <br>
        랭크 : {{ review.rank }}
        <br>
        내용 : {{ review.title }}
        <br>
        작성유저 : {{ review.user }}
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
      </div>
  </div>
</template>

<script>
export default {
  name : 'MovieReviewItem',
  props: {
    review: {
      type: Object,
      required: true
    }
  },
  data(){
    return{
      reviewItem:{
        title: this.review.title,
        movie: this.review.movie_title,
        rank: this.review.rank,
        content: this.review.content
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
        review_id : this.review.id,
        token: this.setToken()
      }
      console.log(reviewItemSet)
      this.$store.dispatch('updateReview',reviewItemSet)
    },
    deleteReview(){
      const reviewItemSet = {
        review_id : this.review.id,
        token: this.setToken()
      }
      
      this.$store.dispatch('deleteReview',reviewItemSet)
    }
  },
  created(){
    console.log(this.review)
  }
}
</script>

<style>

</style>