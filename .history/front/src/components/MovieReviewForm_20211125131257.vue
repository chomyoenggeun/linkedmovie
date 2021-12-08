<template>
  <div>
    <div class="to-center container text-status">
      <h1>리뷰 작성</h1>
      <div>
        <div class="custom">
          <div>
            <br>
            <b-input class="login-input-box" type="text" placeholder="게시글 제목"
            id="title"
            v-model="reviewItem.title"></b-input>
          </div>
          <br>
          <div>
            <b-input type="text" class="login-input-box"
            id="movie_title" placeholder="영화이름"
            v-model="reviewItem.movie_title"></b-input>
          </div>
          <br>
          <div>
            <div>
              <b-form-rating v-model="reviewItem.rank"></b-form-rating>
            </div>
          </div>
          <br>
          <div>
            <b-form-textarea
              id="textarea"
              v-model="reviewItem.content"
              placeholder="게시글 작성 o(^-^)o"
              rows="3"
              max-rows="6"
            ></b-form-textarea>

            <pre class="mt-3 mb-0">{{ text }}</pre>
          </div>
        </div>
        <br>
        <b-button @click="createReview">확인</b-button>
        
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieReviewForm',
  data(){
    return{
      reviewItem:{
        title : null,
        movie_title : null,
        rank : 3,
        content : null,
      },
      dialog: false,
    }
  },
  methods:{
    setToken : function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createReview(){
      //여기서 영화랑 id  값 넘기기
      const reviewItemSet = {
        reviewItem: this.reviewItem,
        token:this.setToken()
      }
      this.$store.dispatch('createReviews',reviewItemSet)
      // console.log(reviewItemSet)
    }
  },

}
</script>

<style>
.to-center{
  text-align: center;
}
.bg-color{
  background: rgb(6,5,87);
  background: linear-gradient(180deg, rgba(6,5,87,1) 0%, rgba(43,12,69,1) 100%);
  color: #111111;
  padding: auto
}
.login-input-box{
  width: 400px;
}
.text-status{
  color: #dddddd;
}
.custom{
  /* margin-left: 35%; */
  position: relative;
  top: 50%;
}
</style>