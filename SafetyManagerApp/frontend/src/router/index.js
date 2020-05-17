import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/ppeselection',
        name: 'PPESelection',
        component: () => import('../views/PPESelection.vue')
    },
    {
        path: '/managelogs',
        name: 'ManageLogs',
        component: () => import('../views/ManageLogs.vue')
    },
    {
        path: '/slacknotifications',
        name: 'SlackNotifications',
        component: () => import('../views/SlackNotifications.vue')
    },
    {
        path: '/settings',
        name: 'Settings',
        component: () => import('../views/Settings.vue')
    }
];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router;
