<template>
  <div>
    <div v-if="movieUrlText == 'http://localhost:8080/review'">
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
    <div v-else>
      <!-- {{ review.movie_title}} -->
      <!-- {{ movieCards}} -->
      <div
      v-for="movieCard in movieCards"
      :key="movieCard.id"
      :movieCard="movieCard">
        <!-- {{ movieCard }} {{review.movie_title}} -->
        <div v-if="movieCard.id == movieUrlNum">
          <div v-if="movieCard.title == review.movie_title">
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
        </div>
      </div>
    </div>

    <div v-if="movieCard.id == movieUrlNum">
      <div v-if="movieCard.title == review.movie_title">
        <router-link :to="{name:'MovieReviewCommunity',params:{ reviewId:review.id }}" >
          <div>
            <td class="table-box">
              <tr class="table-box">
                <p>작성자</p>

                <td class="table-box">
                  <span>글 제목</span>
                </td>
              </tr>
              <tr>
                <td class="table-box">
                  <span>글 내용</span>
                </td>
              </tr>
              <tr>
                <span>랭크</span>
              </tr>
            </td>
          </div>
        </router-link>
      </div>
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
import { mapState } from 'vuex'
export default {
  
  name : 'MovieReviewItem',
  props: {
    review: {
      type: Object,
      required: true
    },
    // movieCard:{
    //   type:Object
    // }
  },
  data(){
    return{
      reviewItem:{
        title: this.review.title,
        movie: this.review.movie_title,
        rank: this.review.rank,
        content: this.review.content
      },
      movieUrlNum : null,
      movieUrlText : null
    }
  },
  // created: function(){
  //   this.$store.dispatch('getLoginUser',this.setToken())
  // },
  created:function(){
    let movieUrl = window.location.href.split("movie/")[1]
    this.movieUrlNum = movieUrl
    let Urlmovie = window.location.href.split('movie/')[0]
    this.movieUrlText = Urlmovie
    console.log(movieUrl)
    console.log(this.review)

    this.$store.dispatch('LoadMovieCards',this.setToken())
  },
  methods:{
    setToken:function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
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
  },
  computed:{
    ...mapState(['movieCards']),
  },
  
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
.table-box{
  border: solid #aa5d66 1px;
}
</style>