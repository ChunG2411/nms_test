import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'
import Product from '../views/Product.vue'


const routes = [
    {
        name: "home",
        path: "/",
        component: Home
    },
    {
        name: "product",
        path: "/:id",
        component: Product
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router