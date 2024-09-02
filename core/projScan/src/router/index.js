import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../components/LogIn.vue'
import Dashboard from '../components/HelloWorld.vue'
import Inspect from '../components/Inspect.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/dashboard',
        name: 'MainDashboard',
        component: Dashboard
    },
    {
        path: '/inspect/:id',
        name: 'Inspect',
        component: Inspect,
        props:true
    }

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})


export default router
