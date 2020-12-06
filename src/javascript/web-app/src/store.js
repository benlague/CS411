import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex);


const store = new Vuex.Store({
    state: {
        loggedIn: "unset", 
        snackbar: {
            message: "",
            show: false,
            color: "",
          }
    }, 
    mutations: {
        setLoggedInTrue(state) {
            state.loggedIn = true; 
        }, 
        setLoggedInFalse(state) {
            state.loggedIn = false; 
        }, 
        setSnackbar(state, snackbar) {
            state.snackbar.message = snackbar.message;
            state.snackbar.show = snackbar.show;
            state.snackbar.color = snackbar.color;
          }
    }, 
    getters: {
        isLoggedIn: (state) => {
            return state.loggedIn
        }
    }


})


export default store 