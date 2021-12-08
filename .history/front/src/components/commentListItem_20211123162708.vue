<template>
  <div>
    각각 댓글
    댓글 내용 : {{ comment.content }}
    작성자 : {{ comment.user}}

    <button @click="deleteComment">삭제</button>
  </div>
</template>

<script>
export default {
  name: 'commentListItem',
  props:{
    comment:{
      type:Object
    }
  },
  methods :{
    setToken(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization:`JWT ${token}`
      }
      return config
    },
    deleteComment(){
      const commentItemSet = {
        commnetItem: this.commnetItem,
        comment_id: this.comment.id,
        token: this.setToken()
      }
      this.$store.dispatch('updateComment', commentItemSet)
    }
  }
}
</script>

<style>

</style>