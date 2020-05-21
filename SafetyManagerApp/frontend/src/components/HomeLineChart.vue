<template>
    <v-card class="mt-4 mx-auto" max-width="100%">
        <v-sheet class="v-sheet--offset mx-auto"
                 elevation="6"
                 max-width="calc(100% - 32px)">
            <apexchart type="line" height="200" :options="chartOptionsLine" :series="seriesLine"></apexchart>
        </v-sheet>

        <v-card-text class="pt-0">
            <div class="title font-weight-light mb-2">Total PPE Violations</div>
            <div class="subheading font-weight-light grey--text">Shows the total PPE violations today and the last 4 days.</div>
            <v-divider class="my-2"></v-divider>
            <v-icon class="mr-2"
                    small>
                mdi-clock
            </v-icon>
            <span class="caption grey--text font-weight-light">last updated 1 hour ago</span>
        </v-card-text>
    </v-card>
</template>

<script>
    import VueApexCharts from 'vue-apexcharts';
    import axios from 'axios';

    export default {
        name: 'HomeLineChart',
        components: {
            apexchart: VueApexCharts,
        },
        data: function () {
            return {
                seriesLine: [],
                chartOptionsLine: {
                    chart: {
                        toolbar: {
                            show: false,
                        },
                        height: 350,
                        type: 'line',
                        zoom: {
                            enabled: false
                        }
                    },
                    dataLabels: {
                        enabled: false
                    },
                    stroke: {
                        curve: 'straight'
                    },
                    title: {
                        text: undefined,
                    },
                    grid: {
                        row: {
                            colors: ['#f3f3f3', 'transparent'],
                            opacity: 0.5
                        },
                    },
                    xaxis: {
                        categories: ['18 May', '19 May', '20 May', '21 May', '22 May'],
                    }
                },
            }
        },
        mounted: function () {
            axios.get('/api/details/total_violation').then((response) => {
                this.seriesLine = [{
                    name: "PPE Violations", 
                    data: response.data.series1,
                }];
            })
            
        }
    };
</script>

<style scoped>
</style>