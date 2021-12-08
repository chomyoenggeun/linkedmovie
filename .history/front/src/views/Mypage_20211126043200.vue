<template>
  <div class="container">
    <h1 class="center">안녕하세요 {{user.username}} 님</h1>

    <div>
      <b-button><router-link class="button" @click.native="logout" to="Home">Logout</router-link></b-button>
      
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'Mypage',
  props:{
    loginState : String,
  },
  methods: {
    logout: function() {
      console.log('is-login')
      this.$emit('is-login',false)
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Home' })
      this.$router.go()
    },
    setToken : function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
  created:function(){
    this.$store.dispatch('getUserData',this.setToken())
  },
  computed:{
    ...mapState(['user']),
  },
}
</script>

<style scoped>

.button{
  text-align: center;
  color: #dddddd;
  text-decoration: none;
}
.center{
  text-align: center;
}
</style>