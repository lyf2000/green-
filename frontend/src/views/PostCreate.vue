<template>
    <div class="post-create">
        <v-btn
                @click="savePost"
        >Save
        </v-btn>
        <v-text-field v-model="title"></v-text-field>
        <markdown-editor
                toolbar="preview"
                v-model="text"
        >

        </markdown-editor>
    </div>
</template>

<script>

    export default {
        name: "PostCreate",
        data() {
            return {
                text: '',
                title: '',

            }
        },
        methods: {
            axiosPost(url, data = {}) {
                return this.$http.post(url, data)
            },
            axiosGet(url) {
                return this.$http.get(url)
            },
            savePost() {
                const self = this;
                const data = {
                    title: self.title,
                    text: self.text
                };
                self.$http.post('/posts/', data)
                    .then(function (response) {
                        console.log(response)
                    })
            },
        },
    }
</script>

<style scoped>

</style>