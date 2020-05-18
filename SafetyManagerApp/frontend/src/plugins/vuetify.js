import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import light from './vuetify/lightTheme';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: { light },
    },
});
