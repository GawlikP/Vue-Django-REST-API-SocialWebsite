
<template>
  <div class="about">
   
    <h1>This is an about page</h1>
    <img alt="Vue logo" src="../assets/szczescboze.png">
    <h3><p >
        Szczesc boze mlody byku, witamy w tym kondominium niemiecko rosyjskim pod zydowskim ukladem powierniczym. 
        Otworz sobie kustoszka i kontynuuj swoja podroz z rozwaga
       </p></h3>
   
  </div>
</template>

<script>
// @ is an alias to /src

//import PostFetchComponent from '@/components/Posts/PostFetchComponent.vue'
export default {
  name: 'About',
  components: {
     // PostFetchComponent,
   
  },

  setup()
  { window.localStorage.setItem("cokolwiek","cokolwiek")
    
  }
}
</script>
