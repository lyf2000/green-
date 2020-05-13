import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import axios from 'axios'

Vue.config.productionTip = false

export const AXIOS = axios.create({
  baseURL: 'http://127.0.0.1:8000/api'
});
new Vue({
  router,
  store,
  vuetify,
  render: function (h) { return h(App) }
}).$mount('#app')
