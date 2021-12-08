<template>
  <div id="app">
    <div id="nav">
      <ul class="horizontal">
        <li><a class="active" href="javascript:void(0)">Home</a></li>
        <li><a href="javascript:void(0)">News</a></li>
        <li><a href="javascript:void(0)">Contact</a></li>
        <li class="rightli" style="float:right"><a href="javascript:void(0)">About</a></li>
      </ul>

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
ul.horizontal {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}
ul {
    display: block;
    list-style-type: disc;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    padding-inline-start: 40px;
}
*, *:before, *:after {
    box-sizing: inherit;
}
li {
    text-align: -webkit-match-parent;
}
</style>