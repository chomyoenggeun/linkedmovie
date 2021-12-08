<template>
  <div class="container card">
    

    <div class="container">
      <div
      v-for="(review, idx) in reviews"
      :key="idx">
        <div v-if="review.id==reviewUrlNum">
          <div>
            <div class="left">
              <h1>{{ review.content }}</h1>
              <div v-if="likes.liked == false">
                <div class="like-box" @click="likeReview">
                  <img class="size" :src="require('@/assets/heart_non.png')" alt="">
                </div>
              </div>
              <div v-if="likes.liked == true">
                <div class="like-box" @click="likeReview">
                  <img class="size" :src="require('@/assets/heart.png')" alt="">
                </div>
              </div>
            </div>
            <div class="right">
              {{ review.user }}g
              <p>작성일자 {{ review.created_at}}</p>
              <p>최종 수정일자 {{ review.updated_at}}</p>
            </div>
            <br class="enter">
            <div class="left">
              영화 제목 : {{ review.movie_title }}
            </div>
            <div class="right">
              랭크 : {{ review.rank }}
            </div>
            <br class="enter">
            <div class="card">
              내용 : {{ review.title }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <br>
    <div>
      <comment-from></comment-from>
      <comment-list></comment-list>
    </div>
  </div>
</template>

<script>
import commentList from '@/components/commentList.vue'
import commentFrom from '@/components/commentFrom.vue'

export default {
  name:'MovieReviewCommunity',
  components:{
    commentList,
    commentFrom
  },

  data:function(){
    return{
      reviewUrlNum : null,
    }
  },
  created(){
    console.log(localStorage.getItem('jwt'))
    this.$store.dispatch('getReviews',this.setToken())

    let reviewUrl = window.location.href.split("detail/")[1]
    this.reviewUrlNum = reviewUrl

    this.$store.dispatch('likeReview',likeReviewSet)
    const likeReviewSet = {
        review_id : this.reviewUrlNum,
        token: this.setToken()
      }
  },
  methods :{
    setToken : function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    likeReview : function(){
      const likeReviewSet = {
        review_id : this.reviewUrlNum,
        token: this.setToken()
      }
      this.$store.dispatch('likeReview',likeReviewSet)
    },
  },
  computed:{
    likes: function(){
      return this.$store.state.likes
    },
    reviews: function(){
      return this.$store.state.reviews
    }
  },
  updateReview: function(){
      const reviewItemSet = {
        reviewItem : this.reviewItem,
        review_id : this.review.id,
        token: this.setToken()
      }
      console.log(reviewItemSet)
      this.$store.dispatch('updateReview',reviewItemSet)
    },
    deleteReview : function(){
      const reviewItemSet = {
        review_id : this.review.id,
        token: this.setToken()
      }
      this.$store.dispatch('deleteReview',reviewItemSet)
    },
}
</script>

<style scpoed>
.enter{
  clear: both;
}
.left{
  float: left;
}
.right{
  float: right;
  text-align: right;
}
</style>