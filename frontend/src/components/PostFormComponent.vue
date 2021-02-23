<template>
    <div  >
        <form @submit.prevent="createPost">
            <MDBInput label="Post Title" size="lg" v-model="post.title" />
            <MDBInput label="Post Content" size="lg" v-model="post.content" />
   
             <MDBBtn color="secondary" type="submit">Secondary</MDBBtn>
    </form>
    </div>

</template>

<script>

import { MDBInput, MDBBtn } from 'mdb-vue-ui-kit';

export default {
    name: 'PostFormComponent',

     components: {
      MDBInput,
      MDBBtn
    },

    data(){
        return {
            post: {
                'title': '',
                'content': ''
            },
            
        }
    },
    methods:{
         async createPost(){
             var response  = await fetch('http://localhost:8000/posts/',{
                 method: 'post',
                 headers: {
                     'Content-Type': 'application/json'
                 },
                 body: JSON.stringify(this.post)
             });

             console.log(await response);
         }
    },

}
</script>
<style scoped>

</style>