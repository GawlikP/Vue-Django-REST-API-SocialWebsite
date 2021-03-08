<template>
  <div class="container" >
  <center>  
        <h1 style="color: white">Utwórz konto</h1>    
  
            <br>
            <AccountRegisterComponent />
    </center>

  </div>
</template>

<script>
// @ is an alias to /src
import AccountRegisterComponent from '@/components/Accounts/AccountRegisterComponent.vue'

export default {
  name: 'Accounts',
  components: {
    AccountRegisterComponent,
  }
}
</script>

<style scoped>

</style>
