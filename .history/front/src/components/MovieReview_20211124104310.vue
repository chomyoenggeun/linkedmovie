<template>
  <div>
    <h1>리뷰 리스트</h1>
    <movie-review-item
    v-for="(review, idx) in reviews"
    :key="idx"
    :review="review"></movie-review-item>
    <router-link to="/review/create">작성하기</router-link>
  </div>
</template>

<script>
import MovieReviewItem from '@/components/MovieReviewItem.vue'
import { mapState } from 'vuex'

export default {
  name : 'MovieReview',
  components: {
    MovieReviewItem,
  },
  methods:{
    setToken(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
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