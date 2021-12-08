<template>
  <div>
    각각 댓글
    댓글 내용 : {{ comment.content }}
    작성자 : {{ comment.user}}
  </div>
</template>

<script>
export default {
  name: 'commentListItem',
  props:{
    comment:{
      type:Object
    }
  }
}
</script>

<style>

</style>