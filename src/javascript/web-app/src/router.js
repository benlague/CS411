import Vue from "vue" 
import Router from "vue-router"

Vue.use(Router)

const router = new Router({
    mode: "history", 
    routes: [
        {
            path: "/", 
            name: "Landing", 
            component: () => import("./views/Landing.vue")
        }, 
        {
            path: "/login", 
            name: "Login", 
            component: () => import("./views/Login.vue")
        }, 
        {
            path: "/signup", 
            name: "Signup", 
            component: () => import("./views/Signup.vue")
        }, 
        {
            path: "/dashboard", 
            name: "Dashboard", 
            component: () => import("./views/Dashboard.vue") 
        }
    ]
})

export default router 