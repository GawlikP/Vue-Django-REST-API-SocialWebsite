
<template>
    <div id="TestComponent">
        <button class="btn btn-succes" @click="increment()">{{count}}</button>
    </div>
</template>
<script>

export default {
name: 'TestComponent',
  data: ()=> {
    return {
      count: 0
    }
  },
  methods: {
    increment () {
      this.count++;
    },
    decrement () {
      if(this.count > 0){
        this.count-- ;
      }
    }
  }
}
</script>
<style scoped>

</style>