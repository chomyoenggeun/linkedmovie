<template>
  <div>
    <h2>댓글</h2>
    <comment-list-item
    v-for="(comment,idx) in comments"
    :key="idx"
    :comment="comment"></comment-list-item>
  </div>
</template>

<script>
import commentListItem from '@/components/commentListItem.vue'
import { mapState } from 'vuex'

export default {
  name:'commentList',
  components:{
    commentListItem
  },
  prop:{
    review:{
      type:Object,
      required:true
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
  },
  computed:{
    ...mapState([
      'comments'
    ])
  },
  created(){
    const commentListSet = {
        review_id : this.review.id,
        token: this.setToken()
      }
    this.$store.dispatch('getComments',commentListSet)
  }
}
</script>

<style>

</style>