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
export default {
    name: "BusinessTable",
    props: ["headers", "data", "isLoading"],
    methods: {
      handleClick(value) {
        if (value.name && value.location) {
          // pass the name and location 
          this.$router.push({name: "Data Display", params: {name: value.name, location: value.location}});
        }
      }, 
    }
}
</script>
<style scoped>
</style>

