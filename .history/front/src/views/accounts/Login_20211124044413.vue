<template>
  <div>
    <template>
  <v-container>
    <v-layout
      text-center
      wrap
    >
      <v-flex xs12>
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        ></v-img>
      </v-flex>

      <v-flex mb-4>
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to Vuetify
        </h1>
        <p class="subheading font-weight-regular">
          For help and collaboration with other Vuetify developers,
          <br>please join our online
          <a href="https://community.vuetifyjs.com" target="_blank">Discord Community</a>
        </p>
      </v-flex>

      <v-flex
        mb-5
        xs12
      >
        <h2 class="headline font-weight-bold mb-3">What's next?</h2>

        <v-layout justify-center>
          <a
            v-for="(next, i) in whatsNext"
            :key="i"
            :href="next.href"
            class="subheading mx-3"
            target="_blank"
          >
            {{ next.text }}
          </a>
        </v-layout>
      </v-flex>

      <v-flex
        xs12
        mb-5
      >
        <h2 class="headline font-weight-bold mb-3">Important Links</h2>

        <v-layout justify-center>
          <a
            v-for="(link, i) in importantLinks"
            :key="i"
            :href="link.href"
            class="subheading mx-3"
            target="_blank"
          >
            {{ link.text }}
          </a>
        </v-layout>
      </v-flex>

      <v-flex
        xs12
        mb-5
      >
        <h2 class="headline font-weight-bold mb-3">Ecosystem</h2>

        <v-layout justify-center>
          <a
            v-for="(eco, i) in ecosystem"
            :key="i"
            :href="eco.href"
            class="subheading mx-3"
            target="_blank"
          >
            {{ eco.text }}
          </a>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>
    <div class="login-page">
      <transition name="fade">
         <div v-if="!registerActive" class="wallpaper-login"></div>
      </transition>
      <div class="wallpaper-register"></div>

      <div class="container">
         <div class="row">
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
   </div>

    <div>
      <div>

      </div>
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

<style>

</style>