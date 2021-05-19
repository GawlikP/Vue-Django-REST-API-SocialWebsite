<template>

    
 




<div id="PostFetchComponent">
         

        <div class="container">
         <div id="loading" v-if="loading==true">
                        <h1> Loading... </h1>
        </div>
        <div v-else>
               <div class="card mt-4 w-75 p-3" v-for="post in posts" :key="post.id">

                   
                    
                        <div id ="big_mommy" style="text-align:left">
                            <div style="display: inline-block;">
                            
                                <img src="https://data.apksum.com/8d/com.tivola.myredpanda/1.1/icon.png" class="rounded-circle"  width="50" height="50"  @click="goTo(`/profile/${profiles[authors[post.author].id].id}`)" alt="avatar" />
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
                                    <i data-toggle="tooltip" title="Lubię to!" @click="giveHearth(post)"  class="far fa-heart" style="color:red"></i>
                            
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
            profiles: [],
            hearts: [],
            loading: true,
        }
    },
    async beforeMount() {
         try {
            this.loading = true;
            await this.getPosts()
            await this.posts.forEach(post => {
                this.hearthed[post.id] = false;
            })
            await this.authors.forEach(author => {
                 this.getProfile(author)
            });
     
      this.loading= false;
      // success
    } catch (error) {
      console.log(error)
    }
         
        
        
        
        // this.loading = false;
    },
    
    
    methods:{
        getProfile(account){
            var token =  window.sessionStorage.getItem('token');

          const headers = {
              'Authorization': `Token ${token}`,
              'Accept': 'application/json',
              'Content-Type': 'application/json'
          }

          return this.axios.get(`http://localhost:8000/accounts/${account.id}/profile/`, {headers: headers, validateStatus: function (status) {
      return status >= 200 && status < 500
    }})
            .then(response =>{
                if(response.status == 200){
                   
                    this.profiles[account.id] = response.data
                    return this.profiles
                }
                else {
                  console.log(response)
                }
            } );
        },
        goTo(path){
      this.$router.push(path);
       
    },
        async getHearts(){
            var token = await window.sessionStorage.getItem('token')
                    
                    const headers = {
                        
                            'Authorization': `Token ${token}`,
                            'Accept': 'application/json',
                            'Content-Type': 'application/json' 
                    }

                 return this.axios.get(`http://localhost:8000/hearts/`, {headers: headers}).then(response => {
               

                this.hearts = response.data
                

            })
        },
        async getPosts(){
            this.loading = true;
            var token = await window.sessionStorage.getItem('token')
                    
                    const headers = {
                        
                            'Authorization': `Token ${token}`,
                            'Accept': 'application/json',
                            'Content-Type': 'application/json' 
                    }
            var response =  await fetch('http://localhost:8000/posts/', {headers: headers});
            this.posts = await response.json()
           
            for await(const post of this.posts){
                    this.setAuthors(post, headers);
                }
 
            await this.getHearts().then(response => {
                for (const post of this.posts){
                    console.log(response);
                post.hearts = 0;
                this.hearts.forEach( heart =>{
                    if(post.id == heart.post){
                    post.hearts++;
                }
                });
                
            }
            }).then(response => {
                console.log(response);
                for  (const author of this.authors){
                this.getProfile(author).then(response => {
                        console.log(response, "skonczylem")
                });
            }
            });
            

           
          await  console.log("skonczylem")
            //this.loading = false;
        },
        async setAuthors(post, headers){
                
                    
                   
            
            var response = await fetch(`http://localhost:8000/accounts/${post.author}`, {headers: headers});
                    var json = await response.json();
                    this.authors[post.author] = json;
        },
        async giveHearth(post){
            
            
          //  var postr = post;
            
           

            var token = await window.sessionStorage.getItem('token')
                    
                    const headers = {
                        
                            'Authorization': `Token ${token}`,
                            'Accept': 'application/json',
                            'Content-Type': 'application/json' 
                    }
                    var data = {'post' : `${post.id}`}
            this.hearthed[post.id] = true;
            var response = await fetch(`http://localhost:8000/hearts/`, {
                method: 'post',
                headers: headers,
                body: JSON.stringify(data)
            });
            var res = await response;
            if(res.status == 406){
                alert('Nie mozesz znow polubic tego samego posta!')
            }else {
                post.hearts +=1;
            }
            return res
            //this.getPosts();
        }
    },
    
   
}
</script>
<style scoped>
tr,hr {
color: white;
}
</style>