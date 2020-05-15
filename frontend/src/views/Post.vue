<template>
    <v-row
            justify="center"
    >
        <v-col
                cols="6"
        >
            <v-card-title
            >
                <v-card-title><h1>iudnbdifunUINUInuinIUN</h1></v-card-title>
                <v-card-text>
                    <v-list>
                        <v-list-item
                        >
                            <v-list-item-avatar>
                                <v-img src="https://miro.medium.com/max/2000/1*iY6f9EVIPPBM62HtnAEBfA.png"></v-img>
                            </v-list-item-avatar>

                            <v-list-item-content>
                                <v-list-item-title>inijniniun
                                        <v-btn
                                                x-small
                                                color="#00E676"
                                                dark
                                        >follow
                                        </v-btn>
                                        <v-icon>mdi-bookmark-outline</v-icon>
                                        <v-icon>mdi-bookmark</v-icon>
                                </v-list-item-title>
                                <v-list-item-subtitle>uinuin</v-list-item-subtitle>
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
            <v-card-title class="post-text"
                          outlined
            >
                <h1>
                    wrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeuf</h1>
                <v-img
                        width="100%"
                        src="https://miro.medium.com/max/2000/1*iY6f9EVIPPBM62HtnAEBfA.png"
                ></v-img>
                <h1>
                    wrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeufwrueibheutniuednbeuf</h1>
            </v-card-title>
        </v-col>
    </v-row>
</template>

<script>
    import {AXIOS} from '../main'

    export default {
        name: "Post",
        props: ['id'],
        data() {
            return {
                author: null,
                post: null,

            }
        },
        methods: {
            f() {
                console.log(12)
            },
            axiosGet(url) {
                return AXIOS.get(url)
            },
            loadPost() {
                const self = this;
                self.axiosGet('/posts/' + self.id)
                    .then(function (response) {
                        const {author, text, title, tags} = response.data;
                        self.author = author;
                        self.post = {
                            text: text,
                            title: title,
                            tags: tags
                        }
                    })
            }
        },
        created() {
            this.loadPost()
        }

    }
</script>

<style scoped>

</style>