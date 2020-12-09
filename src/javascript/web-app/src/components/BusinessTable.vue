<template>
  <div>
    <v-data-table 
      :headers="headers"
      :items="data"
      :disable-pagination="true"
      :loading="isLoading"
      :fixed-header="true"
      :hide-default-footer="true"
    ></v-data-table>
  </div>
</template>
<script>
export default {
    name: "BusinessTable",
    props: ["headers", "data", "isLoading"],
}
</script>
<style scoped>
</style>
