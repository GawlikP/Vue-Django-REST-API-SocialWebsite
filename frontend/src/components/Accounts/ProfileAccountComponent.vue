<template>
<div class="flex">
    <div class="hflex wi">
        <img class="profile-img" src="@/assets/Pepe.jpg">
        <div class="vflex wi">
            <div class="hflex flex-header">
                <h3>Pepe Pan Porażka</h3>
                <button class="btn btn-light">edytuj profil</button>
            </div>
            <div class="vflex flex-body">
                <div class="time">
                    Joined may 2015
                </div>
                <div class="opis">
                    Krwawie cicho żyjonc, żyje cicho krwawionc...🤡
                </div>
                <div class="hflex">
                    <div>666 Obserwujących</div>
                    <div>2137 polubień</div>
                    <div>420 znajomych</div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="hflex wi mt">
        <div class="vflex-autor m10 totop">
            <img class="post-img" src="@/assets/Pepe.jpg">
            <div>23h ago</div>
            <button class="btn btn-primary">Edytuj</button>
            <button class="btn btn-danger">Usuń</button>
        </div>
        <div class="vflex-post wi left m10">
            <h4>Mr. Peperson</h4>
            <div>Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker</div>
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
            posts:[
            ]
        }
    },
    methods: {
       
    }

}
</script>
<style scoped>
.profile-img{
    width: 250px;
    height: auto;
    border-radius: 15% 0% 0% 15%;
}
.post-img{
    width: 100px;
}
.flex{
    display: flex;
    flex-direction: column;
    align-items: center;
    /* width: 100%; */
}
.hflex{
    display: flex;
    flex-direction: row;
    justify-content: center;
}
.vflex{
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-direction: column;
    background-color: lightcoral;
}
.vflex-post{
    display: flex;
    flex-direction: row;
    justify-content: start;
    flex-direction: column;
    background-color: #99394ac1;
    padding: 15px 30px;
}
.vflex-post-button{
    display: flex;
    flex-direction: row;
    justify-content: start;
    flex-direction: column;
    background-color: rgb(47, 79, 61);
    /* padding: 15px 30px; */
}
.vflex-autor{
    display: flex;
    flex-direction: row;
    justify-content: start;
    flex-direction: column;
}
.vflex div{
    padding: 10px;
    justify-content: space-between;
}

.time{
    font-size: 0.8em;
    color: #555;
}
.flex-body * {
     text-align: left;
}
.opis{
    background-color: #99394ac1;
    color: black;
    font-family:Arial, Helvetica, sans-serif;
    font-weight: bold;
    padding: 20px 15px !important;
}
.shadow{
    box-shadow: 2px 2px 5px rgba(0,0,0,0.5);
}

.wi{width:70%;}

.left *{
    text-align: left;
}
.m10{
    margin-right: 10px;
}
.mt{
    margin-top: 20px;
}

</style>