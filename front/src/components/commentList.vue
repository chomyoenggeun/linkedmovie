<template>
  <div>
    <p>{{ comments.length }} 개의 댓글이 있어요!</p>
    <div>
      <comment-list-item
      v-for="(comment,idx) in comments"
      :key="idx"
      :comment="comment"></comment-list-item>
    </div>
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
  data:function(){
    return{
      reviewUrlNum : null,
    }
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
    let reviewUrl = window.location.href.split("detail/")[1]
    this.reviewUrlNum = reviewUrl

    const commentListSet = {
        review_id : reviewUrl,
        token: this.setToken()
      }

    this.$store.dispatch('getComments',commentListSet)
  }
}
</script>

<style>

</style>