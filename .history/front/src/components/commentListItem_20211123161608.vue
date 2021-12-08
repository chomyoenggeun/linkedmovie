<template>
  <div>
    각각 댓글
    댓글 내용 : {{ comment }}
  </div>
</template>

<script>
export default {
  name: 'commentListItem',
  props:{
    comment
  }
}
</script>

<style>

</style>