<template>
  <div>

    <!-- <div class="login-page">
      <transition name="fade">
         <div v-if="!registerActive" class="wallpaper-login"></div>
      </transition>
      <div class="wallpaper-register"></div>

      <div class="container">
         <div class="row m-6 p-6">
            <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
               <div v-if="!registerActive" class="card login" v-bind:class="{ error: emptyFields }">
                  <h1>Sign In</h1>
                  <form class="form-group">
                     <input v-model="emailLogin" type="email" class="form-control" placeholder="Email" required>
                     <input v-model="passwordLogin" type="password" class="form-control" placeholder="Password" required>
                     <input type="submit" class="btn btn-primary" @click="doLogin">
                     <p>Don't have an account? <a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign up here</a>
                     </p>
                     <p><a href="#">Forgot your password?</a></p>
                  </form>
               </div>

               <div v-else class="card register" v-bind:class="{ error: emptyFields }">
                  <h1>Sign Up</h1>
                  <form class="form-group">
                     <input v-model="emailReg" type="email" class="form-control" placeholder="Email" required>
                     <input v-model="passwordReg" type="password" class="form-control" placeholder="Password" required>
                     <input v-model="confirmReg" type="password" class="form-control" placeholder="Confirm Password" required>
                     <input type="submit" class="btn btn-primary" @click="doRegister">
                     <p>Already have an account? <a href="#" @click="registerActive = !registerActive, emptyFields = false">Sign in here</a>
                     </p>
                  </form>
               </div>
            </div>
         </div>

      </div>
   </div> -->

    <div class="to-center bg-color">
      <b-card title="로그인" sub-title="Card subtitle">
        <b-card-text>
          Some quick example text to build on the <em>card title</em> and make up the bulk of the card's
          content.
        </b-card-text>

        <b-card-text>A second paragraph of text in the card.</b-card-text>

        <a href="#" class="card-link">Card link</a>
        <b-link href="#" class="card-link">Another link</b-link>
      </b-card>
    </div>


    <h1>로그인</h1>
    <div>
      <label for="username">사용자 이름 : </label>
      <input type="text"
      id="username"
      v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호 : </label>
      <input type="password"
      id="password"
      v-model="credentials.password"
      @keyup.enter="login">
    </div>
    <button @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'Login',
  data: function(){
    return {
      credentials: {
        username: null,
        password: null,
        isLogin: false,
      }
    }
  },
  props:{
    loginState : String,
  },
  methods: {
    login: function(){
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          console.log(this.credentials)
          localStorage.setItem('jwt',res.data.token)
          this.$emit('login')
          this.$emit('is-login',true)
          this.$router.push({ name: 'Home'})
        })
        .catch(err =>{
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
.to-center{
  text-align: center;
}
.bg-color{
  background: rgb(6,5,87);
  background: linear-gradient(180deg, rgba(6,5,87,1) 0%, rgba(43,12,69,1) 100%);
  color: #dddddd;
}
</style>