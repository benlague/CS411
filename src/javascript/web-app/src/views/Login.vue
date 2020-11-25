<template>
  <div class = "main-container">
      <h1>Login</h1>
      <v-form
      ref="form"
      v-model="valid"
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
        v-model="checkbox"
        :rules="[v => !!v || 'You must agree to continue!']"
        label="Do you want us to remember you?"
        required
      ></v-checkbox>

      <v-btn
        color="success"
        class="mr-4"
        @click="validate"
      >
        Login
      </v-btn>

    </v-form>
  </div>
</template>

<script>

export default {
  name: 'Login',
}
</script>

<style>
  .main-container {
    width: 50%; 
    margin-top: 10%;
    margin-left: 25%;
  }
</style>