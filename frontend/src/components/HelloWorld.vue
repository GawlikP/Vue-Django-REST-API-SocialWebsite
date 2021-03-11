<template>
<div class="main-page">
  <div class="row col-lg-12 h-100">     
    <div class="col-lg-8 panda-bg">
        <!-- <img src="../assets/redpanda.jpg" class="img-responsive" alt="panda"> -->
    </div>     
    <div class="col-lg-4 d-flex align-items-center justify-content-center">        
      <div class="row col-lg-12 p-5">
        <h1 class="text-start">Dołącz do pandastycznej społeczności!</h1>
        <MDBBtn color="danger" rounded size="lg" class="mb-2">Zarejestruj się</MDBBtn>           
        <MDBBtn outline="danger" rounded  size="lg">Zaloguj się</MDBBtn>       
      </div>     
    </div>   
  </div> 
  </div> 
</template>

<script>
import { MDBBtn } from "mdb-vue-ui-kit";


export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  
  components:{
    MDBBtn
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

</style>
