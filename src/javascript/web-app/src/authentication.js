export function storeJWT(jwt) {
    localStorage.setItem("token", jwt); 
}


export function getJWT() {
    return localStorage.getItem("token"); 
}


export function deleteJWT() {
    localStorage.removeItem("token");
}



export function tokenExists() {
    return getJWT() ? true : false 
}