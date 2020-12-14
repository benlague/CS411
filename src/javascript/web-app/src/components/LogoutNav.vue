<template>
    <v-toolbar flat color="transparent" fixed="top">
        <v-btn v-if="showBackArrow" @click="goBack">
            <v-icon dark right>mdi-arrow-left</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
        <v-toolbar-items>
        <v-btn text tile color="#000000" @click="logout">Logout</v-btn>
        </v-toolbar-items>
    </v-toolbar>
</template>

<script>
import api from "../api.js"; 
export default {
    name: "LogoutNav", 
    props: ["showBackArrow"], 
    methods: {
        logout() {
            api.logout()
        }, 
        goBack() {
            // goes to previous route
            this.$router.go(-1); 
        }
    }
}
</script>