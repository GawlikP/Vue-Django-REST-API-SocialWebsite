import 'mdb-vue-ui-kit/css/mdb.min.css'
import { createApp } from 'vue'
import App from './App.vue'
import 'mdb-vue-ui-kit/css/mdb.min.css'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueSessionStorage from 'vue-sessionstorage'
const app = createApp(App)
app.use(VueAxios, axios)
app.use(router)
app.mount('#app')
app.use(VueSessionStorage)
    //createApp(App).use(VueSession).use(router).mount('#app')