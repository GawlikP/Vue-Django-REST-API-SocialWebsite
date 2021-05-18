<template>
    <div id="AccountLoginComponent" class="col-12">
        <form @submit.prevent="loginAccount" class="col-12 d-flex flex-column justify-content-center align-items-lg-center h-100">
        <h1 style="color: white">Logowanie</h1>    
            <div class="d-grid gap-3 col-md-7 col-sm-12 m-sm-auto p-3 max-w-600px">
                <MDBInput  label="Login" white size="lg" v-model="account.username" />
                <MDBInput  label="Hasło" white size="lg" type="password" v-model="account.password" />
                <MDBBtn    class="mt-3 w-75 m-auto"  color="danger"  type="submit" size="lg" rounded>Zaloguj się</MDBBtn>
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
      MDBBtn
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
        async loginAccount(){
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
                // window.location.reload(true);
                this.$router.push('/posts')
                //alert(window.sessionStorage.getItem("token") + window.sessionStorage.getItem("username"));
            }
          
        },
    }

}
</script>
<style scoped>
.max-w-600px{
    max-width: 600px;
}
.btn-danger:hover, .btn-outline-danger:hover{
  background-color: rgb(66, 7, 10);
  border-color: rgb(255, 255, 255);
  color: white;
}
</style>