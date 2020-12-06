import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex);


const store = new Vuex.Store({
    state: {
        loggedIn: "unset" 
    }, 
    mutations: {
        setLoggedInTrue(state) {
            state.loggedIn = true; 
        }, 
        setLoggedInFalse(state) {
            state.loggedIn = false; 
        }
    }, 
    getters: {
        isLoggedIn: (state) => {
            return state.loggedIn
        }
    }


})


export default store 