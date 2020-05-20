<template>
    <v-card shaped elevation="7"
            class="mx-auto"
            max-width="80%"

            outlined
    >
        <v-list-item three-line @click="goToPost">
            <v-list-item-content>
                <v-list-item-title class="headline mb-1">{{post.title}}</v-list-item-title>
                <v-list-item-subtitle>{{post.text}}</v-list-item-subtitle>
            </v-list-item-content>

        </v-list-item>

    </v-card>
</template>

<script>
    export default {
        name: "PostCard",
        props: {
            post: {
                type: Object,
            }
        },
        methods: {
          goToPost() {
            const self = this;
            console.log(self.post.id);
            this.$router.push('/post/' + self.post.id)
          },
        },
    }
</script>

<style scoped>

</style>