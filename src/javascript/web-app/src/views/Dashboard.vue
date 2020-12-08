<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          sm="6"
          md="3"
        >
          <v-text-field
            label="Business Name"
            v-model="businessName"
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          sm="6"
          md="3"
        >
          <v-text-field
            label="Location"
            v-model="location"
          ></v-text-field>
      </v-col>
      </v-row>
      <v-btn color="primary" elevation="2" @click="search">Search</v-btn>
    </v-container>
  </v-form>
</template>



<script>
import api from "../api.js"
export default {
    name: "Dashboard",
    data: () => ({
        location:"", 
        businessName:""
    }),
    methods: {
        search(){
          api.search(this.businessName, this.location)
        }
    }
}
</script>


