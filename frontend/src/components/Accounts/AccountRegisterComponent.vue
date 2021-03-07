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
// Importowanie tagow z MDB5, ladnych guziczkow itd
import { MDBInput, MDBBtn, } from 'mdb-vue-ui-kit';

export default {
    // nazwa komponentu, odpowiada tagowi jakiego trzeba uzyc
    // aby wywolac go w innym komponencie lub widoku
    name: 'AccountRegisterComponent',
    components: {
      MDBInput,
      MDBBtn,
      //  MDBBadge,
    },
    // zmienne uzywane w dzialaniu strony, musza byc zadeklarowane raz 
    // dzialaja i odswiezaja sie dynamicznie
    data(){
        return {
            account : {
                'username': '',
                'password': '',
                'password2': '',
                'email': '',

            },
            // do tej zmiennej bedzie przeniesiony json, ktory odesle nam serwer
            output: '',
            errors: {},
        }
    },
    // deklarowane sa tutaj metody, ktore beda uzywane w komponencie
    methods: {
        // async musi zostac uzyte z tego powodu, ze nie wiemy kiedy dostaniemy 
        // odpowiedz od serwera
        async createAccount(){
            // metoda fetch odpowaida za wyslanie requesta do serwera
            // dziala tak samo jak kazdy inny request
            // najpierw podajemy url
            // nastepnie metode ( post, get, delete, put)
            // nastepnie okresalmy headery ( 'Content-Type', 'Authorization')
            // w sekcji body nadajemy naszego jsona z trescia parametrow 
            //
            var response = await fetch('http://localhost:8000/accounts/',{
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
               
                body: JSON.stringify(this.account)
            });
            //var res = await response;
            // zmienna output jest tutaj nadpisywana przez pozysakna odpowiedz
            var output = await response.json()
            this.output = output;
        },
    }

}
</script>
<style scoped>

</style>