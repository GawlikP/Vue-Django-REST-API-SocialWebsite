<template>

    <div id="PostFetchComponent">
        <div class="container" >
             <MDBTable>

    <tbody v-for="post in posts" :key="post.id" style="text-align:left">
        <tr>
           <strong>{{post.title}}</strong>
        </tr>
        <tr> <b> Author: {{authors[post.author].username}}  </b><br>
        {{post.content}}
        </tr>
        <tr>
            <p class="text-center">
                
              <i data-toggle="tooltip" title="Lubię" @click="giveHearth(post)" v-if="hearthed[post.id] == false" class="far fa-heart" style="color:red"></i>
                      <i v-else class="fas fa-heart"   style="color:red"></i> 
                        {{post.hearts}}
            </p>  
        </tr>

        <tr>
            <PostCommentFetchComponent v-bind:post_id="post.id" />
           
        </tr>
        <hr> 
        
       
    </tbody>
  </MDBTable>
            
            
        </div>
    </div>

</template>
<script>
    import { MDBTable  } from "mdb-vue-ui-kit";
    import  PostCommentFetchComponent  from '@/components/Comments/PostCommentFetchComponent.vue';

export default {
 
    name:'PostFetchComponent',
     components: {
      PostCommentFetchComponent,
      MDBTable 
     // MDBBtn
    },
    data(){
        return {
            posts: [],
            hearthed: [],
            authors: [],
        }
    },
    async created(){
        this.getPosts()
        this.posts.forEach(post => {
                this.hearthed[post.id] = false;
        });
    },
    
    methods:{
        async getPosts(){

            var token = await window.sessionStorage.getItem('token')
                    
                    const headers = {
                        
                            'Authorization': `Token ${token}`,
                            'Accept': 'application/json',
                            'Content-Type': 'application/json' 
                    }

            var response =  await fetch('http://localhost:8000/posts/', {headers: headers});
            this.posts = await response.json()
            this.posts.forEach(post => {
                if(typeof this.hearthed[post.id] === 'undefined')this.hearthed[post.id] = false;
        });
            this.posts.forEach(post => {
                    this.setAuthors(post, headers);
                });

           console.log(this.hearthed) 
        },
        async setAuthors(post, headers){

            

            var response = await fetch(`http://localhost:8000/accounts/${post.author}`, {headers: headers});
                    var json = await response.json();
                    this.authors[post.id] = json;
        },
        async giveHearth(post){
            console.log(post);
            post.hearts +=1;
            var postr = post;
            postr.author_name = null; 

            var token = await window.sessionStorage.getItem('token')
                    
                    const headers = {
                        
                            'Authorization': `Token ${token}`,
                            'Accept': 'application/json',
                            'Content-Type': 'application/json' 
                    }

            this.hearthed[post.id] = true;
            var response = await fetch(`http://localhost:8000/posts/${postr.id}/`, {
                method: 'put',
                headers: headers,
                body: JSON.stringify(postr)
            });
            this.posts.push(await response.json());
           
            this.getPosts();
        }
    },

}
</script>
<style scoped>
tr,hr {
color: white;
}

</style>