import store from "../store"; 


const notify = (message, color) => {
    store.commit("setSnackbar", {message: message, color: color, show: true});
    
}

export default notify; 