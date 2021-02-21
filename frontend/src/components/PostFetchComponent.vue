<template>
    <div>
        <div class="container">
            
            <table class="table">
                    <thead>
                        <th> Title </th>
                        <th> Content </th>
                    </thead>
                    <tbody>
                        <tr v-for="post in posts" :key="post.id">
                            <td>{{post.title}} </td>
                            <td>{{post.content}}</td>
                            
                        </tr>
                    </tbody>
            </table>
        </div>
    </div>
</template>
<script>
export default {
    name:'PostFetchComponent',
    data(){
        return {
            posts: [],
        }
    },
    async created(){
        this.getPosts()
    },
    
    methods:{
        async getPosts(){
            var response =  await fetch('http://localhost:8000/posts/');
            this.posts = await response.json()
        }
    },

}
</script>
<style scoped>

</style>