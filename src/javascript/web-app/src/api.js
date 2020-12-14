import axios from 'axios'
import store from "./store"; 
import router from "./router"; 
import {storeJWT, getJWT, tokenExists, deleteJWT} from "./authentication"
import notify from "./utilities/notify"; 

const defaultRequestConfig = {
    headers: {
      "content-type": "application/x-www-form-urlencoded",
    },
    withCredentials: true,
};

const serverUrl = "http://localhost:8001"


function urlEncode(data) {
    var urlEncodedString = "";
    Object.keys(data).forEach(function(key) {
        urlEncodedString += key + "=" + encodeURIComponent(data[key]) + "&";
    });
    return urlEncodedString.slice(0, -1); //remove the trailing '&'
}

function logoutHelper(unauthorized) {
    deleteJWT()
    store.commit("setLoggedIn", false); 
    store.commit("clearSearches")
    // conditional checks whether we are logging out because of lack of unauthorization, if so, redirect to login and show error message
    if (unauthorized) {
        notify("Please log in again!", "red"); 
        router.push("/login"); 
    }
    else {
        notify("Successfully logged out!", "green"); 
        router.push("/"); 
    }
}

const api = {
    login(email, password, remember_me) {
        return new Promise((resolve, reject) => {
                const payload = urlEncode({ email, password, remember_me})
                axios.post(`${serverUrl}/api/auth/login`, payload, defaultRequestConfig).then(response => {
                    // handle successful login 
                    store.commit("setLoggedIn", true); 
                    storeJWT(response.data["access_token"]); 
                    notify("Successfully logged in!", "green"); 
                    resolve(); 
                }).catch(err => {
                    // handle error, add a snackbar? 
                    notify(err.response.data.message, "red")
                    reject(); 
                })
        })
    }, 
    signup(first_name, last_name, email, password) {
        return new Promise((resolve, reject) => {
            const payload = urlEncode({ first_name, last_name, email, password })
            axios.post(`${serverUrl}/api/auth/register`, payload, defaultRequestConfig).then(() => {
                notify("Successfully logged in!", "green"); 
                resolve(); 
            }).catch(err => {
                notify(err.response.data.message, "red"); 
                reject(); 
            })
        })
    },
    search(name, location) {
        return new Promise((resolve, reject) => {
            // check if jwt exists 
            if (tokenExists()) {
                axios.get(`${serverUrl}/api/yelp`, {params: {name,location}, headers: {"Authorization": "Bearer " + getJWT()}}).then(resp => {
                    console.log(resp); 
                    resolve(resp.data.businesses)
                }).catch(err => {
                    // check for unauthorized status code or signature validation failure 
                    if (err.response.status == 401 || err.response.status == 422) {
                        logoutHelper(true); 
                    }
                    reject(err); 
                })
            }
            else {
                logoutHelper(true); 
            }
        })
    },
    forecast(name, location) {
        return new Promise((resolve, reject) => {
            // check if jwt exists 
            if (tokenExists()) {
                axios.get(`${serverUrl}/api/besttime`, {params: {name,location}, headers: {"Authorization": "Bearer " + getJWT()}}).then(resp => {
                    console.log(resp); 
                    resolve(resp.data.today_forecast)
                }).catch(err => {
                    // check for unauthorized status code or signature validation failure 
                    if (err.response.status == 401 || err.response.status == 422) {
                        logoutHelper(true); 
                    }
                    reject(err); 
                })
            }
            else {
                logoutHelper(true); 
            }
        })
    }, 
    oauthGet(){
        window.location.href = `${serverUrl}/api/auth/oauth/login`
    }, 
    logout(){
        logoutHelper(false); 
    }
}
export default api; 