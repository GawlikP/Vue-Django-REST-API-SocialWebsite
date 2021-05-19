<template>

    
 




<div id="PostFetchComponent">
         

        <div class="container">
        
               <div class="card mt-4 w-75 p-3" v-for="post in posts" :key="post.id">

                    <div id ="big_mommy" style="text-align:left">
                        <div style="display: inline-block;">
                           
                            <img src="https://data.apksum.com/8d/com.tivola.myredpanda/1.1/icon.png" class="rounded-circle"  width="50" height="50" alt="avatar" />
                        </div>
                    
                        <div style="display: inline-block;">
                            <h5 class="mx-2 text-black" >{{authors[post.author].username}} </h5>
                         </div>
                    </div>


                
                
                   
                    
                    <div class="card-body">
                        <h6 class="card-title text-black" style="text-align:left">{{post.title}}</h6>

                            <p class="card-text  text-black mt-4" style="text-align:left">
                                {{post.content}}
                            </p>

        

                        <div class="row">
                            <div style="display: inline;">
                                <i data-toggle="tooltip" title="Lubię to!" @click="giveHearth(post)" v-if="hearthed[post.id] == false" class="far fa-heart" style="color:red"></i>
                                <i v-else class="fas fa-heart"   style="color:red"></i>
                                <p style="color:black; display: inline-block; padding: 3px;">{{post.hearts}}</p>
                            </div>

                            <div style="display: inline;">
                                <PostCommentFetchComponent v-bind:post_id="post.id" />
                            </div>
                        </div>
                    </div>
                </div>
        </div>
</div>

</template>

<script>

    import  PostCommentFetchComponent  from '@/components/Comments/PostCommentFetchComponent.vue';

export default {
 
    name:'PostFetchComponent',
     components: {
      PostCommentFetchComponent,

       
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
                    this.authors[post.author] = json;
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