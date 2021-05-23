<template>
   
    <div id="acc-profile">
    <ProfileAccountComponent v-bind:id="id" />
 
    {{id}}
    </div>
    
</template>

<script>
// @ is an alias to /src
import ProfileAccountComponent from '@/components/Profile/ProfileAccountComponent.vue'

export default {
  name: 'Profile',
  components: {
    ProfileAccountComponent,
  },
  
  data(){
        return {
            id: '',

            
        }
    },
    async created(){
        this.id = this.$route.params.id
    },
    
    methods:{
        async getID(){

        }
      
    },
}
</script>

<style scoped>

</style>
