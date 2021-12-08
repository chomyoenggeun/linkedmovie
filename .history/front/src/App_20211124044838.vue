<template>
  <div id="app">
    <div id="nav">

      <router-link class="menubt" to="/home">LOGO</router-link> |
      <router-link class="menubt" to="/home">Home</router-link> |
      <router-link class="menubt" to="/favorite-movie">FavoriteMovie</router-link> |
      <router-link class="menubt" to="/review">Review</router-link> |
      <span v-if="isLogin">
        <router-link class="menubt_right" to="/mypage"
        >Mypage</router-link> |
      </span>
      <span v-else>
        <router-link class="menubt" to="/account">Account</router-link>
      </span>
    </div>
    <router-view
    @login="isLogin=true">
  </div>
</template>

<script>
export default {
  name : 'App',
    data: function(){
    return {
      isLogin: false,
    }
  }, 
  created : function(){
    const token = localStorage.getItem('jwt')
    if(token){
      this.isLogin = true
    }
  },
  methods : {
    checkLogin: function(loginState){
      this.isLogin = loginState
    }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  background: #111111;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}
/* .menubt{
  padding : 20px;
  background: #255ca3;
  list-style:none;
} */
.menubt:hover{
  background:#255ca3; margin:auto; position:relative; display:box;
}
.menubt_rigth{
  text-align: right;
}

#nav a.router-link-exact-active {
  color: #dddddd;
}
</style>