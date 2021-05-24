<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <center>
          <PostFormComponent />
        </center>
      </div>
    </div>

    <div class="row">

      <div class="col-sm-2 mt-2">
        <PostFilter />
      </div>

      <div class="col-sm-8 mb-2">
        <PostFetchComponent />
      </div>

      <div class="col-sm-2 ">
      <FollowersFetchComponent/>
    
      </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import PostFetchComponent from "@/components/Posts/PostFetchComponent.vue";
import PostFormComponent from "@/components/Posts/PostFormComponent.vue";
import PostFilter from "@/components/Posts/PostFilter.vue";
import FollowersFetchComponent from "@/components/Followers/FollowersFetchComponent.vue";

//import LoadingComponent from "@/components/utility/LoadingComponent.vue";
//import ErrorComponent from "@/components/utility/ErrorComponent.vue";

/*const PostFetch = ()  => ({
  component: import("@/components/Posts/PostFetchComponent.vue"),
  loading: LoadingComponent,
  eroror: ErrorComponent,
  timeout: 30
})*/

export default {
  name: "Posts",
  components: {
    //PostFetch,
    PostFetchComponent,
    PostFormComponent,
    PostFilter,
    FollowersFetchComponent,
  },
  data() {
    return {
      username: "",
    };
  },
  created() {
    if (window.sessionStorage.getItem("username")) {
      this.username = window.sessionStorage.getItem("username");
    }
  },
};
</script>