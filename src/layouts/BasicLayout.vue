<template>
  <div class="basic-layout">
    <!-- 左侧边栏 -->
    <aside class="sidebar" :class="{ collapsed: isCollapsed }">
      <div class="logo">
        <router-link to="/profile" class="logo-link">
          <img src="@/assets/dmn1.jpg" alt="Logo">
          <span v-show="!isCollapsed">Moon Admin</span>
        </router-link>
      </div>
      <nav class="menu">
        <router-link to="/home" class="menu-item" exact-active-class="router-link-active">
          <i class="icon">H</i>
          <span v-show="!isCollapsed">首页</span>
        </router-link>
        <router-link to="/dashboard" class="menu-item" exact-active-class="router-link-active">
          <i class="icon">D</i>
          <span v-show="!isCollapsed">仪表盘</span>
        </router-link>
        <router-link to="/admin/profile" class="menu-item" exact-active-class="router-link-active">
          <i class="icon">M</i>
          <span v-show="!isCollapsed">个人主页管理</span>
        </router-link>
      </nav>
    </aside>

    <!-- 主容器 -->
    <div class="main-container" :class="{ 'collapsed': isCollapsed }">
      <header class="header">
        <div class="header-left">
          <button class="collapse-btn" @click="toggleCollapse">
            <i class="icon">≡</i>
          </button>
        </div>
        <div class="header-right">
          <div class="user-info" @click="toggleDropdown">
            <img src="@/assets/dmn1.jpg" alt="Avatar" class="avatar" />
            <span class="username">Moon Admin</span>
            <div v-if="isDropdownOpen" class="dropdown-content" @click.stop>
              <router-link to="/admin/profile" class="dropdown-item">个人中心</router-link>
              <button @click="logout" class="dropdown-item">退出登录</button>
            </div>
          </div>
        </div>
      </header>

      <main class="content">
        <router-view></router-view>
      </main>

      <Footer />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Footer from '@/components/Footer.vue'

const router = useRouter()
const isCollapsed = ref(false)
const isDropdownOpen = ref(false)

const toggleCollapse = () => {
  isCollapsed.value = !isCollapsed.value
}

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

// 退出登录函数
const logout = () => {
  console.log('用户已退出登录');
  localStorage.removeItem('token') // 清除 token
  router.push('/login') // 跳转到登录页面
}

// 点击空白处收起下拉菜单
onMounted(() => {
  const handleClickOutside = (event: MouseEvent) => {
    const dropdown = document.querySelector('.dropdown-content')
    const userInfo = document.querySelector('.user-info')
    if (dropdown && userInfo && !userInfo.contains(event.target as Node)) {
      isDropdownOpen.value = false
    }
  }
  
  document.addEventListener('click', handleClickOutside)

  // 清理事件监听器
  return () => {
    document.removeEventListener('click', handleClickOutside)
  }
})
</script>

<style scoped>
.basic-layout {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: 240px;
  background: #f7f9fc;
  border-right: 1px solid #eaedf3;
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
}

.sidebar.collapsed {
  width: 80px;
}

.logo {
  height: 64px;
  padding: 16px;
  border-bottom: 1px solid #eaedf3;
}

.logo-link {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: #1a1f36;
}

.logo img {
  width: 32px;
  height: 32px;
  border-radius: 8px;
}

.menu {
  padding: 16px 0;
}

.menu-item {
  display: flex;
  align-items: center;
  padding: 12px 24px;
  color: #1a1f36;
  text-decoration: none;
  gap: 12px;
}

.menu-item:hover {
  background: #edf2f7;
}

.menu-item.router-link-active {
  background: #e6efff;
  color: #2563eb;
}

.main-container {
  flex: 1;
  margin-left: 240px;
  display: flex;
  flex-direction: column;
  transition: all 0.3s;
}

.sidebar.collapsed + .main-container {
  margin-left: 80px;
}

.header {
  height: 64px;
  background: white;
  border-bottom: 1px solid #eaedf3;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-left {
  display: flex;
  align-items: center;
}

.collapse-btn {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  padding: 8px;
  color: #1a1f36;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 8px;
  position: relative;
}

.user-info img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
}

.username {
  cursor: pointer;
  color: #333;
}

.dropdown-content {
  position: absolute;
  right: 0;
  top: 40px; /* 调整下拉菜单的位置 */
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 1;
  min-width: 150px;
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

.content {
  flex: 1;
  padding: 24px;
  background: #f7f9fc;
}

.icon {
  font-style: normal;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>