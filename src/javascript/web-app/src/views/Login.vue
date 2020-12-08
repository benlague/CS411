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

      <v-checkbox
        v-model="remember_me"
        label="Do you want us to remember you?"
      ></v-checkbox>

      <v-btn
        color="success"
        class="mr-4"
        :disabled="!valid"
        @click="login"
      >
        Login
      </v-btn>
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
    remember_me: false,
    passwordVisible: false,
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
      ], 
    passwordRules: [v => !!v || "Password is required"],
    rememberRules: [v => !!v || 'You must agree to continue!']


  }), 
  methods: {
    login() {
      api.login(this.email, this.password, this.remember_me).then(() => {
        this.$router.push("/dashboard");
      })
    }, 
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