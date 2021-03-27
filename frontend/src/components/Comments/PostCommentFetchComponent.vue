<template>
    <div >
  
        <div class="container" >
            

    <tbody v-for="comment in comments" :key="comment.id" style="text-align:left">
        <tr>
           <strong>{{authors[comment.id].username}}</strong>
        </tr>
        <tr>
        {{comment.content}}
        </tr>
        
        <hr> 
        
       
    </tbody>
 
    </div>
    </div>
</template>

<script>

//import { MDBTable  } from "mdb-vue-ui-kit";
export default {

    name: 'PostCommentFetchComponent',
    props:{
        post_id: Number,
    },
    components: {
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
    }
}
</script>
<style  scoped>

</style>
