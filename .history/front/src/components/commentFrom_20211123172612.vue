<template>
  <div>
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
      const commentItemSet = {
        review_id : this.review.id,
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