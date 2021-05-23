<template>
        <!-- Comments -->
        <div class="col-12 p-0 pt-2 m-0 text-black">
            <div class="col-10 offset-1">
                <!-- User img and date -->
                <div class="d-flex p-0 m-0 bg-light rounded">
                    <div class="p-2 d-flex justify-content-center bg-danger rounded-start align-content-center">
                        <img class="p-0 m-0 align-self-center align-self-center rounded-circle  xsmall-img" src="@/assets/Pepe.jpg">
                    </div>
                    <div class="d-flex flex-column flex-fill text-start p-1 px-2">
                        <div class="d-flex justify-content-between">
                            <p class="p-0 m-0 text-start small-text">{{user}}</p>
                            <p class="p-0 m-0 text-start small-text text-decoration-underline">{{date}}</p>
                        </div>
                        {{content}}
                    </div>
                </div>
            </div>
        </div>
</template>

<script>

export default {
    name: 'CommentTemplate',
    props: ['user', 'content', 'date'],
    components: {
    },
    data(){
        return {
        }
    },
    methods: {
       }
    }

</script>

<style scoped>
.xsmall-img{
    width: 45px;
    height: 45px;
}

.small-text, .dim-text{
    font-size: 0.85em;
    /* text-decoration: underline dotted; */
}
.dim-text, .dim-text-underline{
    color: #ccc;
}
.dim-text-underline{
    text-decoration: underline;
}
h1{
    text-decoration: underline;
}
.hand:hover{
    cursor: pointer;
}
.active, .active-danger, .active-blue{
    transition: all 0.2s;
}
.active:hover{
    color: darkslateblue;
}
.active-danger:hover{
    color: tomato;
    }
.active-blue:hover{
    color: lightskyblue;
    }
</style>