<template>
    <div >
  
        <div class="container" >
    <a data-toggle="tooltip" title="Komentarze" class="m-2"  role="button" style="color: rgb(59, 89, 152);" @click="collapse1 = !collapse1"  >
        <i class="fas fa-comments fa-lg"></i>
    <MDBIcon iconstyle="fab"  size="lg"></MDBIcon>
  </a> 

    <tbody v-for="comment in comments" :key="comment.id"  style="text-align:left;">

    
        <MDBCollapse id="collapsibleContent1" v-model="collapse1">
           <table class="borderless" style="text-align:left">
                <tr style="color:black">
                    <strong>{{authors[comment.id].username}}</strong>
                </tr>

                <tr style="color:black">
                    {{comment.content}}
                </tr>
            </table>
        </MDBCollapse> 
               
    </tbody>
    
        <MDBCollapse id="collapsibleContent1" v-model="collapse1">
            <div class="form-outline mt-4">
                <form>
                    <MDBInput  label="twój komentarz..." white style="background-color:silver" size="lg" type="text"  class="w-50" />
                    <br>
                    <MDBBtn color="danger" >Dodaj komentarz</MDBBtn >
                    
                </form>
            </div>     
        </MDBCollapse> 
                
    </div>
    </div>
</template>

<script>
     import { MDBCollapse, MDBBtn, MDBInput, MDBIcon } from "mdb-vue-ui-kit";
     import { ref } from 'vue';
//import { MDBTable  } from "mdb-vue-ui-kit";
export default {

    name: 'PostCommentFetchComponent',
    props:{
        post_id: Number,
    },
    components: {
          MDBCollapse,
          MDBBtn,
          MDBInput,
          MDBIcon
          
     //   MDBTable
    },
    async created() {
            this.getComments();
    },
    data(){
        return {
            comments: [],
            authors: [],

        }
    },
    methods:{
        async getComments(){
            var token = await window.sessionStorage.getItem('token');
            const header = {
                'Authorization': `Token ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json' 
            }
            var response = await fetch('http://localhost:8000/comments/', {headers: header})
            var comments = await response.json()
            comments.forEach(comment => {
                if (comment['post'] === this.post_id)this.comments.push(comment)
            });

            this.comments.forEach(comment => {
                    this.getAuthors(comment, header);
            });
        },
        async getAuthors(comment, headers){
               

            var response = await fetch(`http://localhost:8000/accounts/${comment.author}`, {headers: headers});
            var json = await response.json();
            this.authors[comment.id] = json;
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
