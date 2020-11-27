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
            if (email.length > 0 && password.length > 0) {
                const payload = urlEncode({ email, password, remember_me})
                axios.post("/api/auth/login", payload, defaultRequestConfig).then(() => {
                    // handle succesful login 
                    resolve("Successfully logged in!")
                }).catch(err => {
                    // handle error, add a snackbar? 
                    reject(err.response.data.message); 
                })
            }
            else {
                reject("Email and password must be filled out!")
            }
        })
    }, 
    signup(first_name, last_name, email, password, confirmPassword) {
        return new Promise((resolve, reject) => {
            if (password != confirmPassword) {
                reject("Password and Confirm Password must match"); 
            }
            if (first_name.length == 0 || last_name.length == 0 || email.length == 0 || password.length == 0 || confirmPassword.length == 0 ) {
                reject("All form fields must be filled out!")
            }
            const payload = urlEncode({ first_name, last_name, email, password })
            axios.post('/api/auth/register', payload).then(() => {
                resolve("Succesfully signed up!")

            }).catch(err => {
                reject(err.response.data.message); 
            })
        })
    }
}

export default api; 