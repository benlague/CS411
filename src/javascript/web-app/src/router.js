import Vue from "vue" 
import Router from "vue-router"
import store from "./store"; 
import {tokenExists} from "./authentication"

Vue.use(Router)

const router = new Router({
    mode: "history", 
    routes: [
        {
            path: "/", 
            name: "Landing", 
            component: () => import("./views/Landing.vue"), 
            beforeEnter: (to, from, next) => redirectFromPublicRouteIfSignedIn(next)
        }, 
        {
            path: "/login", 
            name: "Login", 
            component: () => import("./views/Login.vue"), 
            beforeEnter: (to, from, next) => redirectFromPublicRouteIfSignedIn(next)
        }, 
        {
            path: "/signup", 
            name: "Signup", 
            component: () => import("./views/Signup.vue"), 
            beforeEnter: (to, from, next) => redirectFromPublicRouteIfSignedIn(next)
        }, 
        {
            path: "/dashboard", 
            name: "Dashboard", 
            component: () => import("./views/Dashboard.vue"), 
            meta: {
                requiresAuth: true
            }
        }
    ]
})


const verifyLoginAndRedirect = async (redirect, next) => {
    let isLoggedIn = store.getters.isLoggedIn; 
    if (isLoggedIn == "unset") {
        // check for the jwt 
        if (!tokenExists()) {
            store.commit("setLoggedInFalse"); 
            // if jwt doesn't exist, send user back to login screen
            redirect()
        }
        else {
            // add a route to server to check if the JWT is actually valid 
            store.commit("setLoggedInTrue");
            next();  
        }

    }
    else if (isLoggedIn == true) {
        next()
    }
    else {
        redirect()
    }

}


/*
If the user is signed in and attempts to access a public view, such as the homepage or login, redirect them to dashboard/.
Else, send them to their destination
*/
const redirectFromPublicRouteIfSignedIn = (next) => {
    const redirectToDashboard = () => next("dashboard");
    if (store.getters.isLoggedIn == true) {
      redirectToDashboard();
    } else if (store.getters.isLoggedIn == "unset") {
      verifyLoginAndRedirect(next, redirectToDashboard);
    } else {
      next();
    }
  };



router.beforeEach(async (to, from, next) => {
    const redirectToLogin = () => next({path: "/login", query: {redirect: to.fullPath}});
    if (to.matched.some(record => record.meta.requiresAuth)) {
    verifyLoginAndRedirect(redirectToLogin, next);
    } else {
    next();
    }
});

export default router 