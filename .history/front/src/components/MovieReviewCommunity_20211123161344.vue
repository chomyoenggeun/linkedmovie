<template>
  <div>
    <h1>리뷰 자세히 보기</h1>
    <div
    v-for="(review, idx) in reviews"
    :key="idx">
      <div v-if="review.id==reviewUrlNum">
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
        </div>
      </div>
    </div>

    <div>
      <commentList
      v-for="(review, idx) in reviews"
      :key="idx"
      :review="review"></commentList>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import commentList from '@/components/commentList.vue'

export default {
  name:'MovieReviewCommunity',
  components:{
    commentList
  },
  computed:{
    ...mapState([
      'reviews'
    ])
  },
  data:function(){
    return{
      reviewUrlNum : null,
      // revieItem : {
      //   movie_title : this.review.movie_title,
      //   title: this.review.title,
      //   content: this.review.content,
      //   rank : this.review.rank
      // }
    }
  },
  created(){
    console.log(localStorage.getItem('jwt'))
    this.$store.dispatch('getReviews',this.setToken())

    let reviewUrl = window.location.href.split("detail/")[1]
    this.reviewUrlNum = reviewUrl
  },
  methods :{
    setToken : function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
}
</script>

<style>

</style>