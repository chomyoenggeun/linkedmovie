<template>
  <div>
    <h1>영화 리뷰 리스트</h1>
    <router-link to="/movie/review/create">작성하기</router-link>
    <dmovie-review-item
    v-for="(moviereview, idx) in moviereviews"
    :key="idx"
    :moviereview="moviereview"></dmovie-review-item>
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
      'moviereviews'
    ])
  },
  created(){
    console.log(localStorage.getItem('jwt'))
    this.$store.dispatch('getMovieReviews',this.setToken())
  }
}
</script>

<style>

</style>