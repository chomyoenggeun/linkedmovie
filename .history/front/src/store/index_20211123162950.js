import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieCards: [],
    carosalCards : [],
    loginState : false,
    loginjwt : null,
    reviews: [],
    user : null,
    comments : [],
  },
  mutations: {
    // GET_LOGIN_USER: function(state,res){
    //   state.user = res

    // },
    LOAD_MOVIE_CARDS:function(state, results){
      state.movieCards = results
    },
    GET_REVIEWS:function(state, res){
      state.reviews = res
      // console.log(state.reviews)
    },
    CREATE_REVIEWS : function(state, res){
      state.reviews.push(res)
      // console.log(state.reviews)
    },
    UPDATE_REVIEW : function(state,reviewItem){
      state.reviews = state.reviews.map((review) => {
        if (review === reviewItem){
          return { ...review,
            title: reviewItem.titie,
            content: reviewItem.content,
            rank: reviewItem.rank
          }
        }
        return review
      })
    },
    DELETE_REVIEW : function(state, reviewItem){
      const index = state.reviews.indexOf(reviewItem)
      state.reviews.splice(index,1)
    },
    GET_COMMENTS : function(state,res){
      state.comments = res
    },
  },
  actions: {
    // getLoginUser: function({commit},token){
    //   axios({
    //     method: 'get',
    //     url:'http://123.0.01:8000/account/api-token-auth/',
    //     headers: token,
    //   })
    //     .then(res =>{
    //       console.log(res)
    //       commit('GET_LOGIN_USER')
    //     })
    // },
    // 로그인 정보 보내기
    // Login: function(context){
    //   axios({
    //     method: 'post',
    //     url: 'http://127.0.0.1:8000/accounts/signup/',
    //     data: this.credentials
    //   })
    //     .then(()=>{
    //       console.log(context)
    //       context.commit('LOGIN',context)
    //       this.$router.push({name: 'Login'})
    //     })
    //     .catch(err =>{
    //       console.log(err)
    //     })
    // },
    // 영화 불러오기
    LoadMovieCards: function({commit},token){
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
        headers: token,
      })
        .then(res => {
          console.log(res.data)
          commit('LOAD_MOVIE_CARDS',res.data)
        })
    },
    // LikeMovie:function({commit},token){
    //   //좋아요 표시
    //   Pass
    // },
    getReviews: function({commit},token){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/`,
        headers: token,
      })
        .then(res => {
          // console.log(res.data)
          commit('GET_REVIEWS',res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    createReviews: function({commit},object){
      axios({
        method: 'post',
        url:'http://127.0.0.1:8000/community/',
        headers: object.token,
        data: object.reviewItem,
      })
        .then(res => {
          console.log(res)
          commit('CREATE_REVIEWS')
          router.push({ name:'MovieReviewItem' })
          router.go()
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateReview: function({commit},object){
      axios({
        method: 'PUT',
        url:`http://127.0.0.1:8000/community/${object.review_id}/`,
        data:object.reviewItem,
        headers: object.token
      })
        .then(() => {
          commit('UPDATE_REVIEW')
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteReview({commit},object){
      axios({
        method: 'DELETE',
        url:`http://127.0.0.1:8000/community/${object.review_id}/`,
        headers: object.token,
        
      })
        .then(res=>{
          console.log(res)
          commit('DELETE_REVIEW')
        })
        .catch(err =>{
          console.log(err)
        })
    },
    getComments({commit},object){
      axios({
        method: 'GET',
        url:`http://127.0.0.1:8000/community/${object.review_id}/comments/`,
        headers: object.token,
      })    
        .then((res) => {
          console.log(object.review_id)
          console.log(res)
          commit('GET_COMMENTS',res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteComment({commit},object){
      axios({
        method:'DELETE',
        url: `http://127.0.0.1:8000/community/comments/${object.comment_id}/`
      })
    }
  },
  
  modules: {
  }
})