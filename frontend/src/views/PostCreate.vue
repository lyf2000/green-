<template>
    <div class="post-create">
        <v-file-input
                label="Main Image"
                filled
                prepend-icon="mdi-camera"
                v-model="img"
        ></v-file-input>
        <v-btn
                @click="savePost"
        >Save
        </v-btn>
        <v-text-field placeholder="Title" v-model="title"></v-text-field>
        <markdown-editor
                toolbar="preview"
                v-model="text"
                placeholder="Content"
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
                img: '',

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

                let formData = new FormData();
                formData.append("main_img", self.img);
                formData.append("title", self.title);
                formData.append("text", self.text);

                self.$http.post('/posts/', formData)
                    .then(function (response) {
                        console.log(response)
                    })
            },
        },
    }
</script>

<style scoped>

</style>