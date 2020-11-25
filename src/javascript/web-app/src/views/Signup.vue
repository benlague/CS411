<template>
  <div class = "main-container">
      <h1>Signup</h1>
      <v-form
      ref="form"
      v-model="valid"
      lazy-validation
    >
    <v-text-field
        v-model="name"
        :rules="[v => !!v || 'Name is required']"
        label="Name"
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
        @click="validate"
      >
        Signup
      </v-btn>

    </v-form>
  </div>
</template>

<script>

export default {
  name: 'Signup',
}
</script>

<style>
  .main-container {
    width: 50%; 
    margin-top: 10%;
    margin-left: 25%;
  }
</style>