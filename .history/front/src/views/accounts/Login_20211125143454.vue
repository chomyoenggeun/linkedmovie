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

    <div class="to-center container text-status logtemp" :class="{ active : Active }">
      <h1>로그인</h1>
      <div title="로그인" sub-title="linked-Movie에 오신걸 환영합니다">
        <div class="custom">
          <div>
            <br>
            <b-input class="login-input-box" type="text" placeholder="사용자 이름"
            id="username"
            v-model="credentials.username"></b-input>
            <!-- <input type="text" placeholder="사용자 이름"
            id="username"
            v-model="credentials.username"> -->
          </div>
          <br>
          <div>
            <b-input type="password" class="login-input-box"
            id="password" placeholder="비밀번호"
            v-model="credentials.password"
            @keyup.enter="login"></b-input>
          </div>
        </div>
        <br>
        <b-button @click="login">확인</b-button>

        <b-card-text>
          ID가 없으신가요?
          <br>
          <router-link to="/account/signup">Signup</router-link>
        </b-card-text>
        
      </div>
    </div>
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
      },
      Active : false
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
          this.Active = true;
          setTimeout(()=>{
            this.Active = false;
          },200)
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
  color: #111111;
  padding: auto
}
.login-input-box{
  width: 270px;
}
.text-status{
  color: #dddddd;
}
.custom{
  /* margin-left: 35%; */
  position: relative;
  top: 50%;
  left: 40%;
}

.logtemp {
  position: relative;
  animation-name: non;
  animation-duration: .2s;
}

@keyframes non {
  0% { left: 0; }
  30% { left: -5px; }
  68%, 72% { left: 5px; }
  68%, 72% { left: -3px; }
  68%, 72% { left: 3px; }
  100% { left: 0; }
}
</style>