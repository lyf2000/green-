<template>
    <v-row
            justify="center"
    >
        <v-col
                cols="6"
        >
            <v-card-title
            >
                <v-card-title><h1>{{post.title}}</h1></v-card-title>
                <v-card-text>
                    <v-list>
                        <v-list-item
                        >
                            <v-list-item-avatar>
                                <v-img src="https://miro.medium.com/max/2000/1*iY6f9EVIPPBM62HtnAEBfA.png"></v-img>
                            </v-list-item-avatar>

                            <v-list-item-content>
                                <v-list-item-title>{{post.author.username}}
                                    <v-btn
                                            @click="follow(post.author.id)"
                                            x-small
                                            color="#00E676"
                                            :dark="post.author.is_friend==='true'"
                                            :outlined="post.author.is_friend!=='true'"
                                    >follow
                                    </v-btn>
                                    <v-icon @click.prevent="bookmarkPost(id)"
                                            v-if="post.marked==='true'"
                                    >mdi-bookmark
                                    </v-icon>
                                    <v-icon @click="bookmarkPost(id)"
                                            v-else
                                    >mdi-bookmark-outline
                                    </v-icon>
                                </v-list-item-title>
                                <v-list-item-subtitle>{{post.created}}</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                    </v-list>
                </v-card-text>
            </v-card-title>
        </v-col>

        <v-col class="post-main-img"
               cols="8"
        >
            <v-img
                    src="https://miro.medium.com/max/2000/1*iY6f9EVIPPBM62HtnAEBfA.png"
            >

            </v-img>
        </v-col>
        <v-col
                cols="6"
        >
            <markdown-editor
                    toolbar="preview"
                    v-model="post.text"
            ></markdown-editor>
        </v-col>
    </v-row>
</template>

<script>

    export default {
        name: "Post",
        props: ['id'],
        data() {
            return {
                post: null,
            }
        },
        methods: {
            f() {
                console.log(12)
            },
            axiosGet(url) {
                return this.$http.get(url)
            },
            loadPost() {
                const self = this;
                self.axiosGet('/posts/' + self.id)
                    .then(function (response) {
                        self.post = response.data;
                    })
            },
            bookmarkPost(id) {
                // console.log(11);
                // console.log(this.marked);
                this.post.marked = this.post.marked!=='true' ? 'true' : 'false'
                // console.log(this.post.marked);
                // const self = this;
                // self.axiosGet('bookmark/' + id)
                //     .then(function (response) {
                //
                //     })
                //     .catch(function (response) {
                //         console.log(response)
                //     })
            },
            follow(id) {
                console.log(id)
            }
        },
        created() {
            this.loadPost()
        }

    }
</script>

<style scoped>

</style>