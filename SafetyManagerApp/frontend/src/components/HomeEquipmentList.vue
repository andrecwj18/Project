<template>
    <v-card class="mt-4 mx-auto" max-width="100%">
        <v-sheet class="v-sheet--offset d-flex mx-auto"
                 elevation="6"
                 max-width="calc(100% - 32px)"
                 color="orange">
            <span class="font-weight-light d-flex align-center mr-auto white--text pl-6 py-7">PPE Required Today</span>
            <v-card-actions class="pr-4">
                <v-btn fab small>
                    <v-icon>mdi-file-document-edit</v-icon>
                </v-btn>
            </v-card-actions>
        </v-sheet>
        <v-list class="pl-2">
            <v-list-item v-for="(item, i) in items" :key="i">
                <v-list-item-icon>
                    <v-icon v-text="item.icon"></v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title v-text="item.text"></v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>

    </v-card>
</template>

<script>
    export default {
        name: 'HomeEquipmentList',
        data: function () {
            return {
                item: 1,
                items: [
                    { icon: 'mdi-hard-hat', text: 'Hard Hat' },
                    { icon: 'mdi-safety-goggles', text: 'Goggles' },
                    { icon: 'mdi-hand', text: 'Gloves' },
                    { icon: 'mdi-tshirt-crew', text: 'Safety Clothes' },
                    { icon: 'mdi-shoe-formal', text: 'Covered Shoes' },
                ],
            }
        },
    };
</script>

<style scoped>
</style>