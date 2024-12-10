<template>
  <div class="public-profile">
    <header class="profile-nav">
      <h1>Moon</h1>
      <div class="nav-right">
        <div class="dropdown">
          <span @click="toggleDropdown" class="username">Moon Admin</span>
          <div v-if="isDropdownOpen" class="dropdown-content">
            <!-- <router-link to="/login" class="dropdown-item">登录</router-link> -->
            <router-link to="/admin/profile" class="dropdown-item">个人中心</router-link>
            <p @click="logout" class="dropdown-item">退出登录</p>
          </div>
        </div>
      </div>
    </header>

    <div class="profile-content">
      <div class="profile-header">
        <!-- <img :src="profile.avatar" alt="Avatar" class="avatar"> -->
        <img :src="latestAvatar" alt="Avatar" class="avatar" v-if="latestAvatar" >
        <h1>{{ profile.name }}</h1>
        <p class="bio">{{ profile.bio }}</p>
      </div>
      
      <section class="profile-details">
        <div class="daily-quote" :title="dailyQuote">
          <h2>舔狗日记</h2>
          <p>{{ truncatedQuote }}</p>
        </div>

        <div class="about-me">
          <h2>关于我</h2>
          <p>{{ dataToUpdate.about_me }}</p>
        </div>
        
        <div class="contact-info">
          <h2>联系方式</h2>
          <ul>
            <li>
              <EmailIcon class="icon" />
              {{ profile.email }}
            </li>
            <li>
              <GithubIcon class="icon" />
              {{ dataToUpdate.github }}
            </li>
            <li>
              <QQIcon class="icon" />
              {{ dataToUpdate.qq }}
            </li>
            <li>
              <WechatIcon class="icon" />
              {{ dataToUpdate.wechat }}
            </li>
          </ul>
        </div>
      </section>
    </div>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useUserStore } from '@/store/user'
import axios from 'axios'
import EmailIcon from '@/components/icons/EmailIcon.vue'
import GithubIcon from '@/components/icons/GithubIcon.vue'
import QQIcon from '@/components/icons/QQIcon.vue'
import WechatIcon from '@/components/icons/WechatIcon.vue'
import Footer from '@/components/Footer.vue'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const dailyQuote = ref('')
const isDropdownOpen = ref(false)
const router = useRouter()
const latestAvatar = ref('');
const userId = '1';

const profile = ref({
  name: 'Moon',
  avatar: '/src/assets/dmn1.jpg',
  bio: '世界和平',
  about: '也许明天会好呢',
  email: '123456789@qq.com',
})
const dataToUpdate = ref({
  github: '',
  qq: '',
  wechat: '',
  about_me: ''
})
// 联系方式
const queryProfile = async (userId:string): Promise<void> => {
  const response = await axios.get(`http://localhost:5000/api/user/${userId}/contacts`);
  if (response.data.code === 200) {
    dataToUpdate.value = response.data.data;
    dataToUpdate.value.github = response.data.data.github;
    dataToUpdate.value.qq = response.data.data.qq;
    dataToUpdate.value.wechat = response.data.data.wechat;
    dataToUpdate.value.about_me = response.data.data.about_me;
  }
}


const fetchUserProfile = async (userId: string):Promise<void> => {
  const response = await axios.get(`http://localhost:5000/api/user/${userId}`);
  if (response.data.code === 200) {
    profile.value = response.data.data;
    // 获取头像
    latestAvatar.value = profile.value.avatar;
    // 获取username
    profile.value.name = response.data.data.username;

    // console.log(latestAvatar.value);
  }else{
    latestAvatar.value = '/src/assets/dmn1.jpg';
    // console.log(latestAvatar.value);
  } 
}
onMounted(() => {
  fetchUserProfile(userId);
  queryProfile(userId);
});

const truncatedQuote = computed(() => {
  if (dailyQuote.value.length > 50) {
    return dailyQuote.value.slice(0, 50) + '...'
  }
  return dailyQuote.value
})

const fetchDailyQuote = async () => {
  try {
    const response = await axios.get('https://apis.tianapi.com/saylove/index', {
      params: {
        key: '81b39e09c6748897fefc0691b70f76de'
      }
    })
    if (response.data.code === 200) {
      dailyQuote.value = response.data.result.content
    }
  } catch (error) {
    console.error('获取每日一言失败:', error)
  }
}

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

// 退出登录函数
const logout = () => {
  // 这里添加退出登录的逻辑，例如清除用户信息
  console.log('用户已退出登录');
  localStorage.removeItem('token') // 清除 token
  // 跳转到登录页面
  router.push('/login')
}

onMounted(() => {
  fetchDailyQuote()
})
</script>

<style scoped>
.public-profile {
  min-height: 100vh;
  background: #f0f2f5;
  display: flex;
  flex-direction: column;
}

.profile-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  background: white;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.nav-right {
  display: flex;
  gap: 16px;
  position: relative;
}

.nav-button {
  padding: 8px 16px;
  border-radius: 4px;
  background: #1890ff;
  color: white;
  text-decoration: none;
  transition: background 0.3s;
}

.nav-button:hover {
  background: #40a9ff;
}

.profile-content {
  max-width: 800px;
  margin: 40px auto;
  padding: 0 20px;
}

.profile-header {
  text-align: center;
  margin-bottom: 40px;
}

.avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  margin-bottom: 20px;
}

.bio {
  color: #666;
  font-size: 1.2em;
}

.profile-details {
  display: grid;
  gap: 40px;
}

.daily-quote, .about-me, .contact-info {
  background: white;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.daily-quote p {
  color: #666;
  cursor: help;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  line-height: 1.5;
}

.daily-quote p:hover {
  overflow: visible;
  -webkit-line-clamp: unset;
  background: white;
  position: relative;
  z-index: 1;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-radius: 4px;
  padding: 10px;
  margin: -10px;
}

h2 {
  margin-bottom: 16px;
  color: #333;
}

.contact-info ul {
  list-style: none;
  padding: 0;
}

.contact-info li {
  margin: 8px 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.icon {
  width: 20px;
  height: 20px;
  color: #666;
}

.dropdown {
  position: relative;
}

.dropdown-button {
  background: #1890ff;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}

.dropdown-content {
  position: absolute;
  right: 0;
  width: 100px;
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

.nav-right {
  position: relative;
}

/* .avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  cursor: pointer;
} */

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

.username {
  cursor: pointer;
  color: #333;
}
</style>