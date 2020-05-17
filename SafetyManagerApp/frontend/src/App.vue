<template>
    <v-app>
        <v-app-bar app color="primary" dark elevation="0" class="px-2">
            <v-app-bar-nav-icon
                @click.stop="sidebarMenu = !sidebarMenu"
            ></v-app-bar-nav-icon>
            <v-spacer></v-spacer>
            <v-btn @click="toggleTheme" color="primary" class="mr-2">
                {{ buttonText }}
            </v-btn>
            <v-icon>mdi-account</v-icon>
        </v-app-bar>
        <v-navigation-drawer
            v-model="sidebarMenu"
            app
            floating
            :permanent="sidebarMenu"
            :mini-variant.sync="mini">
            <v-list dense color="primary" rounded="false" dark>
                <v-list-item>
                    <v-list-item-action>
                        <v-icon @click.stop="toggleMini = !toggleMini"
                            >mdi-chevron-left</v-icon
                        >
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>
                            <h3 class="font-weight-thin">Navigation</h3>
                        </v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
            <v-list>
                <v-list-item
                    v-for="item in items"
                    :key="item.title"
                    link
                    :to="item.href"
                >
                    <v-list-item-icon>
                        <v-icon color="primary">{{ item.icon }}</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title class="primary--text">
                            {{ item.title }}
                        </v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-content>
            <v-container fluid>
                <v-row>
                    <v-col class="px-6">
                        <transition name="fade">
                            <router-view></router-view>
                        </transition>
                    </v-col>
                </v-row>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
export default {
    name: 'App',
    computed: {
        mini() {
            return this.$vuetify.breakpoint.smAndDown || this.toggleMini;
        },
        buttonText() {
            return !this.$vuetify.theme.dark ? 'Go Dark' : 'Go Light';
        }
    },
    data: () => ({
        sidebarMenu: true,
        toggleMini: false,
        items: [
            { title: 'Home', href: '/', icon: 'home' },
            {
                title: 'PPE Selection',
                href: '/ppeselection',
                icon: 'mdi-hard-hat'
            },
            {
                title: 'Manage Logs',
                href: '/managelogs',
                icon: 'mdi-file-document-outline'
            },
            {
                title: 'Slack Notifications',
                href: '/slacknotifications',
                icon: 'mdi-bell-outline'
            },
            { title: 'Settings', href: '/settings', icon: 'mdi-cog-outline' }
        ]
    }),
    methods: {
        toggleTheme() {
            this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
        }
    }
};
</script>

<style scoped>
.v-list--dense {
    border-radius: 0 !important;
}
</style>
