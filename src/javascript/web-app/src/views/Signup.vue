<template>
  <div class = "signup-container">
      <h1>Signup</h1>
      <v-form
      ref="form"
      lazy-validation
    >
    <v-text-field
        v-model="first_name"
        :rules="[v => !!v || 'First name is required']"
        label="First Name"
        required
      ></v-text-field>    
      <v-text-field
        v-model="last_name"
        :rules="[v => !!v || 'Last name is required']"
        label="Last Name"
        required
      ></v-text-field>
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

      <v-text-field
        v-model="confirmPassword"
        :rules="[v => !!v || 'Confirmed password is required!']"
        label="Confirm Password"
        required
      ></v-text-field>

      <v-btn
        color="success"
        class="mr-4"
        @click="signup"
      >
        Signup
      </v-btn>

    </v-form>
  </div>
</template>

<script>
import api from "../api"; 
export default {
  name: 'Signup',
  data: () => ({
    first_name: "", 
    last_name: "", 
    email: "", 
    password: "", 
    confirmPassword: ""
  }), 
  methods: {
    signup(){
      api.signup(this.first_name, this.last_name, this.email, this.password, this.confirmPassword).then(() => {
        console.log("sucessfully signed up"); 
      }).catch(err => { 
        console.log(err); 
      })
    }
  }
}
</script>

<style>
  .signup-container {
    width: 50%; 
    margin-top: 10%;
    margin-left: 25%;
  }
</style>