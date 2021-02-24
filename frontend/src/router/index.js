import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Posts from '../views/Posts.vue'
import Accounts from '../views/Accounts.vue'
const routes = [{
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        component: About
    },
    {
        path: '/posts',
        name: 'Posts',
        component: Posts
    },
    {
        path: '/accounts',
        name: 'Accounts',
        component: Accounts
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router