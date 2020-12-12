<template>
    <div>
        <v-card shaped elevation="2" class="mx-10 mt-10">
            <v-card-title>Busyness Forecast</v-card-title>
            <v-card-subtitle>{{this.name + " @ " + this.location}}</v-card-subtitle>
            <bar-chart class="mx-10 pb-5" :data="dataCollection"></bar-chart>
        </v-card>
        <v-row class="mx-7 mt-10">
            <v-col>
                <v-card elevation="2">
                    <v-card-title>Quiet Hour</v-card-title>
                    <v-card-text>
                        {{this.parseTime(this.quiet_time)}}
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card elevation="2">
                    <v-card-title>Busy Hour</v-card-title>
                    <v-card-text>
                        {{this.parseTime(this.busy_time)}}
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>

<script>
import BarChart from "../components/BarChart"

export default {
    name: "DataDisplay",
    components: {
        BarChart
    }, 
    data: () => ({
        name: "", 
        location: "",
        dataCollection: {},
        busy_time: [],
        quiet_time: []
    }), 
    methods: {
        generateDatacollection(data){
            // added label and config for data to display in bar chart
            this.dataCollection = {
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
                data: data
                }
            ]
            }
        },
        parseTime(hours) {
            let hoursIn12 = []
            for (let i = 0; i < hours.length; i++){
                (hours[i] < 12) ? hoursIn12.push(hours[i] + "AM") : hoursIn12.push((hours[i] - 12) + "PM")
            }
            return hoursIn12
        }
    },
    mounted() {
        if (this.$route.params.name && this.$route.params.location) {
            this.name = this.$route.params.name; 
            this.location = this.$route.params.location; 
            this.busy_time = this.$route.params.busy_time;
            this.quiet_time = this.$route.params.quiet_time;
        }
    },
    created() {
        this.generateDatacollection(this.$route.params.day_raw)
    }
}
</script>