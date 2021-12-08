<template>
  <div>
    <div>
      {{ review.movie_title }}
      <router-link :to="{name:'MovieReviewCommunity',params:{ reviewId:review.id }}" >
        <div class="container">
          <div class="box">
            <div class="user-box">
              {{ review.user }}
            </div>
            <div class="section-box">
              <div class="title-box">
                {{ review.title }}
              </div>
              <div class="content-box">
                영화 작성 글 : {{ review.content }}
              </div>
            </div>
            <div class="rank-box">
              랭크 : {{ review.rank }}
            </div>
          </div>
        </div>
        <div class="box"></div>
      </router-link>    
    </div>
      
        <!-- <span v-if="user === review.user">
        </span> -->
          <!-- <button @click="updateReview">
            <v-expansion-panel-header>
              수정
            </v-expansion-panel-header>
          </button> -->
          <!-- <button @click="deleteReview">
            삭제
          </button> -->
      
    <br>
  </div>
</template>

<script>
export default {
  name : 'MovieReviewItem',
  props: {
    review: {
      type: Object,
      required: true
    },
    movieCard:{
      type:Object
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
.box{
  clear: both;
  color: #dddddd;
  text-decoration: none;
  /* border: blue solid 1px; */
  padding: 10px;
}
.box:hover{
  /* background-color: aqua; */
}
.user-box{
  float: left;
  padding: 10px;
}
.section-box{
  float: left;
}
.title-box{
  padding:10px;
}
.content-box{
  padding: 10px;
}
.rank-box{
  float: right;
}
</style>