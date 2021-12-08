<template>
  <div>
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

<style>

</style>