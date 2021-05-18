<template>
  <div>
    <!-- <div>{{this.$route.name}}</div> -->
    <div id="nav" class="d-flex flex-row flex-wrap justify-content-center align-content-lg-center align-content-start py-1 px-3 mb-5" v-if="`${this.$route.name}`!=`Home`">
      <router-link class="col-lg-auto text-nowrap mx-1 my-0" v-for="url in urls" v-bind:key="url.link" v-bind:to="`${ url.link }`">{{ url.title }}</router-link>
      <AuthorizeGuardComponent />
    </div>
    <router-view/>
  </div>
</template>



<script>
import AuthorizeGuardComponent from './components/Security/AuthorizeGuardComponent.vue'
  export default{

    components:{
        
      AuthorizeGuardComponent
    },
     data(){
      return {
        urls: [
          {link: "/",         title: "Strona Główna"},
          {link: "/about",    title: "Cokolwiek"},
          {link: "/posts",    title: "Posty"}
        ]
      }
    }

  }
</script>


<style>


body{
 padding: 0;
 margin: 0;
 background-color: rgb(17, 17, 17);

}
#app {
  font-family: Avenir, Roboto, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
}

#nav {
  height: 60px;
  background-color: #F93154;
  box-shadow: 0px 8px 10px rgba(0,0,0,0.7);
}

#nav a {
  font-weight: bold;
  /* color: #2c3e50; */
  color: #ffffff;
  transition: all 0.25s;
}
#nav a:hover {
  /* color: #82c7ff; */
}

#nav a.router-link-exact-active {
  color: #3b3b3b;
  border-bottom: 1px solid #242424;
}
</style>
