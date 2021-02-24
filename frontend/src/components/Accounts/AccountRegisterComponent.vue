<template>
    <div id="Account RegisterComponent">
        <div class="jumbotron">
            <form @submit.prevent="createAccount">
                <MDBInput label="Nick" size="lg" v-model="account.nick" />
                <MDBInput label="Password" size="lg" v-model="account.password" />
                <MDBInput label="Confirm Password" size="lg" v-model="account.password2" />
            
                <MDBBtn color="secondary" type="submit"> Register </MDBBtn>
                <h1 v-if="output">{{output}} </h1>
            </form> 
        </div>
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
                'nick': '',
                'password': '',
                'password2': '',

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