<template>
  <div class="about">
    <h1>This is an about page</h1>
    <PostFetchComponent/>
  </div>
</template>

<script>
// @ is an alias to /src

import PostFetchComponent from '@/components/PostFetchComponent.vue'

export default {
  name: 'About',
  components: {
      PostFetchComponent
  }
}
</script>
