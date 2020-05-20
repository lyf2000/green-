<template>
    <div class="signin">
        <v-text-field v-model="username"></v-text-field>
        <v-text-field v-model="password"></v-text-field>
        <v-btn @click.prevent="login">log</v-btn>
    </div>
</template>

<script>

    import LocalStorageService from "../store/LocalStorageService";


    export default {
        name: "SignIn",
        data() {
            return {
                username: '',
                password: '',
                localStorageService: LocalStorageService.getService(),

            }
        },
        methods: {
            login() {
                const self = this;
                const data = {
                    'username': self.username,
                    'password': self.password
                };
                self.$http.post('http://127.0.0.1:8000/api/token/', data)
                    .then(function (response) {
                        self.localStorageService.setToken(response.data);
                        alert('OK');
                    })
                    .catch(function (error) {
                        alert('cred wrong!');
                    });
                self.username = '';
                self.password = '';
            }
        }
    }
</script>

<style scoped>

</style>