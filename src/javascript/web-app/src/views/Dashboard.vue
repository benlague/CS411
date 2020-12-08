<template>
<section>
  <div class = "title">
      <h1>Search for Business</h1>
  </div>
  <v-form>
    <v-container>
      <v-row>
        <v-col>
          <v-text-field
            label="Business Name"
            v-model="businessName"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            label="Location"
            v-model="location"
          ></v-text-field>
      </v-col>
      </v-row>
      <v-btn color="primary" elevation="2" @click="search">Search</v-btn>
    </v-container>
  </v-form>
  <div>
    <BusinessTable
      :headers="headers"
      :data="businesses"
      :isLoading="loadingTable"
    />
  </div>
</section>
</template>



<script>
import api from "../api.js"; 
import BusinessTable from "../components/BusinessTable"
export default {
    name: "Dashboard",
    components: {
      BusinessTable
  },
    data: () => ({
        location:"", 
        businessName:"", 
        headers: [], 
        businesses: [], 
        loadingTable: false 

    }),
    methods: {
        search(){
          this.businesses = []; 
          this.loadingTable = true; 
          api.search(this.businessName, this.location).then(data => {
            this.parseBusinessData(data); 
            this.loadingTable = false; 
          })
        }, 
        parseBusinessData(data) {
          // set the headers that we want to display
          this.headers = [{text: "name", value: "name"}, {text: "location", value: "location"}, {text: "Phone Number", value: "phoneNumber"}, {text: "price", value: "price"}, {text: "rating", value: "rating"}]
          // parse through response data and add to our component
          for (let i = 0; i < data.length; i ++) {
            this.businesses.push({
              "name": data[i]["name"], 
              "location": data[i]["location"]["display_address"][0] + " " + data[i]["location"]["display_address"][1], 
              "phoneNumber": data[i]["display_phone"], 
              "price": data[i]["price"], 
              "rating": data[i]["rating"]
            })
          }
        }
    }, 
}
</script>


<style scoped>
.title {
  margin-left: 45%;
  margin-top: 1%;
  font-size: large;
}
</style>
