<template>
    <v-app>
        <v-app-bar
                app
                color="primary"
                dark
        >

            <v-spacer></v-spacer>

        </v-app-bar>

        <v-content>
            <router-view></router-view>
        </v-content>
    </v-app>
</template>

<script>
    import HelloWorld from './components/HelloWorld';




    export default {
        name: 'App',

        components: {
            HelloWorld,
        },

        data: () => ({
            //
        }),
    };
</script>
