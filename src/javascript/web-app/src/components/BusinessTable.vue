<template>
  <div>
    <v-data-table 
      :headers="headers"
      :items="data"
      :disable-pagination="true"
      :loading="this.loadingTable"
      :fixed-header="true"
      :hide-default-footer="true"
      @click:row="handleClick"
    ></v-data-table>
  </div>
</template>
<script>
import api from "../api"
import {mapState} from "vuex"

export default {
    name: "BusinessTable",
    props: ["headers", "data"],
    methods: {
      handleClick(value) {
        if (value.name && value.location) {
          // pass the besttime data 
          this.$store.commit("setLoadingTable", true)  
          api.forecast(value.name, value.location).then(data => {
            this.$store.commit("setLoadingTable", false)  
            console.log(data)
            this.$router.push({name: "Data Display", params: {
                    name: value.name, 
                    location: value.location, 
                    day_raw: data.day_raw, 
                    busy_time: data.busy_hours, 
                    quiet_time: data.quiet_hours}});
          })
        }
      }, 
    }, 
    computed: {
        ...mapState(["loadingTable"])
    }
}
</script>
<style scoped>
</style>

