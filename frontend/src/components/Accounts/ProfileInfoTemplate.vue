<template>
    <!-- USER BAR COMPONENT -->
    <div class="row mb-2 bg-danger shadow rounded ">
        
        <!-- User img -->
        <img class="col-12 col-md-4 p-0 rounded-start" src="@/assets/Pepe.jpg">
        
        <!-- User info -->
        <div class="col-md-8 p-3 ">
            <!-- User name -->
            <div class="d-flex p-0 justify-content-start">
                <h1 class="py-3 text-md-start align-self-center">
                    {{user}}
                    <i class="fas fa-pencil-alt p-2 small-icon hand active" data-toggle="tooltip" title="Edytuj profil" v-on:click="show_alert()"></i>
                </h1>
            </div>

            <!-- User data -->
            <div class="col-12 px-2">
                <p class="col-md-12 m-0 text-start dim-text-underline"><i class="fas fa-user align-self-center px-1" data-toggle="tooltip" title="Edytuj profil"></i>Dołączył: {{registered}}</p>
                <p class="col-md-12 pb-3 text-start">{{motto}}</p>
                <div class="d-flex flex-row align-items-center p-0 m-0 small-text text-center text-start my-bg-info">
                    <div class="flex-fill px-0 py-1 m-0 align-self-center ">
                        Obserwujący: {{watchers}}
                    </div>
                    <div class="flex-fill px-0 py-1 m-0 mx-2 align-self-center ">
                        Polubień: {{likes}}
                    </div>
                    <div class="flex-fill px-0 py-1 m-0 align-self-center ">
                        Znajomi: {{friends}}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ProfileInfo',
    props: ['user', 'img', 'registered', 'motto', 'watchers', 'likes', 'friends'],
    components: {
    },
    data(){
        return {
        }
    },
    methods: {
       show_alert: function () {
            alert("TODO: Funkcjonalność do stworzenia");
       }
    }

}
</script>

<style scoped>
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
.small-icon{
    font-size: 0.65em;
}
.hand:hover{
    cursor: pointer;
}
.my-bg-info *{
    background-color: darkslateblue;
    color: #ddd;
    border-radius: 5px;
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