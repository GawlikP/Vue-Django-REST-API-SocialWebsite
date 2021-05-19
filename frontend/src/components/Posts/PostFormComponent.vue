<template>
   
   <div class="container-fluid card bg-black col-8">
   
        
        <div class="row">

            <div class="col-sm-12">
                <h5 class="card-title mt-4" style="text-align:left">Witaj, {{username}} </h5>
            </div>
        </div>
<form @submit.prevent="createPost">
<div>
                <h2><i class="fas fa-angry" v-if="posted == 1" style="color:red"></i>
                <i class="fas fa-smile" v-if="posted == -1" style="color:green"></i> </h2>

                <div v-if="posted == 1">
                    <MDBBadge  color="danger" v-for="(error, index) in errors" :key="error.id">
                        <b>{{index}} </b>: {{error[0]}}    
                    </MDBBadge>
                </div>
            </div>
        <div class="row">

               
                <div class="col-sm-2">
                    <img src="https://images92.fotosik.pl/504/9b065e813f1536e6.png" class="rounded-circle img-fluid w-50" alt="avatar" />
                </div>
           
                <div class="col-sm-4">
                 <MDBInput label="Tytuł Postu" white size="lg" v-model="post.title" class="form-control "/>
                </div>

                <div class="col-sm-4">
               <MDBInput label="Jak minął twój dzień ?" white size="lg" v-model="post.content" class="form-control" /> 
                   
                </div>

                <div class="col-sm-2">
                 <MDBBtn color="danger" type="submit" size="lg" onclick="javascript:window.location.reload()" rounded>Opublikuj</MDBBtn> 
                    
                </div>
            
        </div>
  </form>
   
    </div>
     

          
    
       

</template>

<script>
import { MDBInput, MDBBtn, MDBBadge } from 'mdb-vue-ui-kit';
export default {
    name: 'PostFormComponent',
     components: {
      MDBInput,
      MDBBtn,
        MDBBadge,
    },
    data(){
        return {
            post: {
                'title': '',
                'content': '',
                
            },
            posted: 0,
            errors:{},
            
        }
    },
    methods:{
         async createPost(){
             var auth = await window.sessionStorage.getItem('token')
                    
                    const headers = {
                        
                            'Authorization': `Token ${auth}`,
                            'Accept': 'application/json',
                            'Content-Type': 'application/json' 
                    }
             var response  = await fetch('http://localhost:8000/posts/',{
                 method: 'post',
                 headers: headers,
                 body: JSON.stringify(this.post)
             });
             var res = await response;
             var output = await response.json()
             var status = res.status;
             //console.log(output)
                this.posted  = -1;
                console.log(status);
               if (status == 201){
                   this.posted = -1;
               }else {
                   this.posted = 1;
               }
                if (this.posted == 1){
                    this.errors = output;
                }
         }
    },
    created(){
    if(window.sessionStorage.getItem("username")){
      this.username = window.sessionStorage.getItem("username");
    }
  }
}
</script>
<style scoped>
</style>