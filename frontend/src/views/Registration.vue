<template>
  <div class="container" >
  <center>  
        <h1 style="color: white">Utwórz konto</h1>    
  
            <br>
            <AccountRegistrationComponent />
    </center>

  </div>
</template>

<script>
// @ is an alias to /src
import AccountRegistrationComponent from '@/components/Accounts/AccountRegistrationComponent.vue'

export default {
  name: 'Registration',
  components: {
    AccountRegistrationComponent,
  }
}
</script>

<style scoped>

</style>
