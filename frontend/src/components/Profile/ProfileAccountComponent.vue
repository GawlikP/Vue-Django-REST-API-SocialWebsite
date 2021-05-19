<template>
<div id="exist" v-if="exist == 'yes'">
<div class="flex">
    <div class="hflex wi">
        <img class="profile-img" src="@/assets/Pepe.jpg">
        <div class="vflex wi">
            <div class="hflex flex-header">
                <h3>{{account.username}}</h3>
                <button class="btn btn-light" @click="collapse1 = !collapse1">edytuj profil</button>
            </div>
            <div class="vflex flex-body">
                <div class="time">
                   Dołączył: {{account.created}}
                </div>
                <div class="opis">
                    {{profile.note}}
                </div>
                <MDBCollapse id="collapsibleContent1" v-model="collapse1">
                
                    <form class="form-group" @submit.prevent="editNote">
                            <MDBInput  label="twój nowy opis"  style=" width:100%!important" size="lg" type="text"  class="w-50" v-model="content.note" />
                    <br>
                    <MDBBtn color="danger" type="submit" onclick="">Edytuj opis</MDBBtn >
                    </form>
           
                </MDBCollapse>
                <div class="hflex">
                    <div>666 Obserwujących</div>
                    <div>2137 polubień</div>
                    <div>420 znajomych</div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="hflex wi mt">
        <div class="vflex-autor m10 totop">
            <img class="post-img" src="@/assets/Pepe.jpg">
            <div>23h ago</div>
            <button class="btn btn-primary">Edytuj</button>
            <button class="btn btn-danger">Usuń</button>
        </div>
        <div class="vflex-post wi left m10">
            <h4>Opis uzytkownika</h4>
            <div>{{profile.description}}</div>
        </div>
    </div>
</div>
</div>
<div id="nope" v-else>
    <center>
    <div class="container">
    <div class="hflex wi">
        <img class="profile-img" src="@/assets/Pepe.jpg">
        <div class="vflex wi">
            <div class="hflex flex-header">
                <h1>Niema takiego profilu</h1>
                
            </div>
            <div class="vflex flex-body">
                
            </div>
        </div>
    </div>
    </div>
    </center>
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
            posts:[
            ],
            profile: [],
            account: [],
            
            content: {
                note: ''
            },
            exist: 'no',
            show_note_form: false,
        }
    },
    async created(){
        this.getProfile();
        
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

          return this.axios.get(`http://localhost:8000/profiles/${this.id}/`, {headers: headers, validateStatus: function (status) {
      return status >= 200 && status < 500
    }})
            .then(response =>{
                if(response.status == 200){
                    console.log(response);
                    this.profile = response.data;
                    this.getAccount();
                    this.exist = 'yes';
                }
                else {
                    alert('Niema takiego profilu!');
                }
            } );
            //this.id
      },
      async getAccount(){
          var token = await window.sessionStorage.getItem('token');

          const headers = {
              'Authorization': `Token ${token}`,
              'Accept': 'application/json',
              'Content-Type': 'application/json'
          }

          return this.axios.get(`http://localhost:8000/accounts/${this.profile.account}`, {headers: headers, validateStatus: function (status) {
      return status >= 200 && status < 500
    }})
            .then(response =>{
                if(response.status == 200){
                    console.log(response);
                    this.account = response.data;
                    this.exist = 'yes';
                }
                else {
                    alert('Niema takiego profilu!');
                }
            } );
      },
      async editNote(){
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
             //console.log(output)
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
      }

    }

}
</script>
<style scoped>
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