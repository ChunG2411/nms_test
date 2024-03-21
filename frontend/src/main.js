import { createApp } from 'vue'
import './assets/style.css'
import App from './App.vue'
import router from './router/router.js'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'

const app = createApp(App)

library.add(fas)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.mount('#app')