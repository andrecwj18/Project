<template>
    <v-container fluid>
        <div id="example-1">
            <button>Delete Row</button>
        </div>
        <v-card>
            <v-data-table v-model="selected"
                          :headers="headers"
                          :items="timestamp"
                          item-key="name"
                          show-select
                          class="elevation-1">
                <template v-slot:top>
                </template>
            </v-data-table>
        </v-card>
        <div>
            <VueTableDynamic />
        </div>
    </v-container>
</template>
<script>

    import VueTableDynamic from 'vue-table-dynamic'
    export default {
        components: {
            VueTableDynamic
        },
        computed: {
            headers() {
                return [
                    { text: 'Timestamp', value: 'timestamp' },
                    { text: 'Missing PPE', value: 'missing_ppe' },
                    { text: 'Image', value: 'Image' },
                ]
            }
        }
    }
</script>
<style scoped></style>
