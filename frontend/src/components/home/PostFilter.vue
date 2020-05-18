<template>
    <v-row>
        <v-col
                cols="12"
                sm="2"
        >
            <v-text-field
                    v-on:keypress.enter="filterPosts"
                    v-model="searchText"
                    label="Search"
                    :filled="true"
                    :clearable="true"
            ></v-text-field>
        </v-col>
        <v-col
                cols="12"
                sm="2"
        >
            <v-select
                    filled
                    :items="orderValues"
                    label="Order by created date"
                    v-model="orderSelected"
                    v-on:change="filterPosts"
            ></v-select>
        </v-col>
        <v-col cols="12" sm="2">
            <v-select
                    v-model="tagsSelected"
                    :items="tags"
                    chips
                    label="Tags"
                    multiple
            ></v-select>
        </v-col>
        <v-col cols="12" sm="1">
            <div class="my-2">
                <v-btn
                        outlined
                        @click="filterPosts"
                >Search
                </v-btn>
            </div>
        </v-col>
        <v-col cols="12" sm="2">

            <div class="ma-2">
                <v-btn :disabled="!prev"
                       depressed
                       small
                       @click="$emit('prev-page')"
                >
                    <v-icon>mdi-chevron-left</v-icon>
                </v-btn>
                <v-btn :disabled="!next"
                       depressed
                       small
                       @click="$emit('next-page')"
                >
                    <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
            </div>
        </v-col>

    </v-row>
</template>

<script>

    export default {
        name: "PostFilter",
        props: {
            next: null,
            prev: null
        },
        data() {
            return {
                searchText: "",
                orderValues: ['Asc', "Desc"],
                orderSelected: 'Desc',
                tags: [],
                tagsSelected: [],
            }
        },
        methods: {
            getSearchParams() {
                let self = this;
                return {
                    'search': self.searchText.trim(),
                    'ordering': self.getOrderValue(),
                    'tags': self.tagsSelected
                }
            },
            getOrderValue() {
                let self = this;
                let order = "-created";
                if (self.orderSelected === "Asc") {
                    order = "created"
                }
                return order
            },
            filterPosts() {
                const searchParams = decodeURIComponent(new URLSearchParams(this.getSearchParams()).toString());
                console.log(searchParams);
                this.$emit('filter-posts', searchParams);
            },
            loadTagList() {
                const self = this;
                this.$http.get('/tags')
                    .then(function (response) {
                        self.tags = response.data.map(tag => {
                            return tag.name
                        })
                    })
            }
        },
        created() {
            this.loadTagList()
        }
    }
</script>

<style scoped>

</style>