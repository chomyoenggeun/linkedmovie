<template>
  <div id="app">
    <div id="nav">

      <div>
        <b-navbar toggleable="lg" type="dark" variant="info">
          <b-navbar-brand href="#">NavBar</b-navbar-brand>

          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
              <b-nav-item href="#">Link</b-nav-item>
              <b-nav-item href="#" disabled>Disabled</b-nav-item>
            </b-navbar-nav>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
              <b-nav-form>
                <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
              </b-nav-form>

              <b-nav-item-dropdown text="Lang" right>
                <b-dropdown-item href="#">EN</b-dropdown-item>
                <b-dropdown-item href="#">ES</b-dropdown-item>
                <b-dropdown-item href="#">RU</b-dropdown-item>
                <b-dropdown-item href="#">FA</b-dropdown-item>
              </b-nav-item-dropdown>

              <b-nav-item-dropdown right>
                <!-- Using 'button-content' slot -->
                <template #button-content>
                  <em>User</em>
                </template>
                <b-dropdown-item href="#">Profile</b-dropdown-item>
                <b-dropdown-item href="#">Sign Out</b-dropdown-item>
              </b-nav-item-dropdown>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>
      </div>



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
</style>