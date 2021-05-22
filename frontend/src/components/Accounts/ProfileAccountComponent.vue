<template>
    <div class="container mycontainer">
        <div class="row justify-content-center">
            <div class="col-md-8 justify-content-center mycol">
                <div class="row bg-danger shadow rounded myrow">
                    <img class="col-12 col-md-4 p-0 rounded-start" src="@/assets/Pepe.jpg">
                    <div class="col-md-8 p-3 mycol">
                        <div class="d-flex p-0 justify-content-start">
                            <h1 class="py-3 text-md-start align-self-center">
                                {{name}}
                                <i class="fas fa-pencil-alt p-2 small-icon hand active" data-toggle="tooltip" title="Edytuj profil" v-on:click="show_alert(1)"></i>
                            </h1>
                            
                        </div>
                        <div class="col-12 px-2">
                            <p class="col-md-12 m-0 text-start dim-text-underline"><i class="fas fa-user align-self-center px-1" data-toggle="tooltip" title="Edytuj profil"></i>Dołączył: {{registered}}</p>
                            <p class="col-md-12 pb-3 text-start">{{motto}}</p>
                            <div class="d-flex flex-row align-items-center p-0 m-0 small-text text-center text-start my-bg-info">
                                <div class="flex-fill px-0 py-1 m-0 align-self-center mycol">
                                    Obserwujący: {{watchers}}
                                </div>
                                <div class="flex-fill px-0 py-1 m-0 mx-2 align-self-center mycol">
                                    Polubień: {{likes}}
                                </div>
                                <div class="flex-fill px-0 py-1 m-0 align-self-center mycol">
                                    Znajomi: {{friends}}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
                <div class="row justify-content-center  myrow">
                    <div class="row bg-dark p-3 my-3 shadow rounded" v-for="post in posts" v-bind:key="post.id">
                        <div class="d-flex p-0 justify-content-start">
                            <h1 class="py-3 text-start align-self-center">
                                {{post.title}}
                                <i class="fas fa-pencil-alt p-2 small-icon hand active" data-toggle="tooltip" title="Edytuj post" v-on:click="show_alert(3)"></i>
                            </h1>
                            
                        </div>
                        <div class="col-12 ms-3">
                            <p class="col-12 p-0 m-0 text-start">{{post.content}}</p>
                        </div>
                        <div class="col-12 justify-content-center border-bottom border-1 pt-3">
                            <!-- <router-link class="col-12 py-3 m-0 hand text-info" v-bind:key="post.link" v-bind:to="`${ post.link }`">
                                    <i class="fas fa-comments px-1" data-toggle="tooltip"></i>
                                    Wyświetl komentarze
                            </router-link> -->
                            <div class="col-12 py-1 m-0 hand text-info" v-on:click="show_alert(2)">
                                    <i class="fas fa-comments px-1" data-toggle="tooltip"></i>
                                    Wyświetl komentarze
                            </div>
                        </div>
                        <div class="col-12">
                            <p class="col-12 pt-3 m-0 text-start small-text dim-text">Opublikowano: {{post.add_date}}</p>
                            <div class="col-3 p-0 m-0 text-start small-text dim-text hand active-danger" v-on:click="show_alert(4)">
                                <i class="fas fa-trash-alt p-2" data-toggle="tooltip"></i>
                                Usuń post</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ProfileAccountComponent',
    components: {
    },
    data(){
        return {
            name  : "Pan Pepe",
            motto : "Cierpię cichutko żyjąc i żyję cichutko by cierpieć.",
            likes : 2137,
            friends  : 420,
            watchers : 666,
            registered : "Maj 2015",
            posts:[
                {id : 1,
                add_date : "01/01/2021",
                link : "posts",
                title : "Code: JP2GMD",
                content: "Jan Paweł II Ganiał Małe Dinozury"},
                {id : 2,
                add_date : "06/11/2020",
                link : "posts",
                title : "Czym jest Lorem Ipsum?",
                content: "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"},
            ]
        }
    },
    methods: {
       show_alert: function (inv) {
           switch (inv) {
               case 1:
                    alert("TODO: Edycja danych użytkownika");
                   break;
               case 2:
                    alert("TODO: Sekcja komentarzy");
                   break;
               case 3:
                    alert("TODO: Edycja postów");
                   break;
               case 4:
                    alert("TODO: Usuwanie postu");
                   break;
           }
       }
    }

}
</script>

<style scoped>
.mycontainer{
    /* border: solid 2px #0f0; */
}
.mycol{
    /* border: solid 2px #f00; */
}
.myrow{
    /* border: solid 2px #00f; */
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
.small-icon{
    font-size: 0.7em;
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
.fg-title{
    color: darkslateblue;
}
.none-decorated{
    text-decoration: none;
}
</style>