<template>
  <div class = "login-container">
      <h1>Login</h1>
      <v-form
      ref="form"
      v-model="valid"
      @submit.prevent="login"
    >
      <v-text-field
        v-model="email"
        type="email"
        :rules="emailRules"
        label="Email"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        :rules="passwordRules"
        label="Password"
        required
        :append-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
        :type="passwordVisible ? 'text' : 'password'"
        @click:append="passwordVisible = !passwordVisible"
      ></v-text-field>

      <v-btn
        color="success"
        class="mr-4"
        :disabled="!valid"
        @click="login"
      >
        Login
      </v-btn>
      <v-btn
        color="success"
        class="mr-4"
        @click="oauth"
      >
        Sign in with OAuth
      </v-btn>
      <a class = "mr-4" href="/signup">Don't have an account?</a>
    </v-form>
  </div>
</template>

<script>
import api from "../api.js"
export default {
  name: 'Login',
  data: () => ({
    valid: true, 
    email: "", 
    password: "", 
    passwordVisible: false,
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
      ], 
    passwordRules: [v => !!v || "Password is required"],
  }), 
  methods: {
    login() {
      api.login(this.email, this.password, this.remember_me).then(() => {
        this.$router.push("/dashboard");
      })
    },
    oauth() {
      api.oauthGet()
    } 
  }
}
</script>

<style>
  .login-container {
    width: 50%; 
    margin-top: 10%;
    margin-left: 25%;
  }
</style>