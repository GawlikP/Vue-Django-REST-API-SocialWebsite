<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8 justify-content-center ">
                <div class="row mb-2 bg-danger shadow rounded ">

                    <div class="bg-danger shadow rounded col-md-4"> 
                        <img class="col-12 mt-4 mb-4 rounded-start" src="@/assets/Pepe.jpg"> 
                    </div>
                    
                    <div class="col-md-8 p-3 ">
                
                        <div class="d-flex p-0 justify-content-start">
                            <h1 class="py-3 text-md-start align-self-center">
                                {{account.username}}
                            </h1>
                        </div>

                
                        <div class="col-12 px-2">
                            <p class="col-md-12 m-0 text-start dim-text-underline"><i class="fas fa-user align-self-center px-1" data-toggle="tooltip" title="Edytuj profil"></i>Dołączył: {{account.created}}}</p>
                            <div class="col-md-12 pb-3 text-start">{{profile.note}}
                                <i @click="collapse1 = !collapse1" class="fas fa-pencil-alt p-2 small-icon hand active" data-toggle="tooltip" title="Edytuj profil" v-on:click="show_alert()"></i>    
                            </div>
                            
                            <MDBCollapse id="collapsibleContent1" class="mb-2" v-model="collapse1">
                                <form class="form-group " @submit.prevent="editNote">
                                        <MDBInput  label="twój nowy opis"  style=" width:100%!important" size="lg" type="text"  class="w-50" v-model="content.note" />
                                <MDBBtn class="mt-2" color="dark" type="submit" onclick="">Edytuj opis</MDBBtn >
                                
                                </form>
                            </MDBCollapse>

                            <div class="d-flex flex-row align-items-center p-0 m-0 small-text text-center text-start my-bg-info">
                                <div class="flex-fill px-0 py-1 m-0 align-self-center ">
                                    Obserwujący: {{watchers}}   
                                </div>
                                <div class="flex-fill px-0 py-1 m-0 mx-2 align-self-center ">
                                    Polubień: {{likes}}
                                </div>
                                <div class="flex-fill px-0 py-1 m-0 align-self-center ">
                                    Znajomi: {{friends}}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                    
                

                <div class="row justify-content-center  ">
                    <div class="row bg-dark p-3 my-3 shadow rounded">
                        
                       
                        <div class="d-flex justify-content-between p-0 pb-2 m-0 border-bottom border-1">
                            
                            
                            <div class="d-flex flex-row">
                                <img class="p-0 m-0 rounded-circle align-self-center shadow xsmall-img" src="@/assets/Pepe.jpg">
                                <div class="d-flex flex-column justify-content-start p-0 ps-2 m-0">
                                    <div class="p-0 m-0 text-start text-decoration-underline">user</div>
                                    <p class="p-0 m-0 text-start small-text dim-text">Opublikowano: data</p>
                                </div>
                            </div>

                            
                            <div class="d-flex flex-column p-0 m-0 justify-content-end text-end">
                                <div class="p-0 m-0 small-text dim-text hand active-danger" v-on:click="show_alert(1)">
                                    <i class="fas fa-pen p-1" data-toggle="tooltip"></i>
                                    Edytuj post</div>
                                <div class="p-0 m-0 small-text dim-text hand active-danger" v-on:click="show_alert(1)">
                                    <i class="fas fa-trash-alt p-1" data-toggle="tooltip"></i>
                                    Usuń post</div>
                            </div>
                        </div>
                        
                      
                        <div class="d-flex p-0 justify-content-between">
                            <h5 class="py-3 text-start align-self-center">
                                tytuł
                            </h5>
                        </div>
                        <div class="col-12 ms-3">
                            <p class="col-12 p-0 m-0 text-start">treśc</p>
                        </div>
                       
                           
                        
                        <div class="row p-1 m-0 mb-2 border-bottom border-1">
                            <div class="col-6 hand" v-on:click="show_alert(1)">
                                <i class="fas fa-heart px-1" data-toggle="tooltip"></i>
                                lajki
                            </div>
                            <div class="col-6 hand" v-on:click="show_alert(1)">
                                <i class="fas fa-comments px-1" data-toggle="tooltip"></i>
                                Komentarze
                            </div>
                        </div>

                    
                    </div>
                </div>
               
            </div>
        </div>
    </div>
</template>


<script>
import { MDBCollapse ,MDBInput, MDBBtn } from 'mdb-vue-ui-kit';
import { ref } from 'vue';

