import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex);


const initialState = {
    loggedIn: "unset", 
    snackbar: {
        message: "",
        show: false,
        color: "",
      }, 
      businesses: [], 
      headers: [], 
      businessName: "", 
      location: "", 
      loadingTable: false 
}

const store = new Vuex.Store({
    state: initialState, 
    mutations: {
        setLoggedIn(state, val) {
            state.loggedIn = val; 
        },  
        setSnackbar(state, snackbar) {
            state.snackbar.message = snackbar.message;
            state.snackbar.show = snackbar.show;
            state.snackbar.color = snackbar.color;
          }, 
        setBusinesses(state, businesses) {
            state.businesses = businesses
        }, 
        setHeaders(state, headers) {
            state.headers = headers; 
        }, 
        setBusinessName(state, name) {
            state.businessName = name; 
        }, 
        setLocation(state, location) {
            state.location = location; 
        }, 
        clearSearches(state) {
            state.businesses = [], 
            state.headers = [], 
            state.businessName = "", 
            state.location = "", 
            state.loadingTable = false 
        }, 
        setLoadingTable(state, val) {
            state.loadingTable = val;
        }

    }, 
    getters: {
        isLoggedIn: (state) => {
            return state.loggedIn
        }
    }


})


export default store 