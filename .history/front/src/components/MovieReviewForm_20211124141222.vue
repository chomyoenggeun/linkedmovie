<template>
  <div>
    <h1>리뷰 작성 폼</h1>
    <div>
      <label for="title">글 제목 : </label>
      <input type="text"
      id="title"
      v-model="reviewItem.title">
      <br>
      <label for="movie_title">영화 제목 : </label>
      <input type="text"
      id="movie_title"
      v-model="reviewItem.movie_title">
      <br>
      <label for="rank">평점 : </label>
      <input type="text"
      id="rank"
      v-model="reviewItem.rank">
      <br>
      <label for="content">내용 : </label>
      <input type="text"
      id="content"
      v-model="reviewItem.content">
    </div>
    <button @click="createReview">저장</button>
  </div>
</template>

<script>
export default {
  name: 'MovieReviewForm',
  data(){
    return{
      reviewItem:{
        title : null,
        movie_title : null,
        rank : 5,
        content : null,
      },
      dialog: false,
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
    createReview(){
      //여기서 영화랑 id  값 넘기기
      const reviewItemSet = {
        reviewItem: this.reviewItem,
        token:this.setToken()
      }
      this.$store.dispatch('createReviews',reviewItemSet)
      console.log(reviewItemSet)
    }
  },

}
</script>

<style>

</style>