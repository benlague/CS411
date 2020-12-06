<script>
  //Importing Bar class from the vue-chartjs wrapper
  import { Bar } from 'vue-chartjs'
  //Exporting this so it can be used in other components
  export default {
    extends: Bar,
    data () {
      return {
        datacollection: {
          //Data to be represented on x-axis
          labels: ["6AM", "7AM", "8AM", "9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", 
                   "6PM", "7PM", "8PM", "9PM", "10PM", "11PM", "12AM", "1AM", "2AM", "3AM", "4AM", "5AM"],
          datasets: [
            {
              label: 'Venue Capacity',
              backgroundColor: '#2980B9',
              pointBackgroundColor: 'white',
              borderWidth: 1,
              pointBorderColor: '#249EBF',
              //Data to be represented on y-axis
              data: [45,50,60,60,65,60,60,60,60,65,65,65,70,80,90,100,100,90,70,50,35,0,0,40]
            }
          ]
        },
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
      this.renderChart(this.datacollection, this.options)
    }
  }
</script>