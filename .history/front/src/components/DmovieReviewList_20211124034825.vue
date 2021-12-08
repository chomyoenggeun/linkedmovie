<template>
  <div>
    <h1>영화 리뷰 리스트</h1>
    <dmovie-review-item
    v-for="(review, idx) in reviews"
    :key="idx"
    :review="review"></dmovie-review-item>
    <router-link to="/review/create">작성하기</router-link>
  </div>
</template>

<script>
import DmovieReviewItem from '@/components/DmovieReviewItem.vue'
import { mapState } from 'vuex'

export default {
  name : 'DmovieReviewList',
  components: {
    DmovieReviewItem,
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