<template>
  <div class="login-container">
    <div class="login-box">
      <div class="login-header">
        <img src="@/assets/dmn1.jpg" alt="Logo" class="logo">
        <h2>Moon 后台管理系统</h2>
      </div>
      
      <div class="login-form">
        <div class="form-item">
          <input 
            type="text" 
            v-model="form.username" 
            placeholder="用户名"
          >
        </div>
        <div class="form-item">
          <input 
            type="password" 
            v-model="form.password" 
            placeholder="密码"
          >
        </div>
        <button class="login-button" @click="handleLogin">登录</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/store/user'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const form = reactive({
  username: '',
  password: ''
})

const handleLogin = async () => {
  try {
    await userStore.login(form)
    const redirect = route.query.redirect as string || '/'
    router.push(redirect)
  } catch (error) {
    console.error('登录失败:', error)
    alert('登录失败，请检查用户名和密码')
  }
}
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f0f2f5;
}

.login-box {
  width: 100%;
  max-width: 400px;
  padding: 40px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.login-header {
  text-align: center;
  margin-bottom: 40px;
}

.logo {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-bottom: 16px;
}

.form-item {
  margin-bottom: 24px;
}

.form-item input {
  width: 100%;
  padding: 10px;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  font-size: 14px;
}

.login-button {
  width: 100%;
  padding: 12px;
  background: #1890ff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

.login-button:hover {
  background: #40a9ff;
}
</style> 