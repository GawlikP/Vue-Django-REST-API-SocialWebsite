<template>


  <div class="d-grid gap-4 col-12 mx-auto">

      
      <h5>Sortuj</h5>
    <MDBBtn size="md" outline="danger" rounded>polubienia</MDBBtn>
    <MDBBtn size="md"  outline="danger" rounded>komentarze</MDBBtn>
    
  </div>
</template>
<script>
import { MDBBtn } from "mdb-vue-ui-kit";

  export default {
    components: {
      MDBBtn
    }
  };

</script>
<style scoped>




.btn-danger:hover, .btn-outline-danger:hover{
  
  border-color: rgb(255, 255, 255);
  color: white;
}



</style>
