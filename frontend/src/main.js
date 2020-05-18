import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import AXIOS from './router/axios'


import 'v-markdown-editor/dist/v-markdown-editor.css';
import Editor from 'v-markdown-editor'

Vue.config.productionTip = false;
Vue.use(Editor);



Vue.prototype.$http = AXIOS;


new Vue({
    router,
    store,
    vuetify,
    render: function (h) {
        return h(App)
    }
}).$mount('#app');
