<template>
  <div class="container" >
  <center>  <img alt="Vue logo" src="../assets/backendsiebawi.png">
        <h1> Witajcie przystojniaczki, tutaj tylko backend na chwile <br>
        Nie przeszkadzaj sobie i ciesz sie zyciem mordeczko</h1>    
  
        <PostFetchComponent/>
    </center>
  </div>
</template>

<script>
// @ is an alias to /src

import PostFetchComponent from '@/components/PostFetchComponent.vue'

export default {
  name: 'Posts',
  components: {
      PostFetchComponent
  }
}
</script>
