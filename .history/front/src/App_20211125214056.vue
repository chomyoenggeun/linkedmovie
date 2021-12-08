<template>
  <div id="app">
    <ul class="horizontal">
      <li><router-link class="active" to="/home"><img class="size" :src="require('@/assets/sample.svg')" alt=""></router-link></li>
      <li><router-link class="active" to="/home">Home</router-link></li>
      <!-- <li><router-link class="active" to="/genre-movie">FavoriteMovie</router-link></li> -->
      <li><router-link class="active" to="/review">Review</router-link></li>
      <li v-if="isLogin" class="rightli" style="float:right"><router-link class="menubt_right" to="/mypage"
      >Mypage</router-link></li>
      <li v-else class="rightli" style="float:right"><router-link to="/account/login">Login</router-link></li>
    </ul>

    <router-view
    @login="isLogin=true"/>
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
body, html{
  width: 100%;
  height: 100%;
  background: #111111;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  background: #111111;
  width: 100vw;
  height: 100vh;
  /* color: #dddddd; */
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

/* #nav a.router-link-exact-active {
  color: #dddddd;
} */
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active:hover {
  /* background-color: #04AA6D; */
  background: rgb(6,5,87);
  background: linear-gradient(180deg, rgba(6,5,87,1) 0%, rgba(43,12,69,1) 100%);
  color: #dddddd;
}
.size{
  width: 20px;
}
</style>