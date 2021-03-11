<template>

<MDBContainer fluid>
  <MDBRow class="mb-3">
    <MDBCol col="13" md="7" offsetLg="0" ><img src="../assets/panda.jpg" class="img-fluid" alt="panda" ></MDBCol>
    <MDBCol col="11" md="4"> 
  
      <MDBRow class="mb-3">  
        
      
        <p class="text-start " style="font-size: 350%;"><strong>Dołącz do pandastycznej społeczności!</strong></p>
        <br>
        <br>
        <p class="text-start " style="font-size: 170%;"><strong>Zostań pandą już dzisiaj.</strong></p>
      </MDBRow>
       
        <MDBBtn tag="a" color="danger" rounded size="lg" href="/accounts" style="width:70%;" ><strong>Zarejestruj się</strong></MDBBtn>
        
    
 
          <br>
          <br>
        <MDBBtn tag="a" outline="danger" rounded  size="lg" href="/login" style="width:70%;"><strong>Zaloguj się</strong></MDBBtn>
      
    </MDBCol>
  </MDBRow>
</MDBContainer>    
 
</template>

<script>


import {  MDBBtn,MDBCol, MDBRow,MDBContainer  } from "mdb-vue-ui-kit";


export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  
  components:{
      MDBBtn,
      MDBCol,
      MDBRow,
      MDBContainer 
    
  }
};

  

  
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
