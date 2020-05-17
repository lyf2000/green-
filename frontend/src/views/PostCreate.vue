<template>
    <div class="post-create">
        <v-btn
            @click="savePost"
        >Save
        </v-btn>
        <markdown-editor
                toolbar="preview"
                v-model="text"
        >

        </markdown-editor>
    </div>
</template>

<script>
    import {AXIOS} from '../main'

    export default {
        name: "PostCreate",
        data() {
            return {
                text: ''
            }

        }
    }
</script>

<style scoped>

</style>