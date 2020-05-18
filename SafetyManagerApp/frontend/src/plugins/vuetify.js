import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import light from './vuetify/lightTheme';
import VueTableDynamic from 'vue-table-dynamic'

Vue.use(Vuetify);
Vue.use(VueTableDynamic);

export default new Vuetify({
    theme: {
        themes: { light },
    },
});
