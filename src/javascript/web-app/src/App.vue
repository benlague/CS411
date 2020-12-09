<template>
  <v-app>
    <v-snackbar v-model="snackbar.show" :color="snackbar.color" :top="true" :timeout="3000">
      {{ snackbar.message }}
      <v-btn dark text @click="snackbar.show = false">Close</v-btn>
    </v-snackbar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import { mapState } from "vuex";


export default {
  name: 'App',
    computed: {
    ...mapState(["snackbar"])
  },

};
</script>
