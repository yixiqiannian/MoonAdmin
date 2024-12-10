<template>
  <div class="home">
    <div class="header">
      <!-- <h1>Moon Admin</h1> -->
      <p class="last-login-time">上次登录时间: {{ lastLoginTime }}</p> <!-- 显示上次登录时间 -->
      <div class="nav-right">
        <!-- <div class="dropdown">
          <span @click="toggleDropdown" class="username">Moon Admin11</span>
          <div v-if="isDropdownOpen" class="dropdown-content">
            <router-link to="/admin/profile" class="dropdown-item">个人中心</router-link>
            <button @click="logout" class="dropdown-item">退出登录</button>
          </div>
        </div> -->
      </div>
    </div>
    <div class="welcome-section">
      <div class="welcome-header">
        
        <img src="@/assets/dmn1.jpg" alt="Logo" class="logo">
        <div class="welcome-name">
          <h3>欢迎使用 Moon Admin</h3>
          <p>今日天气：阴；不管天气如何，都要保持好心情</p>
        </div><!-- <h1>欢迎使用 Moon Admin</h1> -->
      </div>
      <div class="stat-card">
        <h3>访问量</h3>
        <div class="stat-value">1,234</div>
      </div>

      <div class="stat-card">
        <h3>新增用户</h3>
        <div class="stat-value">14</div>
      </div>

      <div class="stat-card">
        <h3>任务量</h3>
        <div class="stat-value">34</div>
      </div>
      <div class="welcome-content">
        <!-- <h2 class="app-name">Moon Admin</h2> -->
        <!-- <p class="last-login-time">上次登录时间: {{ lastLoginTime }}</p> 显示上次登录时间 -->
        <p class="current-time">当前ip地址：<b>南京</b>；当前时间：<b>{{ currentTime }}</b></p>
      </div>
    </div>

    <!-- 项目动态时间轴 -->
    <div class="timeline-section">
      <h2>项目动态</h2>
      <div class="timeline">
        <div v-for="(update, index) in projectUpdates" :key="index" class="timeline-item">
          <div class="timeline-point"></div>
          <div class="timeline-content">
            <div class="update-time">{{ update.time }}</div>
            <div class="update-title">{{ update.title }}</div>
            <div class="update-desc">{{ update.description }}</div>
          </div>
        </div>
      </div>
    </div>
    <button @click="logout" class="logout-button">退出登录</button>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios' // 引入 Axios

const router = useRouter()

// 当前时间
const currentTime = ref(new Date().toLocaleString())
const lastLoginTime = ref('') // 初始化上次登录时间
let timer: ReturnType<typeof setInterval>

// 项目更新记录
const projectUpdates = ref([
{
    time: '2024-12-07 21:30',
    title: '修复个人联系方式添加失败BUG',
    description: '个人联系方式已经可以正常保存修改'
  },
{
    time: '2024-12-01 18:30',
    title: '新增首页上次登录时间显示',
    description: '添加了首页上次登录时间显示功能'
  },
  {
    time: '2024-11-30 14:30',
    title: '新增个人主页管理功能',
    description: '添加了个人资料编辑、头像上传等功能'
  },
  {
    time: '2024-11-28 16:45',
    title: '优化后台布局',
    description: '重构了后台管理界面，优化了导航菜单和路由配置'
  },
  {
    time: '2024-11-22 10:20',
    title: '初始化项目',
    description: '创建项目基础架构，配置开发环境'
  }
])

const isDropdownOpen = ref(false)

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

// 退出登录函数
const logout = () => {
  console.log('用户已退出登录');
  localStorage.removeItem('token') // 清除 token
  router.push('/login')
}

// 获取上次登录时间
const fetchLastLoginTime = async () => {
  const userId = '1'; // 替换为实际用户 ID
  try {
    const response = await axios.get(`http://localhost:5000/api/user/${userId}/last_login`);
    if (response.data.code === 200) {
      lastLoginTime.value = response.data.data; // 设置上次登录时间
    } else {
      console.error('获取上次登录时间失败:', response.data.message);
    }
  } catch (error) {
    console.error('请求错误:', error);
  }
}

onMounted(() => {
  fetchLastLoginTime(); // 组件加载时获取上次登录时间
  timer = setInterval(() => {
    currentTime.value = new Date().toLocaleString()
  }, 1000)
})

onUnmounted(() => {
  clearInterval(timer)
})
</script>

<style scoped>
.home {
  padding: 24px;
}
/* 头像 */
.logo {
  display: inline-block;
  width: 80px;
  height: 80px;
  padding: 10px;
  border-radius: 50%;
  margin-bottom: 16px;
}

/* 卡片 */
.stat-card {
  display: inline-block;
  width: 200px;
  text-align: center;
  background: rgb(237, 234, 234);
  padding: 24px;
  margin-left: 20px;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.stat-card h3 {
  color: #64748b;
  font-size: 20px;
  /* letter-spacing: 8px; */
  margin-bottom: 8px;
}

.welcome-name>p {
  font-size: 14px;
  color: #666;
}

.welcome-section {
  background: white;
  padding: 24px;
  border-radius: 8px;
  margin-bottom: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.current-time {
  color: #666;
  margin-top: 8px;
}

.last-login-time {
  color: #999; /* 上次登录时间的颜色 */
  margin-top: 8px;
}

/* 时间轴样式 */
.timeline-section {
  background: white;
  padding: 24px;
  border-radius: 8px;
  margin-bottom: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.timeline {
  position: relative;
  padding-left: 24px;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 2px;
  background: #e2e8f0;
}

.timeline-item {
  position: relative;
  padding-bottom: 24px;
}

.timeline-point {
  position: absolute;
  left: -29px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #2563eb;
  border: 2px solid white;
}

.update-time {
  color: #64748b;
  font-size: 14px;
  margin-bottom: 4px;
}

.update-title {
  font-weight: 500;
  margin-bottom: 4px;
}

.update-desc {
  color: #64748b;
  font-size: 14px;
}

h2 {
  font-size: 18px;
  font-weight: 500;
  margin-bottom: 16px;
  color: #1a1f36;
}

.logout-button {
  margin-top: 16px;
  padding: 8px 16px;
  background-color: #f44336; /* 红色背景 */
  color: white; /* 白色文字 */
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.logout-button:hover {
  background-color: #d32f2f; /* 悬停时的颜色 */
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
}

.nav-right {
  position: relative;
}

.username {
  cursor: pointer;
  color: #333;
}

.dropdown {
  position: relative;
}

.dropdown-content {
  position: absolute;
  right: 0;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 1;
}

.dropdown-item {
  display: block;
  padding: 8px 16px;
  text-decoration: none;
  color: #333;
}

.dropdown-item:hover {
  background: #f0f0f0;
}

.welcome-header {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}
</style>