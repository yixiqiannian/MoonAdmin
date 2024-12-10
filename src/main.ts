import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import './router/permission'
import { useUserStore } from '@/store/user'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)

const userStore = useUserStore()
if (userStore.token) {
  userStore.fetchUserInfo(userStore.token)
}

app.mount('#app')
