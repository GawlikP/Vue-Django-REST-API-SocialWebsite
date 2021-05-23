<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8 justify-content-center ">
                
                <ProfileInfo 
                    :user=user 
                    :img=img 
                    :registered=registered 
                    :motto=motto 
                    :watchers=watchers 
                    :likes=likes 
                    :friends=friends />
                      
                <!-- POSTS COMPONENT -->
                <div class="row justify-content-center  ">
                    <div class="row bg-dark p-3 my-3 shadow rounded" v-for="post in posts" v-bind:key="post.id">
                        
                        <!-- Post author info & post actions -->
                        <div class="d-flex justify-content-between p-0 pb-2 m-0 border-bottom border-1">
                            
                            <!-- Info -->
                            <div class="d-flex flex-row">
                                <img class="p-0 m-0 rounded-circle align-self-center shadow xsmall-img" src="@/assets/Pepe.jpg">
                                <div class="d-flex flex-column justify-content-start p-0 ps-2 m-0">
                                    <div class="p-0 m-0 text-start text-decoration-underline">{{post.user}}</div>
                                    <p class="p-0 m-0 text-start small-text dim-text">Opublikowano: {{post.add_date}}</p>
                                </div>
                            </div>

                            <!-- Actions -->
                            <div class="d-flex flex-column p-0 m-0 justify-content-end text-end">
                                <div class="p-0 m-0 small-text dim-text hand active-danger" v-on:click="show_alert(1)">
                                    <i class="fas fa-pen p-1" data-toggle="tooltip"></i>
                                    Edytuj post</div>
                                <div class="p-0 m-0 small-text dim-text hand active-danger" v-on:click="show_alert(1)">
                                    <i class="fas fa-trash-alt p-1" data-toggle="tooltip"></i>
                                    Usuń post</div>
                            </div>
                        </div>
                        
                        <!-- Post -->
                        <div class="d-flex p-0 justify-content-between">
                            <h5 class="py-3 text-start align-self-center">
                                {{post.title}}
                            </h5>
                        </div>
                        <div class="col-12 ms-3">
                            <p class="col-12 p-0 m-0 text-start">{{post.content}}</p>
                        </div>
                        <!-- <router-link class="col-12 py-3 m-0 hand text-info" v-bind:key="post.link" v-bind:to="`${ post.link }`">
                                <i class="fas fa-comments px-1" data-toggle="tooltip"></i>
                                Wyświetl komentarze
                        </router-link> -->
                           
                        <!-- Likes/Comments -->
                        <div class="row p-1 m-0 mb-2 border-bottom border-1">
                            <div class="col-6 hand" v-on:click="show_alert(1)">
                                <i class="fas fa-heart px-1" data-toggle="tooltip"></i>
                                {{post.likes}}
                            </div>
                            <div class="col-6 hand" v-on:click="show_alert(1)">
                                <i class="fas fa-comments px-1" data-toggle="tooltip"></i>
                                Komentarze
                            </div>
                        </div>

                        <!-- Comments blocks -->
                        <CommentTemplate 
                            v-for="comment in post.comments" 
                            v-bind:key="comment.id" 
                            :user="comment.user" 
                            :content="comment.content" 
                            :date="comment.date"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import CommentTemplate from '@/components/Comments/CommentTemplate.vue'
import ProfileInfo from '@/components/Accounts/ProfileInfoTemplate.vue'

export default {
    name: 'ProfileAccountComponent',
    components: {
        CommentTemplate : CommentTemplate,
        ProfileInfo : ProfileInfo,
    },
    data(){
        return {
            img   : "Pepe.jpg",
            user  : "Pan Pepe",
            motto : "Cierpię cichutko żyjąc i żyję cichutko by cierpieć.",
            likes : 2137,
            friends  : 420,
            watchers : 666,
            registered : "Maj 2015",
            posts:[
                {id : 1,
                user : "Subnabu Malahati",
                add_date : "01/01/2021",
                likes : 4,
                title : "Code: JP2GMD",
                content: "Jan Paweł II Ganiał Małe Dinozury",
                comments : [{
                    id : 1,
                    user : "MadaQuaka",
                    date : "21/03/2021",
                    content : "Tak było. Nie kłamię."
                }]},
                {id : 2,
                user : "Henryk Majdan",
                add_date : "06/11/2020",
                likes : 12,
                title : "Czym jest Lorem Ipsum?",
                content: "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker",
                comments : [{
                    id : 1,
                    user : "Leeeevii",
                    date : "18/11/2020",
                    content : "Takie rzeczy to ja lubie : D."
                },
                {
                    id : 2,
                    user : "Keeeke",
                    date : "18/11/2020",
                    content : "Stary dobry Lorem. Pamiętam jak za czasów Hitlera pisaliśmy z chłopakami z SS w księgach spisowych bezsensowyny tekst. Coś tego typu właśnie."
                }]},
            ]
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