/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import axios from 'axios'
import { registerPlugins } from '@/plugins'

// Set default URL for axios
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'; 

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

const app = createApp(App)

registerPlugins(app)

app.mount('#app')
