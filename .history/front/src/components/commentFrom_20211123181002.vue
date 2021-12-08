<template>
  <div>
    <h1>댓글 작성</h1>

    <label for="content">댓글 작성 : </label>
    <input type="text"
    id="content"
    v-model="commentItem.content">
    <button @click="createComment">댓글 작성</button>
  </div>
</template>

<script>
export default {
  name:'commentForm',
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
        review_id : reviewUrl,
        token: this.setToken()
      }
      this.$store.dispatch('createComment',commentItemSet)
      // this.commentItem.content = null
    }
  }
}
</script>

<style>

</style>