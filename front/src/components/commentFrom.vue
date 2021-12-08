<template>
  <div>
    <h5>댓글 작성</h5>
    <b-input @keyup.enter="createComment"
    v-model="commentItem.content" placeholder="댓글을 입력해주세요">
    </b-input>
    <b-button class="right" @click="createComment"> 전송 </b-button>
    <br class="enter">
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
        commentItem: this.commentItem,
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