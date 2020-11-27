<template>
  <div class = "login-container">
      <h1>Login</h1>
      <v-form
      ref="form"
      lazy-validation
    >
      <v-text-field
        v-model="email"
        :rules="[v => !!v || 'Email is required']"
        label="Email"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        :rules="[v => !!v || 'Password is required']"
        label="Password"
        required
      ></v-text-field>

      <v-checkbox
        v-model="remember_me"
        :rules="[v => !!v || 'You must agree to continue!']"
        label="Do you want us to remember you?"
        required
      ></v-checkbox>

      <v-btn
        color="success"
        class="mr-4"
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
    email: "", 
    password: "", 
    remember_me: false 
  }), 
  methods: {
    login() {
      api.login(this.email, this.password, this.remember_me).then(resp => {
        console.log(resp); 
        console.log("successfully logged in!")
      }).catch(err => {
        console.log(err); 
      })
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