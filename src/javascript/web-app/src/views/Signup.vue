<template>
  <div class = "signup-container">
      <h1>Signup</h1>
      <v-form
      ref="form"
      v-model="valid"
      @submit.prevent="signup"
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
        :disabled="!valid"
      >
        Signup
      </v-btn>
      <a class = "mr-4" href="/login">Already have an account?</a>

    </v-form>
  </div>
</template>

<script>
import api from "../api"; 
export default {
  name: 'Signup',
  data: () => ({
    valid: true, 
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
        this.$router.push("/login");
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