<template>
  <div>
    <v-data-table 
      :headers="headers"
      :items="data"
      :disable-pagination="true"
      :loading="isLoading"
      :fixed-header="true"
      :hide-default-footer="true"
      @click:row="handleClick"
    ></v-data-table>
  </div>
</template>
<script>
import api from "../api"

export default {
    name: "BusinessTable",
    props: ["headers", "data", "isLoading"],
    methods: {
      handleClick(value) {
        if (value.name && value.location) {
          // pass the besttime data 
          api.forecast(value.name, value.location).then(data => {
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
    }
}
</script>
<style scoped>
</style>

