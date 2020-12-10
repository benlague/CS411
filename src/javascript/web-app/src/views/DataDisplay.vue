<template>
    <div>
        <v-card shaped elevation="2" class="mx-10 mt-10">
            <v-card-title>Busyness Forecast</v-card-title>
            <v-card-subtitle>Venue Name</v-card-subtitle>
            <bar-chart class="mx-10 pb-5"></bar-chart>
        </v-card>
        <v-row class="mx-7 mt-10">
            <v-col>
                <v-card elevation="2">
                    <v-card-title>Quiet Hour</v-card-title>
                    <v-card-text>
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Laudantium, similique aut, nihil assumenda ea velit, praesentium aspernatur repellat cum aliquid sit at totam asperiores pariatur vel facilis est veritatis soluta!
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card elevation="2">
                    <v-card-title>Busy Hour</v-card-title>
                    <v-card-text>
                        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quasi tempore quae iusto similique sed, ex dignissimos exercitationem laudantium nemo culpa quam quia beatae deleniti maxime. Quidem beatae velit illo vel?
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
        location: ""
    }), 
    mounted() {
        if (this.$route.params.name && this.$route.params.location) {
            this.name = this.$route.params.name; 
            this.location = this.$route.params.location; 
        }
    }
}
</script>