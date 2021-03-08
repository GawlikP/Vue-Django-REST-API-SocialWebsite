<template>
    <div id="Account RegisterComponent">

        

            <form @submit.prevent="createAccount">
                <div class="d-grid gap-2 col-3 mx-auto">
                    <MDBInput  label="Login" white size="lg" v-model="account.username" />
                        <br>
                    <MDBInput label="Hasło" white size="lg" type="password" v-model="account.password" />
                        <br>
                    <MDBInput label="Powtórz hasło" white size="lg" type="password" v-model="account.password2" />
                        <br>
                    <MDBInput label="Email" white size="lg" type="email" v-model="account.email" />
                        <br>
                    <MDBBtn color="info" type="submit" size="lg" rounded>Zarejestruj się</MDBBtn>
 
                </div>

                <h1 v-if="output">{{output}} </h1>
                
            </form> 
        </div>
 
</template>
<script>

import { MDBInput, MDBBtn, } from 'mdb-vue-ui-kit';

export default {
    name: 'AccountRegisterComponent',
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
                'password2': '',
                'email': '',

            },
            output: '',
            errors: {},
        }
    },
    methods: {
        async createAccount(){
            var response = await fetch('http://localhost:8000/accounts/',{
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
               
                body: JSON.stringify(this.account)
            });
            //var res = await response;
            var output = await response.json()
            this.output = output;
        },
    }

}
</script>
<style scoped>

</style>