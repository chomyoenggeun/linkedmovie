import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import _ from 'lodash'

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
    moviereviews: [],
    genreData: [],
    likes : [],
    randomMovie : [],
    active: false
  },
  mutations: {
    FAIL: function(state, res){
      state.active = res
      console.log(active)
    },
    GET_USER_DATA : function(state,res){
      state.user = res
    },
    LOAD_MOVIE_CARDS:function(state, results){
      state.movieCards = results
    },
    LOAD_GENRE_DATA : function(state,results){
      state.genreData = results
    },
    RANDOM_PICK : function(state,results){
      state.randomMovie = results
    },
    // GET_MOVIE_DATA:function(state, results){
    //   state.
    // },
    GET_REVIEWS:function(state, res){
      state.reviews = res
      // console.log(state.reviews)
    },
    GET_MOVIE_REVIEWS : function(state,res){
      state.moviereviews = res
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
    LIKE_REVIEW : function(state,res){
      state.likes = res
      console.log(res)
    },
    GET_COMMENTS : function(state,res){
      state.comments = res
    },
    CREATE_COMMENT : function(state, res){
      state.comments.push(res)
    },
    DELETE_COMMENT : function(state,commentItem){
      const index = state.comments.indexOf(commentItem)
      state.comments.splice(index, 1)
    }
  },
  actions: {
    // accounts 정보
    getUserData : function({commit},token){
      axios({
        method: 'get',
        url:'http://127.0.0.1:8000/accounts/',
        headers: token,
      })
        .then(res =>{
          commit('GET_USER_DATA',res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 영화 불러오기
    LoadMovieCards: function({commit},token){
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
        headers: token,
      })
        .then(res => {
          // console.log(res.data)
          commit('LOAD_MOVIE_CARDS',res.data)
        })
    },
    LoadGenreData : function({commit},token){
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/movies/genre/`,
        headers: token,
      })
        .then(res =>{
          console.log(res.data)
          commit('LOAD_GENRE_DATA',res.data)
        })
    },
    random : function({commit},token){
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/movies/genre/`,
        headers: token,
      })
        .then(res => {
          console.log(res.data)
          const randomGenre = _.sample(res.data,1)
          commit('RANDOM_PICK',randomGenre)
        })
      // axios({
      //   method: 'get',
      //   url: 'http://127.0.0.1:8000/movies/',
      //   headers: token,
      // })
      //   .then(res => {
      //     console.log(res.data)
      //     const randomMovie = _.sampleSize(res.data,5)
      //     commit('RANDOM_PICK',randomMovie)
      //   })
        .catch(err =>{
          console.log(err)
        })
    },
    likeMovie:function({commit},object){
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/movies/${object.review_id}/`,
        headers: object.token,
        data: object.review_id
      })
        .then(res =>{
          console.log(res)
          commit('LIKE_MOVIE',res.data)
        })
    },
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
        .then(() => {
          // console.log(res)
          commit('CREATE_REVIEWS')
          router.push({ name:'Review' })
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
        .then(()=>{
          // console.log(res)
          commit('DELETE_REVIEW')
        })
        .catch(err =>{
          console.log(err)
          object.Active = true
          setTimeout(()=>{
            object.Active =false
          },200)
          commit('FAIL',object.Active)
        })
    },
    likeReview({commit},object){
      axios({
        method:'POST',
        url:`http://127.0.0.1:8000/community/${object.review_id}/likes/`,
        headers:object.token
      })
        .then((res)=>{
          console.log(object.review_id)
          console.log(res.data)
          commit('LIKE_REVIEW',res.data)
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
          // console.log(object.review_id)
          // console.log(res)
          commit('GET_COMMENTS',res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    createComment({commit},object){
      axios({
        method: 'POST',
        url:`http://127.0.0.1:8000/community/${object.review_id}/comments/`,
        data: object.commentItem,
        headers: object.token,
      })
        .then((res) =>{
          commit('CREATE_COMMENT', res.data)
        })
        .catch(err =>{
          console.log(err)
        })
    },
    deleteComment({commit},object){
      axios({
        method:'DELETE',
        url: `http://127.0.0.1:8000/community/comments/${object.comment_id}/`,
        headers: object.token
      })
        .then((res)=>{
          console.log(res)
          commit('DELETE_COMMENT',res.data)
          router.go()
        })
        .catch(err =>{
          console.log(err)
        })
    },
    getMovieData({commit},token){
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
        headers: token,
      })
        .then(res => {
          console.log(res.data)
          commit('GET_MOVIE_DATA',res.data)
        })
    },
    // getMovieReviews({commit},token){
    //   axios({
    //     method: 'GET',
    //     url:`http://127.0.0.1:8000/movies/moviereviews/`,
    //     headers: token,
    //   })    
    //     .then((res) => {
    //       // console.log(object.review_id)
    //       console.log(res)
    //       commit('GET_MOVIE_REVIEWS',res.data)
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // }
  },
  
  modules: {
  }
})