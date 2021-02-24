<template>
    <div id="PostFetchComponent">
        <div class="container">
            
            <MDBCard v-for="post in posts" :key="post.id" style="text-align:left">
                <MDBCardBody>
                    <MDBCardTitle>{{post.title}}</MDBCardTitle>
                    <hr>
                    <MDBCardText>
                        {{post.content}}
                    </MDBCardText>
                   
                        <i  @click="giveHearth(post)" v-if="hearthed[post.id] == false" class="far fa-heart" style="color:red"></i>
                        <i v-else class="fas fa-heart" style="color:red"></i> 
                        {{post.hearts}}
                    
                </MDBCardBody>
                
            </MDBCard>
            
        </div>
    </div>
</template>
<script>
    import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText } from "mdb-vue-ui-kit";
    

export default {
 
    name:'PostFetchComponent',
     components: {
      MDBCard,
      MDBCardBody,
      MDBCardTitle,
      MDBCardText,
     // MDBBtn
    },
    data(){
        return {
            posts: [],
            hearthed: [],
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
            var response =  await fetch('http://localhost:8000/posts/');
            this.posts = await response.json()
            this.posts.forEach(post => {
                if(typeof this.hearthed[post.id] === 'undefined')this.hearthed[post.id] = false;
        });
           console.log(this.hearthed) 
        },
        async giveHearth(post){
            console.log(post);
            post.hearts +=1;

            this.hearthed[post.id] = true;
            var response = await fetch(`http://localhost:8000/posts/${post.id}/`, {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(post)
            });
            this.posts.push(await response.json());
           
            this.getPosts();
        }
    },

}
</script>
<style scoped>

</style>