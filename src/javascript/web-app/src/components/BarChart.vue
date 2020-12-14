<script>
  //Importing Bar class from the vue-chartjs wrapper
  import { Bar } from 'vue-chartjs'
  //Exporting this so it can be used in other components
  export default {
    extends: Bar,
    props: ["data"],
    data () {
      return {
        //Chart.js options that controls the appearance of the chart
        options: {
          scales: {
            yAxes: [{
              ticks: {
                callback: function(value) {
                        return (value % 20 == 0) ? value + "%" : "";
                    },
                beginAtZero: true
              },
            }],
            xAxes: [ {
              gridLines: {
                display: false
              },
              ticks: {
                callback: function(value) {
                  let hour = parseInt(value.slice(0,-2));
                  return (hour % 3 == 0) ? value : ""
                }
              }
            }]
          },
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
        }
      }
    },
    mounted () {
      //renderChart function renders the chart with the datacollection and options object.
      console.log(this.data)
      this.renderChart(this.data, this.options)
    }
  }
</script>