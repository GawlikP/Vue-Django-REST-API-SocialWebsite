<template>
<div class="main-page">
    <div class="row col-lg-12 h-100">     
        <div class="col-lg-7 panda-bg">
           
        </div>     
        <div class="col-lg-5 d-flex align-items-center justify-content-center">        
        <MDBCol class="row col-lg-10 p-5 mw-600px">
            <AccountLogoutComponent />
        </MDBCol> 
        </div>
    </div>
</div>

</template>
<script>
import {   MDBCol   } from "mdb-vue-ui-kit";
import AccountLogoutComponent from '@/components/Accounts/AccountLogoutComponent'

export default ({
    name: 'Logout',
    setup() {
        
    },
    components:{
        
        MDBCol,
        AccountLogoutComponent
    },
    
})
</script>
<style lang="stylus" scoped>

</style>
