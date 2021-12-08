<template>
  <div>
    <div class="button">
      <b-button><router-link @click.native="logout" to="Home">Logout</router-link></b-button>
      
    </div>
  </div>
</template>

<script>
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
    }
  }
}
</script>

<style scoped>
.button{
  text-align: center;
  color: #dddddd;
  text-decoration: none;
}
</style>