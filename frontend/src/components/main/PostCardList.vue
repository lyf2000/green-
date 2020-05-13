<template>
    <div>
        <v-container>
            <PostFilter
                    @filter-posts="filterPosts"
                    @prev-page="prevPage"
                    @next-page="nextPage"
                    v-bind:next="next"
                    v-bind:prev="prev"
            />
            <PostCardItem
                    v-for="post of posts"
                    v-bind:post="post"
            />
        </v-container>
    </div>
</template>

<script>

    import PostCardItem from "./PostCardItem";
    import PostFilter from "./PostFilter";

    import {AXIOS} from "../../main";

    export default {
        name: "PostCardList",
        data() {
            return {
                posts: [],
                next: null,
                prev: null,

            }
        },
        components: {
            PostCardItem, PostFilter
        },
        methods: {

            loadPosts() {
                this.filterPosts("")
            },
            f() {
                console.log(123);
            },
            axiosGet(url) {
                return AXIOS.get(url)
            },
            otherPage(url) {
                const self = this;
                self.axiosGet(url)
                    .then(function (response) {
                        self.newPosts(response);
                    })
            },
            newPosts(response) {
                const {results, next, previous} = response.data

                this.posts = results;
                this.next = next;
                this.prev = previous
            },
            filterPosts(searchParams) {
                const self = this;
                const url = '/posts/?' + searchParams;
                self.axiosGet(url)
                    .then(function (response) {
                        self.newPosts(response)
                    })
            },
            prevPage() {
                console.log('PREV');
                if (this.prev) {
                    console.log(this.prev);
                    this.otherPage(this.prev)
                }
            },
            nextPage() {
                console.log('NEXT');
                if (this.next) {
                    console.log(this.next);
                    this.otherPage(this.next)
                }
            }

        },
        created() {
            this.loadPosts();
        }
    }
</script>

<style scoped>

</style>