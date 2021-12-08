<template>
  <div class="back">
    작성자 : {{ comment.user }}
    댓글 내용 : {{ comment.content }}

    <b-button @click="deleteComment" class="right">삭제</b-button>
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
        comment_id: this.comment.id,
        token: this.setToken(),
        active : false,
      }
      this.$store.dispatch('deleteComment', commentItemSet)
    }
  }
}
</script>

<style>
.back{
  background: #999999;
  margin: 2%;
  padding: 2%;
}
.logtemp {
  position: relative;
}

.logtemp.active {
  animation-name: non;
  animation-duration: .2s;
}

@keyframes non {
  0% { left: 0; }
  20% { left: -30px; }
  40% { left: 30px; }
  60% { left: -10px; }
  80% { left: 10px; }
  100% { left: 0; }
}
</style>