<template>
  <div class = "signup-container">
      <h1>Signup</h1>
      <v-form
      ref="form"
      lazy-validation
    >
    <v-text-field
        v-model="first_name"
        :rules="firstNameRules"
        label="First Name"
        required
      ></v-text-field>    
      <v-text-field
        v-model="last_name"
        :rules="lastNameRules"
        label="Last Name"
        required
      ></v-text-field>
      <v-text-field
        v-model="email"
        :rules="emailRules"
        label="Email"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        label="Password"
        :append-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
        :type="passwordVisible ? 'text' : 'password'"
        @click:append="passwordVisible = !passwordVisible"
        :rules="passwordRules"
        required
      ></v-text-field>

      <v-text-field
        v-model="confirmPassword"
        label="Confirm Password"
        :append-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
        :type="passwordVisible ? 'text' : 'password'"
        :rules="confirmPasswordRules.concat(passwordConfirmationRule)"
        @click:append="passwordVisible = !passwordVisible"
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
    confirmPassword: "", 
    passwordVisible: false,
    firstNameRules: [v => !!v || "First name is required"], 
    lastNameRules: [v => !!v || "Last name is required"], 
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
      ], 
    passwordRules: [v => !!v || "Password is required"], 
    confirmPasswordRules: [v => !!v || "Confirmed Password is required"]
  }), 
  methods: {
    signup(){
      api.signup(this.first_name, this.last_name, this.email, this.password).then(() => {
        console.log("sucessfully signed up"); 
      }).catch(err => { 
        console.log(err); 
      })
    }
  }, 
  computed: {
    passwordConfirmationRule() {
      return () =>
        this.password === this.confirmPassword || "Password must match";
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