<template>
    <div  >
        <form @submit.prevent="createPost">

            <div >
                <h2><i class="fas fa-angry" v-if="posted == 1" style="color:red"></i>
                <i class="fas fa-smile" v-if="posted == -1" style="color:green"></i> </h2>
                <div v-if="posted == 1">
                <MDBBadge  color="danger" v-for="(error, index) in errors" :key="error.id">
                    <b>{{index}} </b>: {{error[0]}}
                    
                </MDBBadge>
                </div>
            </div>
            <br>
            <div class="d-grid gap-2 col-3 mx-auto">
            <MDBInput label="Tytył Postu" white size="lg" v-model="post.title" />
            <br>
            <MDBInput label="Treść Postu" white size="lg" v-model="post.content" />
            <br>
           
             <MDBBtn color="secondary" type="submit" size="lg" rounded>Dodaj</MDBBtn>  
            </div>
                <br>
            

            <hr>
    </form>
    </div>
</template>
<script>
import { MDBInput, MDBBtn, MDBBadge } from 'mdb-vue-ui-kit';


export default {
    name: 'NewPostCommentFormComponent',
    components: {
      MDBInput,
      MDBBtn,
        MDBBadge,  
    },
    data(){
        return {
        post: {
            ''
        },
    },
    setup() {
        
    },
}
</script>
<style scoped>

</style>
