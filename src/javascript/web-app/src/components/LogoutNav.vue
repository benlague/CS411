<template>
    <v-toolbar flat color="transparent" fixed="top">
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
    methods: {
        logout() {
            api.logout()
        }
    }
}
</script>