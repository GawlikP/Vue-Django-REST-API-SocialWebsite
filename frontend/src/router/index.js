import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Posts from '../views/Posts.vue'
import Registration from '../views/Registration.vue'
import Login from '../views/Login.vue'
import Profiles from '../views/Profiles.vue'
import Profile from '../views/Profile.vue'
import Logout from '../views/Logout.vue'
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
        path: '/registration',
        name: 'Registration',
        component: Registration
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/logout',
        name: 'Logout',
        component: Logout
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile
    },

    {
        path: '/profiles/:id',
        name: 'Profiles',
        component: Profiles
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router