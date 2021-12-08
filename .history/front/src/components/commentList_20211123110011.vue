<template>
  <div>
    <h2>댓글</h2>
    <comment-list-item></comment-list-item>
  </div>
</template>

<script>
import commentListItem from '@/components/commentListItem.vue'
export default {
  name:'commentList',
  components:{
    commentListItem
  },
  methods:{
    setToken(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization:`JWT ${token}`
      }
      return config
    },
  },
  computed:{
    ...mapGetters([
      'comments'
    ])
  },
  created(){
    const commentListSet = {
      review_id:this.review.id,
      token: this.setToken()
    }
    this.$store.dispatch('getComments',commentListSet)
  }
}
</script>

<style>

</style>