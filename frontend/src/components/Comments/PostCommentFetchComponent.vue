<template>
    <div >
  
        <div class="container mb-2" >
    <a data-toggle="tooltip" title="Komentarze" class="m-2"  role="button" style="color: rgb(59, 89, 152);" @click="collapse1 = !collapse1"  >
        <i class="fas fa-comments fa-lg"></i><MDBBadge color="danger" pill notification v-if="licznik">{{licznik}}</MDBBadge>
    <MDBIcon iconstyle="fab"  size="lg"></MDBIcon>
  </a> 
    
    <tbody v-for="comment in comments" :key="comment.id"  style="text-align:left;">

    
        <MDBCollapse id="collapsibleContent1" v-model="collapse1">
           <table class="borderless" style="text-align:left">
                <tr style="color:black">
                    <strong >{{authors[comment.author]}}</strong>
                </tr>

                <tr style="color:black">
                    {{comment.content}}
                </tr>
                <br>
            </table>
        </MDBCollapse> 
                 
    </tbody>
     
        <MDBCollapse id="collapsibleContent1" v-model="collapse1">
           
              <form @submit.prevent="createComment">
                    <MDBInput  label="twój komentarz..."   size="lg" type="text"  col-md v-model="comment.content" />
                    <br> 
                    <MDBBtn color="danger" type="submit" >Dodaj komentarz</MDBBtn >
                   
                </form>
              
        </MDBCollapse> 
                
    </div>
    </div>
</template>

<script>
  
     import { MDBCollapse, MDBIcon ,MDBInput, MDBBtn,MDBBadge } from "mdb-vue-ui-kit";
     import { ref } from 'vue';
//import { MDBTable  } from "mdb-vue-ui-kit";
export default {

    name: 'PostCommentFetchComponent',
    props:{
        post_id: Number,
    },
    components: {
          MDBCollapse,
          MDBIcon,
          MDBInput,
          MDBBtn,
          MDBBadge
         
          
     //   MDBTable
    },
    async created() {
            this.getComments();
    },
    data(){
        return {
            comments: [],
            authors: [],
            comment: {
                
                'content': '',
                'post': `${this.post_id}`  
            },
            posted: 0,
            errors:{},
            licznik:0
        }
    },
    methods:{
        async getComments(){
            this.comments=[];
            this.licznik=0;
            var licznik=0;
            var token = await window.sessionStorage.getItem('token');
            const header = {
                'Authorization': `Token ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json' 
            }
            var response = await fetch('http://localhost:8000/comments/', {headers: header})
            var comments = await response.json()
            comments.forEach(comment => {
                if (comment['post'] === this.post_id){this.comments.push(comment)
                   licznik++;}
            });
           
            var temp = this.comments;
            temp.forEach(comment => {
                
                this.getAuthors(comment);
            });
            this.comments = await temp;
            this.licznik=licznik;
        },
        async getAuthors(comment){
               
            var token = await window.sessionStorage.getItem('token');
            const headers = {
                'Authorization': `Token ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json' 
            }


            return this.axios.get(`http://localhost:8000/accounts/${comment.author}`, {headers: headers}).then(response => {
                console.log(response.data)

                this.authors[comment.author] = JSON.stringify(response.data["username"])
            })
        },
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
            await this.getComments()
          
         }  
        
    },
     setup() {
      const collapse1 = ref(false);

      return {
        collapse1
      }
    }
}
</script>
<style  scoped>

</style>
