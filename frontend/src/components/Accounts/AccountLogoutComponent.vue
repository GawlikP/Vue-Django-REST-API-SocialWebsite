<template>
    <div id ="AccountLogoutComponent">
         <MDBBtn color="danger" @click="logout()" rounded size="lg" class="mb-2">Wyloguj sie</MDBBtn>           
   
    </div>

</template>
<script>
import {  MDBBtn  } from "mdb-vue-ui-kit";

export default ({
    name: 'AccountLoginComponent',
    components: {
      MDBBtn
    },
    created: function (){
        window.sessionStorage.clear()
        this.ChangeRoute('/')   
    },
    methods: {
            logout(){
                    window.sessionStorage.clear()
                    this.ChangeRoute('/')
            },
            ChangeRoute(path){
                this.$router.push(path);
       
                }
    }
})
</script>
