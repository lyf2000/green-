<template>
    <div class="home">
        <!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
        <PostCardList/>
    </div>
</template>

<script>

    import HelloWorld from '@/components/HelloWorld.vue'
    import PostCardList from '@/components/home/PostCardList.vue'

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
