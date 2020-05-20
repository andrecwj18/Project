<template>
    <v-container fluid>
        <div id="example-1">
            <button>Delete Row</button>
        </div>
        <v-card>
                <vue-table-dynamic :params="params"
                                   @select="onSelect"
                                   @selection-change="onSelectionChange"
                                   ref="table">
                </vue-table-dynamic>
        </v-card>
    </v-container>
</template>
<script>

    import VueTableDynamic from 'vue-table-dynamic'
    export default {
        name: 'Demo',
        data() {
            return {
                params: {
                    data: [
                        ['Timestamp', 'Missing PPE', 'Image of Incident'],
                        [1, 'b3ba90', '7c95f7'],
                        [2, 'ec0b78', 'ba045d'],
                        [3, '63788d', 'a8c325']
                    ],
                    header: 'row',
                    border:true,
                    showCheck: true

                }
            }
        },
        methods: {
            onSelect(isChecked, index, data) {
                console.log('onSelect: ', isChecked, index, data)
                console.log('Checked Data:', this.$refs.table.getCheckedRowDatas(true))
            },
            onSelectionChange(checkedDatas, checkedIndexs, checkedNum) {
                console.log('onSelectionChange: ', checkedDatas, checkedIndexs, checkedNum)
            }
        },
        components: { VueTableDynamic }
    }
</script>
<style scoped></style>