export default {

    

    name: 'ProfileAccountComponent',
    components: {
        MDBInput,
        MDBBtn,
        MDBCollapse
      
    },
    props: {
        id: String,
    },
    data(){
        return {
            posts:[],
            profile: [],
            account: [],
            content: {
                note: ''
            },
            autors: [],
            exist: 'no',
            show_note_form: false,
        }
    },
    async beforeCreate(){
        var result = await this.getProfile().then(response => {
            console.log(response.account);
           return this.getAccount(response.account).then(response =>{
               console.log(response);
               return this.getPostsofUser(response.id).then(response =>{
                   console.log(response);
                    for(const post in response){
                    this.setAuthors(post);
                    }
                    return this.authors;
               });
           });

        }); 
        console.log(result);
        console.log(this.profile);
        console.log(this.account);
        //await this.getAccount();

    },
    setup() {
        const collapse1 = ref(false);

        return {
            collapse1
        }
    },
    
    methods: {
        async getProfile()
        {
          var token = await window.sessionStorage.getItem('token');

            const headers = {
                'Authorization': `Token ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }

    
             var result =await fetch(`http://localhost:8000/profiles/${this.id}`, {
                method: 'get',
                headers: headers,
            }).then(results=>{
                this.profile=results.json()
                return this.profile;
                
            });
            
            return result;
        },

        async getAccount(acc)
        {
            var token = await window.sessionStorage.getItem('token');

            const headers = {
                'Authorization': `Token ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }

           var result =await fetch(`http://localhost:8000/accounts/${acc}`, {
                method: 'get',
                headers: headers,
            }).then(results=>{
                this.account=results.json()
                return this.account;
                
            });
            
            return result;
        },

        async editNote()
        {
            var token = await window.sessionStorage.getItem('token');

            const headers = {
                        
                'Authorization': `Token ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json' 
            }

            var data = this.profile;
            data.note = this.content.note;


            var response  = await fetch(`http://localhost:8000/profiles/${this.id}/`,{
                method: 'put',
                headers: headers,
                body: JSON.stringify(this.profile)
            });

            var res = await response;
            var output = await response.json()
            var status = res.status;
            
                this.posted  = -1;
                console.log(status);
                if (status == 200){
                    this.profile = output;
                    alert('Udalo sie zmienic notke profilu!')}
                else if(status == 401){
                     alert('Nie masz uprawnien!')
                
               }else {
                   console.log(output)
                   alert('Cos poszlo nie tak :/')
               }
               
        },
        
        async unhide_note(){
            this.show_note_form = true;
        },

        async getPostsofUser(id){
            var token = await window.sessionStorage.getItem('token')
                    
                    const headers = {
                        
                            'Authorization': `Token ${token}`,
                            'Accept': 'application/json',
                            'Content-Type': 'application/json' 
                    }
            var result =await fetch(`http://localhost:8000/accounts/${id}/posts`, {
                method: 'get',
                headers: headers,
            }).then(results=>{
                this.posts=results.json()
                return this.posts;

            });
            
            return result;
        },
        async setAuthors(post){
                
            var token = await window.sessionStorage.getItem('token')    
                const headers = { 
                    'Authorization': `Token ${token}`,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json' 
                } 
            
            var response = await fetch(`http://localhost:8000/accounts/${post.author}`, {headers: headers}).then(results=>{
                
                this.authors[post.author] = results.json();
                return this.autors;
            });

               console.log(response);     
        },
      

    }

}
</script>
<style scoped>
.xsmall-img{
    width: 45px;
    height: 45px;
}

.small-text, .dim-text{
    font-size: 0.85em;
    /* text-decoration: underline dotted; */
}
.dim-text, .dim-text-underline{
    color: #ccc;
}
.dim-text-underline{
    text-decoration: underline;
}
h1{
    text-decoration: underline;
}
.hand:hover{
    cursor: pointer;
}
.active, .active-danger, .active-blue{
    transition: all 0.2s;
}
.active:hover{
    color: darkslateblue;
}
.active-danger:hover{
    color: tomato;
    }
.active-blue:hover{
    color: lightskyblue;
    }
.profile-img{
    width: 250px;
    height: auto;
    border-radius: 15% 0% 0% 15%;
}
.post-img{
    width: 100px;
}
.flex{
    display: flex;
    flex-direction: column;
    align-items: center;
    /* width: 100%; */
}
.hflex{
    display: flex;
    flex-direction: row;
    justify-content: center;
}
.vflex{
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-direction: column;
    background-color: lightcoral;
}
.vflex-post{
    display: flex;
    flex-direction: row;
    justify-content: start;
    flex-direction: column;
    background-color: #99394ac1;
    padding: 15px 30px;
}
.vflex-post-button{
    display: flex;
    flex-direction: row;
    justify-content: start;
    flex-direction: column;
    background-color: rgb(47, 79, 61);
    /* padding: 15px 30px; */
}
.vflex-autor{
    display: flex;
    flex-direction: row;
    justify-content: start;
    flex-direction: column;
}
.vflex div{
    padding: 10px;
    justify-content: space-between;
}

.time{
    font-size: 0.8em;
    color: #555;
}
.flex-body * {
     text-align: left;
}
.opis{
    background-color: #99394ac1;
    color: black;
    font-family:Arial, Helvetica, sans-serif;
    font-weight: bold;
    padding: 20px 15px !important;
}
.shadow{
    box-shadow: 2px 2px 5px rgba(0,0,0,0.5);
}

.wi{width:70%;}

.left *{
    text-align: left;
}
.m10{
    margin-right: 10px;
}
.mt{
    margin-top: 20px;
}

</style>