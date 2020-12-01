<template>
        <div class = "main-container">
                <v-toolbar flat color="transparent" fixed="top">
                    <v-spacer></v-spacer>
                    <v-toolbar-items>
                    <v-btn text tile color="#000000" @click="signup">Sign Up</v-btn>
                    <v-btn text tile color="#000000" @click="login">Sign In</v-btn>
                    </v-toolbar-items>
                </v-toolbar>
                <div class = "title">
                    <p>Title Here</p>
                </div>
        </div>
</template>

<script>
export default {
    name: "Landing", 
    methods: {
        login() {
            this.$router.push("Login")
        }, 
        signup() {
            this.$router.push("Signup")
        }
    }
}
</script>

<style>
    .main-container {
        background: url("../assets/landing-banner.jpeg") no-repeat center center fixed;
        height: 100%;
        overflow: auto; 
        width:100%;
        margin:0;
        padding:0;
    }
    .title {
          margin: 0 auto;
    }
</style>