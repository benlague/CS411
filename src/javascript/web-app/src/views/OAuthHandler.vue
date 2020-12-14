<template>
<div></div>
</template>

<script>
import { storeJWT } from '../authentication';
import store from '../store';

export default {
    name: "OAuthHandler",
    mounted() {
        const access_token = this.$route.query.access_token;
         store.commit("setLoggedIn", true); 
         storeJWT(access_token);
         this.$router.push("/dashboard");
    }
}
</script>

<style>
</style>