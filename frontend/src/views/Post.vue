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
                                            @click="followUser(post.author.id)"
                                            x-small
                                            color="#00E676"
                                            v-bind:dark="isFriend"
                                            v-bind:outlined="isNotFriend"
                                    >follow
                                    </v-btn>
                                    <v-icon @click.prevent="bookmarkPost(id)"
                                            v-if="post.marked==='true'"
                                    >mdi-bookmark
                                    </v-icon>
                                    <v-icon @click.prevent="bookmarkPost(id)"
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
                    :src="post.main_img"
            ></v-img>
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
        computed: {
            isFriend() {
                return this.post.author.is_friend === 'true';
            },
            isNotFriend() {
                return this.post.author.is_friend !== 'true';
            }
        },
        methods: {
            f() {
                console.log(12)
            },
            axiosGet(url) {
                return this.$http.get(url)
            },
            axiosPost(url) {
                return this.$http.post(url)
            },
            loadPost() {
                const self = this;
                self.axiosGet('/posts/' + self.id)
                    .then(function (response) {
                        self.post = response.data;
                    })
            },
            bookmarkPost(id) {
                const self = this;
                // console.log(11);
                // console.log(this.marked);
                // console.log(this.post.marked);
                // const self = this;
                self.axiosPost('/bookmark/' + id)
                    .finally(function (response) {
                        self.post.marked = self.post.marked !== 'true' ? 'true' : 'false';
                        console.log('ok');
                    })
            },
            followUser(id) {
                const self = this;
                // console.log(11);
                // console.log(this.marked);
                // console.log(this.post.marked);
                // const self = this;
                self.axiosPost('/users/follow/' + id)
                    .finally(function (response) {
                        self.post.author.is_friend = self.post.author.is_friend !== 'true' ? 'true' : 'false';
                    })
            },
        },
        created() {
            this.loadPost()
        }

    }
</script>

<style scoped>

</style>