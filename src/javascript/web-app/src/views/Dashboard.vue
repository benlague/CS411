<template>
<section>
  <LogoutNav :showBackArrow="false"/>
  <div class = "title">
      <h1>Search for Business</h1>
  </div>
  <v-form>
    <v-container>
      <v-row>
        <v-col>
          <v-text-field
            label="Business Keyword(s)"
            v-model="setKeyword"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            label="Location"
            v-model="setLocation"
          ></v-text-field>
      </v-col>
      </v-row>
      <v-btn color="primary" elevation="2" @click="search">Search</v-btn>
    </v-container>
  </v-form>
  <div>
    <BusinessTable
      :headers="this.headers"
      :data="this.businesses"
    />
  </div>
</section>
</template>



<script>
import api from "../api.js"; 
import { mapState } from "vuex";
import BusinessTable from "../components/BusinessTable";
import LogoutNav from "../components/LogoutNav";

export default {
    name: "Dashboard",
    components: {
      BusinessTable, 
      LogoutNav

  },
    methods: {
        search(){
          this.$store.commit("setLoadingTable", true)  
          api.search(this.setKeyword, this.setLocation).then(data => {
            if (data) {
                this.parseBusinessData(data); 
            }
          this.$store.commit("setLoadingTable", false)  
          })
        }, 
        parseBusinessData(data) {
          let parsingBusinesses = []
          // set the headers that we want to display
          this.$store.commit("setHeaders", [{text: "name", value: "name"}, {text: "location", value: "location"}, {text: "Phone Number", value: "phoneNumber"}, {text: "price", value: "price"}, {text: "rating", value: "rating"}])
          
          // parse through response data and add to our component
          for (let i = 0; i < data.length; i ++) {
            parsingBusinesses.push({
              "name": data[i]["name"], 
              "location": data[i]["location"]["display_address"][0] + " " + data[i]["location"]["display_address"][1], 
              "phoneNumber": data[i]["display_phone"], 
              "price": data[i]["price"], 
              "rating": data[i]["rating"]
            })
          }
          this.$store.commit("setBusinesses", parsingBusinesses); 
        }
    },
    computed: {
    ...mapState(["businesses", "headers", "businessName", "location"]), 
    setKeyword: {
      set(val) {
        this.$store.commit("setBusinessName", val)
      }, 
      get(){
        return this.businessName
      }
    }, 
    setLocation: {
      set(val) {
        this.$store.commit("setLocation", val)
      }, 
      get() {
        return this.location
      }
    }
  }

}
</script>


<style scoped>
.title {
  margin-left: 45%;
  margin-top: 1%;
  font-size: large;
}
</style>
