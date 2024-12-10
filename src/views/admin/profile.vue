<template>
  <div class="admin-profile">
    <h1 class="page-title">个人主页管理</h1>

    <div class="profile-form">
      <div class="form-group">
        <label>网站标题</label>
        <input v-model="dataToUpdate.title" type="text" placeholder="请输入网站标题">
      </div>

      <div class="form-group">
        <label>个人简介</label>
        <textarea v-model="dataToUpdate.bio" placeholder="请输入个人简介"></textarea>
      </div>

      <div class="form-group">
        <label>头像 URL</label>
        <input v-model="dataToUpdate.avatar" type="text" placeholder="请输入头像的网络地址">
        <div class="latest-avatar">
          <h2>头像预览</h2>
          <img :src="latestAvatar" alt="Latest Avatar" v-if="latestAvatar" class="latest-avatar-preview">
        </div>
      </div>

      <div class="form-actions">
        <button class="save-avatar-btn" @click="saveAvatar">保存头像</button>
      </div>
      <br>
      <hr>
      <div class="form-group">
        <label>联系方式</label>
        <!-- <input v-model="dataToUpdate.email" type="email" placeholder="邮箱"> -->
        <input v-model="dataToUpdate.about_me" type="text" placeholder="关于我">
        <input v-model="dataToUpdate.github" type="text" placeholder="GitHub">
        <input v-model="dataToUpdate.qq" type="text" placeholder="QQ">
        <input v-model="dataToUpdate.wechat" type="text" placeholder="微信公众号">
        <button class="save-btn" @click="saveProfile">保存个人资料</button>
      </div>

      
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

const dataToUpdate = ref({
  title: 'Moon',
  bio: '世界和平',
  avatar: '', // 从后端获取的头像 URL
  email: 'example@example.com',
  github: '',
  qq: '',
  wechat: '',
  about_me: '',
})

const latestAvatar = ref(''); // 新增变量用于存储最新头像

const saveProfile = async () => {
  const userId = '1'; // 替换为实际用户 ID
  const dataToSend :{ github?: string; qq?: string; wechat?: string;about_me?: string }={};
  
  
  // 添加其他个人资料
  // formData.append('title', profile.value.title);
  // formData.append('bio', profile.value.bio);
  // formData.append('email', dataToUpdate.value.email);
  // dataToUpdate.git('github', dataToUpdate.value.github);
  // dataToUpdate.append('qq', dataToUpdate.value.qq);
  // dataToUpdate.append('wechat', dataToUpdate.value.wechat);
  // 仅添加非空字段
  if (dataToUpdate.value.github) {
    dataToSend.github = dataToUpdate.value.github;
  }
  if (dataToUpdate.value.qq) {
    dataToSend.qq = dataToUpdate.value.qq;
  }
  if (dataToUpdate.value.wechat) {
    dataToSend.wechat = dataToUpdate.value.wechat;
  }
  if (dataToUpdate.value.about_me) {
    dataToSend.about_me = dataToUpdate.value.about_me;
  }

  try {
    const response = await axios.put(`http://localhost:5000/api/user/${userId}/contacts`, dataToSend, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    if (response.data.code === 200) {
      alert('个人资料更新成功！');
    } else {
      alert('更新失败，请重试！');
    }
  } catch (error) {
    console.error('保存失败:', error);
    alert('保存失败，请重试');
  }
}

const saveAvatar = async () => {
  const userId = '1'; // 替换为实际用户 ID
  const formData = new FormData();
  
  // 添加头像 URL
  formData.append('avatar', dataToUpdate.value.avatar);
  
  try {
    const response = await axios.patch(`http://localhost:5000/api/user/${userId}/avatar`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    if (response.data.code === 200) {
      alert('头像更新成功！');
      latestAvatar.value = response.data.data; // 更新最新头像
    } else {
      alert('头像更新失败，请重试！');
    }
  } catch (error) {
    console.error('头像保存失败:', error);
    alert('头像保存失败，请重试');
  }
}

// 在组件加载时获取用户信息，包括头像
const fetchUserProfile = async (userId: string): Promise<void> => {
  const response = await axios.get(`http://localhost:5000/api/user/${userId}`);
  if (response.data.code === 200) {
    dataToUpdate.value = response.data.data; // 更新用户信息，包括头像
    // dataToUpdate.value.avatar = response.data.data.avatar;
    latestAvatar.value = dataToUpdate.value.avatar;
    // dataToUpdate.value.avatar = response.data.data.avatar; // 初始化最新头像
  }
};


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
// 在组件加载时调用
// fetchUserProfile(1.toString()); // 使用 toString() 方法
// 或者
onMounted(() => {
  const userId = '1'; // 替换为实际用户 ID
  fetchUserProfile(userId); // 获取用户基本信息
  queryProfile(userId); // 获取用户联系方式
});

// fetchUserProfile(`${1}`); // 使用模板字面量
</script>

<style scoped>
.admin-profile {
  padding: 24px;
}

.page-title {
  margin-bottom: 24px;
  font-size: 24px;
  font-weight: 500;
  color: #1a1f36;
}

.profile-form {
  background: white;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 24px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: #64748b;
  font-weight: 500;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
  margin-bottom: 8px;
}

.form-group textarea {
  height: 100px;
  resize: vertical;
}

.save-btn {
  padding: 12px 24px;
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
}

.save-btn:hover {
  background: #1d4ed8;
}

.save-avatar-btn {
  padding: 12px 24px;
  background: #4caf50; /* 绿色背景 */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  /* margin-left: 10px; 添加左边距 */
}

.save-avatar-btn:hover {
  background: #388e3c; /* 深绿色背景 */
}

/* 新增样式 */
.latest-avatar {
  margin-top: 24px;
}

.latest-avatar-preview {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  object-fit: cover;
}
</style>