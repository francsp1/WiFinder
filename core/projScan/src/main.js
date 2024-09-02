import { createApp } from 'vue'
import PrimeVue from 'primevue/config';

import Tooltip from 'primevue/tooltip';

import App from './App.vue'

import './assets/main.css'

import store from './store'
import router from './router'

createApp(App).use(PrimeVue).directive('tooltip', Tooltip).use(store).use(router).mount('#app')
