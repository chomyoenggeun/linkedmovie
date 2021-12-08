<template>
  <div>
    <h1>리뷰 자세히 보기</h1>
    <div>
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
</template>

<script>
import { mapState } from 'vuex'
export default {
  name:'MovieReviewCommunity',
  computed:{
    ...mapState([
      'reviews'
    ])
  },
  created(){
    console.log(localStorage.getItem('jwt'))
    this.$store.dispatch('getReviews',this.setToken())
  }
}
</script>

<style>

</style>