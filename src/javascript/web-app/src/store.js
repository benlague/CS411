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
        setLoggedIn(state, val) {
            state.loggedIn = val; 
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