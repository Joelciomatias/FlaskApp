import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
//import store from './store'

import VueSocketIO from 'vue-socket.io'
 
Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueAxios, axios)    
Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://localhost:5000',
    vuex: {
        actionPrefix: 'SOCKET_',
        mutationPrefix: 'SOCKET_'
    },
    options: { } //Optional options
}))

new Vue({
    //router
    render: h => h(App)
}).$mount('#app')
