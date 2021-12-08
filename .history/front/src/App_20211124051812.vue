<template>
  <div id="app">
    <div id="nav">
      <ul class="horizontal">
        <li><router-link class="active" to="/home">LOGO</router-link></li>
        <li><router-link class="active" to="/home">Home</router-link></li>
        <li><router-link class="active" to="/favorite-movie">FavoriteMovie</router-link></li>
        <li><router-link class="active" to="/review">Review</router-link></li>
        <li v-if="isLogin" class="rightli" style="float:right"><router-link class="menubt_right" to="/mypage"
        >Mypage</router-link></li>
        <li v-else class="rightli" style="float:right"><router-link class="menubt_right" to="/mypage"
        >Mypage</router-link></li>
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

.active {
  background-color: #04AA6D;
}
</style>