<template>
  <div class="container" >
  <center>  
        <h1 style="color: white">Logowanie</h1>    
  
            <br>
            <AccountLoginComponent />
    </center>

  </div>
</template>

<script>
// @ is an alias to /src
import AccountLoginComponent from '@/components/Accounts/AccountLoginComponent.vue'

export default {
  name: 'Login',
  components: {
    AccountLoginComponent,
  }
}
</script>

<style scoped>

</style>
