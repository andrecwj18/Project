<template>
    <v-container fluid>
        <div id="example-1">
            <button>Delete Row</button>
        </div>
        <v-card>
            <v-data-table v-model="selected"
                          :headers="headers"
                          :items="items"
                          item-key="name"
                          show-select
                          class="elevation-1"
                          loading>
                <template v-slot:top>
                </template>
            </v-data-table>
        </v-card>
    </v-container>
</template>
<script>

    import Axios from "axios"


    export default {
        data() {
            return {
                selected: [],
                itemList: [],
                headers: [
                    { text: 'ID', value: 'id' },
                    { text: 'Violation', value: 'violation' },
                    { text: 'Timestamp', value: 'timestamp' },
                    { text: 'Missing PPE', value: 'ppe' },
                    { text: 'Image', value: 'image' }
                ],
                items: [
                    Axios.get('http://localhost:65006/api/logs/')
                ]
            }
        }
    }
</script>
<style scoped></style>
