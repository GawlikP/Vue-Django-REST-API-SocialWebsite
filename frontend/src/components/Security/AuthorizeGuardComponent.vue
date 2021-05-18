<template>
    <div>
    <!-- <i v-if="ok == false" class="far fa-angry"></i>
    <i v-if="ok == true" class="fas fa-check"></i> -->
            <router-link 
            v-for="link in links" 
            v-bind:key="link.id"  
            class="col-lg-auto text-nowrap mx-1 my-0" 
            v-bind:to="`${ link.link }`" >{{ link.title }}</router-link>
    </div>
</template>
<script>
export default {
    name: 'AuthorizeGuardComponent',
    data() {
        return {
            enable: 'duno',
            ok: false,
            is_token: false,
            auth: {
                'token': ''
            },
            allowed_urls: [
                '/login',
                '/registration',
                '/'
            ],
            loggedin_links: [
                {link: "/profile", title: "Profil", id: 1},
                {link: "/logout", title: "Wyloguj", id: 2}
            ],
            loggedout_links: [
                {link: "/registration", title: "Rejestracja", id: 3},
                {link: "/login", title: "Zaloguj się", id: 4}
            ],
            links: [
                {link: "/registration", title: "Rejestracja", id: 3},
                {link: "/login", title: "Zaloguj się", id: 4}
            ]
        }
    }, 
    methods:{
            checkSession(){
                if(window.sessionStorage.getItem('token') && 
                    window.sessionStorage.getItem('username')
                ) {this.is_token = true; this.enable= 'OK'}
            },

            async checkToken(){

                if(this.is_token == true){

                    this.auth['token'] = await window.sessionStorage.getItem('token')
                    var tkn = `Token ${this.auth['token']}`
                    const headers = {
                        
                            'Authorization': `Token ${this.auth['token']}`,
                            'Accept': 'application/json',
                            'Content-Type': 'application/json' 
                    }
                    
                
                   // var tkn = `Token 53446787654537689654678`
                    console.log(tkn)
                    //alert(this.auth['token'])
                    var response = await fetch('http://localhost:8000/accounts/im_auth/',{
                    method: 'post',
                    headers: headers,
                        //body: JSON.stringify(this.auth)
                        //body: JSON.stringify(this.auth)
                    })

                    console.log(response)
                    var output = await response.json()
                   
                    
                   // alert("Status:" + response.status + " \n JSON:" + jsons)
                    if(response.status == 200){
                        this.ok =true;
                        console.log(output)
                        this.links = this.loggedin_links;
                    }

                } else {
                    this.ok = false;
                    this.links = this.loggedout_links;
                }
            },
            checkRoute(){

                    
                    if(!this.allowed_urls.includes(this.$route.path )){
                        confirm('Nie posiadasz uprawnien!')
                        this.$router.push('/');
                    }
            }

    },
    async created(){
            this.checkSession();
            if(this.token == false){
                confirm('Twoja sesja wygasła!')
                        this.$router.push('/');
            }
            await this.checkToken();
            if(!this.ok){
                this.checkRoute();
            }
    },
    watch:{
    async $route (){
            this.checkSession();
            if(this.token == false){
                confirm('Twoja sesja wygasła!')
                        this.$router.push('/');
            }
            await this.checkToken();
            if(!this.ok){
                this.checkRoute();
            }
        }
    }
}
</script>