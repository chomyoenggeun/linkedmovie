<template>
  <div>
    <div class="to-center container text-status">
      <h1>Linked Movie에 오신걸 환영합니다</h1>
      <div title="로그인" sub-title="linked-Movie에 오신걸 환영합니다">
        <div class="custom">
          <div>
            <br>
            <b-form-input class="login-input-box" type="text" placeholder="사용자 이름"
            id="username"
            v-model="credentials.username"></b-form-input>
          </div>
          <br>
          <div>
            <b-form-input type="password" class="login-input-box"
            id="password" placeholder="비밀번호"
            v-model="credentials.password"
            @keyup.enter="login"></b-form-input>
          </div>
          <br>
          <div>
            <b-form-input type="password" class="login-input-box"
            id="password" placeholder="비밀번호 확인"
            v-model="credentials.passwordConfirmation"
            @keyup.enter="signup"></b-form-input>
          </div>
        </div>
        <br>
        <b-button @click="signup">확인</b-button>

        <b-card-text>
          이미 아이디가 있어요!
          <br>
          <router-link to="/account/login">Login</router-link>
        </b-card-text>
        
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function(){
    return {
      credentials:{
        username: null,
        password: null,
        passwordConfirmation: null,
      },
    }
  },
  methods: {
        signup: function(){
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/accounts/signup/',
            data: this.credentials
          })
            .then(() =>{
              this.$router.push({ name: 'Login' })
            })
            .catch(err => {
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
</style>