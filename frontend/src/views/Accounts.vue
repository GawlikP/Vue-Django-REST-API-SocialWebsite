<template>
  <div class="container" >
  <center>  <img alt="Vue logo" src="../assets/szczescboze.png">
        <h1>Szczesc Boze, obywatelu kondominium zydowsko/rosyjskiego pod niemieckim zarzadem powierniczym <br>
        Zachowaj spokój, otwórz kustosza i kontynuuj swoją podróż</h1>    
  
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
