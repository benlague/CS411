import axios from 'axios'

const defaultRequestConfig = {
    headers: {
      "content-type": "application/x-www-form-urlencoded",
    },
    withCredentials: true
  };


function urlEncode(data) {
    var urlEncodedString = "";
    Object.keys(data).forEach(function(key) {
        urlEncodedString += key + "=" + encodeURIComponent(data[key]) + "&";
    });
    return urlEncodedString.slice(0, -1); //remove the trailing '&'
}

const api = {
    login(email, password, remember_me) {
        return new Promise((resolve, reject) => {
                const payload = urlEncode({ email, password, remember_me})
                axios.post("/api/auth/login", payload, defaultRequestConfig).then(() => {
                    // handle succesful login 
                    resolve("Successfully logged in!")
                }).catch(err => {
                    // handle error, add a snackbar? 
                    reject(err.response.data.message); 
                })
        })
    }, 
    signup(first_name, last_name, email, password) {
        return new Promise((resolve, reject) => {
            const payload = urlEncode({ first_name, last_name, email, password })
            axios.post('/api/auth/register', payload).then(() => {
                resolve("Succesfully signed up!")

            }).catch(err => {
                reject(err.response.data.message); 
            })
        })
    },
    search(name, location) {
        return new Promise((resolve, reject) => {
            axios.get("/api/yelp", {params: {name,location}}, defaultRequestConfig).then(() => {
                resolve()
        }).catch(err => {
            reject(err); 
        })
    })
    }
}
export default api; 