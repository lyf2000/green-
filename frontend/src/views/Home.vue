<template>
    <div class="home">
        <!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
        <PostCardList/>
    </div>
</template>

<script>
    import {AXIOS} from '../main'

    import HelloWorld from '@/components/HelloWorld.vue'
    import PostCardList from '@/components/main/PostCardList.vue'

    export default {
        name: 'Home',
        props: ['id'],
        components: {
            HelloWorld, PostCardList
        },
        data() {
            return {

            }
        },
        methods: {

        },
        created() {

        }
    }
</script>
