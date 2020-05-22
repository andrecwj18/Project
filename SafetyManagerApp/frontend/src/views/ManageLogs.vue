<div>
    <v-container fluid>
        <div id="example-1">
            <button>Delete Row</button>
        </div>
        <v-card>
            <v-data-table v-model="selected"
                          :headers="headers"
                          :items="itemList"
                          item-key="name"
                          show-select
                          class="elevation-1"
                          loading>
                <template slot="items" slot-scope="props">
                    <td>{{ props.item.id }}</td>
                    <td class="text-xs-right">{{ props.item.isviolated }}</td>
                    <td class="text-xs-right">{{ props.item.timestamp }}</td>
                    <td class="text-xs-right">{{ props.item.equipment }}</td>
                </template>
            </v-data-table>
        </v-card>
    </v-container>
</div>

<script>

    import Axios from "axios"


    export default {
        data() {
            return {
                selected: [],
                itemList: [],
                headers: [
                    { text: 'ID', value: 'id' },
                    { text: 'Violation', value: 'isviolated' },
                    { text: 'Timestamp', value: 'timestamp' },
                    { text: 'Missing PPE', value: 'equipment' },
                ]
            }
        },
        created() {
            Axios.get('http://localhost:50550/api/logs/').then(response => (this.itemList = response.data.Success))
        }
    }
</script>
<style scoped></style>
