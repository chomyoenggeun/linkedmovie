<template>
  <div class="container color">
    <h1 class="center">안녕하세요 {{user.username}} 님</h1>

    <div class="button">
      <b-button><router-link @click.native="logout" to="Home">Logout</router-link></b-button>
      
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
.color{
  color: #dddddd;
}

.button{
  text-align: center;
  color: #dddddd;
  text-decoration: none;
}
.center{
  text-align: center;
}
</style>