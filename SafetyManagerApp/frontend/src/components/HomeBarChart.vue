<template>
    <v-card class="mt-4 mx-auto" max-width="100%">
        <v-sheet class="v-sheet--offset mx-auto"
                 elevation="6"
                 max-width="calc(100% - 32px)">
            <apexchart type="bar" height="200" :options="chartOptionsBar" :series="seriesBar"></apexchart>
        </v-sheet>
        <v-card-text class="pt-0">
            <div class="title font-weight-light mb-2">Type of PPE Violations</div>
            <div class="subheading font-weight-light grey--text">Shows the PPE that visitors were missing today and the last 4 days.</div>
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
    import VueApexCharts from 'vue-apexcharts'

    export default {
        name: 'HomeBarChart',
        components: {
            apexchart: VueApexCharts,
        },
        data: function () {
            return {
                seriesBar: [],
                chartOptionsBar: {
                    chart: {
                        toolbar: {
                            show: false,
                        },
                        type: 'bar',
                        height: 350,
                        stacked: true,
                    },
                    plotOptions: {
                        bar: {
                            horizontal: true,
                        },
                    },
                    stroke: {
                        width: 1,
                        colors: ['#fff']
                    },
                    title: {
                        text: undefined,
                    },
                    xaxis: {
                        categories: ['22 May', '21 May', '20 May' , '19 May', '18 May'],
                        labels: {
                            formatter: function (val) {
                                return val + "K"
                            }
                        }
                    },
                    yaxis: {
                        title: {
                            text: undefined
                        },
                    },
                    tooltip: {
                        y: {
                            formatter: function (val) {
                                return val + "K"
                            }
                        }
                    },
                    fill: {
                        opacity: 1
                    },
                    legend: {
                        position: 'top',
                        horizontalAlign: 'left',
                        offsetX: 40
                    }
                }
            }
        },
        mounted: function () {
            this.seriesBar = [{
                name: 'Hard Hat',
                data: [44, 55, 41, 37, 22]
            }, {
                name: 'Safety Goggles',
                data: [53, 32, 33, 52, 13]
            }, {
                name: 'Gloves',
                data: [12, 17, 11, 9, 15]
            }, {
                name: 'Safety Clothes',
                data: [9, 7, 5, 8, 6]
            }, {
                name: 'Covered Shoes',
                data: [25, 12, 19, 32, 25]
            }];
        }
    };
</script>

<style scoped>
</style>