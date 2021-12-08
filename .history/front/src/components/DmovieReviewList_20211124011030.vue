<template>
  <div>
    <h1>무비 디테일 리스트</h1>
    <!-- {{ movieUrlNum }} -->
    <dmovie-review-list></dmovie-review-list>
  </div>
</template>

<script>
import DmovieReviewItem from '@/components/MovieDetailReview/DmovieReviewItem.vue'
export default {
  name : 'DmovieReviewList',
  compoents:{
    DmovieReviewItem
  },
  props:{
    movieUrlNum : String
  }
}
</script>

<style>

</style>