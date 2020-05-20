<template>
    <v-container fluid>
        <v-row>
            <v-col cols="5">
                <home-line-chart></home-line-chart>
            </v-col>
            <v-col>
                <home-bar-chart></home-bar-chart>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="4">
                <home-equipment-list></home-equipment-list>
            </v-col>
            <v-col>
                <home-camera></home-camera>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import HomeLineChart from '@/components/HomeLineChart';
    import HomeBarChart from '@/components/HomeBarChart';
    import HomeEquipmentList from '@/components/HomeEquipmentList';
    import HomeCamera from '@/components/HomeCamera';

export default {
    name: 'Home',
    components: {
        HomeLineChart,
        HomeBarChart,
        HomeEquipmentList,
        HomeCamera,
    }
};
</script>

<style>
    .v-sheet--offset {
        top: -24px;
        position: relative;
    }
</style>
