<template>
<div class="main-page">
  <div class="row col-lg-12 h-100">     
    <div class="col-lg-7 panda-bg">
        <!-- <img src="../assets/redpanda.jpg" class="img-responsive" alt="panda"> -->
    </div>     
    <div class="col-lg-5 d-flex align-items-center justify-content-center">        
      <MDBCol class="row col-lg-10 p-5 mw-600px">
        <h1 class="text-start font-weight-bold mb-4">Dołącz do pandastycznej społeczności!</h1>
        <h4 class="text-start font-weight-lighter mb-3">Zostań pandą już dziś!</h4>
        <MDBBtn color="danger" @click="goTo('\accounts')" rounded size="lg" class="mb-2">Zarejestruj się</MDBBtn>           
        <MDBBtn outline="danger" @click="goTo('\login')" rounded  size="lg">Zaloguj się</MDBBtn>       
      </MDBCol>     
    </div>   
  </div> 
  </div> 
</template>

<script>
import {  MDBBtn, MDBCol   } from "mdb-vue-ui-kit";

export default {
  name: 'Home',
  props: {
    msg: String
  },
  
  components:{
    MDBBtn,
    MDBCol
  },

  methods:{
    goTo(path){
      this.$router.push(path);
       
    }
  },
  created(){
     
  }
};

  
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main-page{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.panda-bg{
  background-image: url("../assets/redpanda.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  min-height: 40vh;
}

.btn-danger:hover, .btn-outline-danger:hover{
  background-color: rgb(77, 170, 165);
  border-color: plum;
  color: white;
}
.mw-600px{
  max-width: 600px;
}
</style>
