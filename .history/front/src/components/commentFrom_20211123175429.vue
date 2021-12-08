<template>
  <div>
    <h1>댓글 작성</h1>
    <input type="text">
    <button @click="createComment">댓글 작성</button>
  </div>
</template>

<script>
export default {
  name:'commentForm',
  props:{
    review:{
      type: Object,
      required: true
    }
  },
  data(){
    return{
      commentItem:{
        content: null,
      }
    }
  },
  methods:{
    setToken(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization:`JWT ${token}`
      }
      return config
    },
    createComment(){
      let reviewUrl = window.location.href.split("detail/")[1]
      this.reviewUrlNum = reviewUrl

      const commentItemSet = {
        review_id : this.reviewUrl,
        token: this.setToken()
      }
      this.$store.dispatch('createComment',commentItemSet)
      this.commentItem.content = null
    }
  }
}
</script>

<style>

</style>