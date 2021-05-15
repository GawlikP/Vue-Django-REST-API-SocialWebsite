<template>
  <div class="container" >
   <center>
      
        <PostFormComponent/>
        <PostFetchComponent/>

        
   </center>
  </div>
</template>

<script>
// @ is an alias to /src
import PostFetchComponent from '@/components/Posts/PostFetchComponent.vue'
import PostFormComponent from '@/components/Posts/PostFormComponent.vue';
export default {
  name: 'Posts',
  components: {
      PostFetchComponent,
      PostFormComponent,
  },
  data(){
    return{
      username : "" 
    }
  },
  created(){
    if(window.sessionStorage.getItem("username")){
      this.username = window.sessionStorage.getItem("username");
    }
  }
}
</script>