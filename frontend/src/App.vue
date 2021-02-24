<template>
  <div id="nav">
    <router-link to="/">Strona Główna</router-link> |
    <router-link to="/about">Cokolwiek</router-link> |
    <router-link to="/posts">Posty</router-link> |
    <router-link to="/accounts">Rejestracja</router-link>
  </div>
  <router-view/>
</template>

<style>
body{
 padding: 0;
 margin: 0;
 background-color: black;

}
#app {
  font-family: Avenir, Roboto, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
