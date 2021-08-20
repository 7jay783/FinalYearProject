import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'

import 'bootstrap/dist/css/bootstrap.min.css'

let app = createApp(App)

// global variables use using this.<variable-name>
app.config.globalProperties.API_BASE_URL = process.env.VUE_APP_API_BASE_URL

app.use(router)

app.mount('#app')
