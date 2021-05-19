<template>
    <div  >
         <form @submit.prevent="createComment">
                    <MDBInput  label="twój komentarz"  style="background-color:silver" size="lg" type="text"  class="w-50" v-model="comment.content" />
                    <br>
                    <MDBBtn color="danger" type="submit" onclick="javascript:window.location.reload()">Dodaj komentarz</MDBBtn >
                    
                </form>
    </div>
</template>
<script>
import { MDBInput, MDBBtn } from 'mdb-vue-ui-kit';


export default {
    name: 'NewPostCommentFormComponent',
    components: {
      MDBInput,
      MDBBtn,
          
    },
    props:{
        post_id: Number,
    },
    data(){
        
        return {
            comment: {
                
                'content': '',
                'post': `${this.post_id}`  
            },
            posted: 0,
            errors:{},
            
        }
    },
    methods:{
      async createComment(){
             var auth = await window.sessionStorage.getItem('token')
                    
                    const headers = {
                        
                            'Authorization': `Token ${auth}`,
                            'Accept': 'application/json',
                            'Content-Type': 'application/json' 
                    }
             var response  = await fetch('http://localhost:8000/comments/',{
                 method: 'post',
                 headers: headers,
                 body: JSON.stringify(this.comment)
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
    }
}
</script>
<style scoped>

</style>
