<template>
    <div id="AccountLoginComponent">

        

            <form @submit.prevent="createAccount">
                <div class="d-grid gap-2 col-3 mx-auto">
                    <MDBInput  label="Login" white size="lg" v-model="account.username" />
                        <br>
                    <MDBInput label="Hasło" white size="lg" type="password" v-model="account.password" />
                        <br>
                    <MDBBtn color="danger" type="submit" size="lg" rounded>Zaloguj się</MDBBtn>
 
                </div>

                <h1 v-if="output">{{output}} </h1>
                
            </form> 
        </div>
 
</template>
<script>

import { MDBInput, MDBBtn, } from 'mdb-vue-ui-kit';

export default {
    name: 'AccountLoginComponent',
    components: {
      MDBInput,
      MDBBtn,
      //  MDBBadge,
    },
    data(){
        return {
            account : {
                'username': '',
                'password': '',

            },
            output: '',
            errors: {},
        }
    },
    methods: {
        async createAccount(){
            var response = await fetch('http://localhost:8000/accounts/login/',{
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
               
                body: JSON.stringify(this.account)
            });
            //var res = await response;
             var output = await response.json()
            this.output = output;
            
            if(response.status == 200){
                window.sessionStorage.setItem("token",this.output["token"]);
                 window.sessionStorage.setItem("username",this.output["username"]);
                alert(window.sessionStorage.getItem("token"));
            }
          
        },
    }

}
</script>
<style scoped>

</style>