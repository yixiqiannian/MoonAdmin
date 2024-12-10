<template>
  <div class="profile-manage">
    <h2>个人主页管理</h2>
    
    <form class="edit-form" @submit.prevent="handleSubmit">
      <div class="form-item">
        <label>头像11</label>
        <div class="avatar-upload">
          <img :src="form.avatar" alt="Avatar" v-if="form.avatar" class="avatar-preview">
          <input type="file" @change="handleAvatarChange" accept="image/*" required>
        </div>
      </div>
      
      <div class="form-item">
        <label>姓名</label>
        <input v-model="form.name" type="text" required>
      </div>
      
      <div class="form-item">
        <label>简介</label>
        <input v-model="form.bio" type="text" required>
      </div>
      
      <button type="submit" class="submit-btn">保存更改</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const form = ref({
  avatar: '',
  name: 'Moon',
  bio: '世界和平',
})

const handleAvatarChange = (event: Event) => {
  console.log('文件选择事件触发');
  const file = (event.target as HTMLInputElement).files?.[0];
  if (file) {
    console.log('选择的文件:', file);
    const reader = new FileReader();
    reader.onload = (e) => {
      form.value.avatar = e.target?.result as string; // 设置头像预览
    };
    reader.readAsDataURL(file); // 读取文件为 Data URL
  } else {
    console.log('没有选择文件');
  }
}

const handleSubmit = async () => {
  const userId = '1'; // 替换为实际用户 ID
  const formData = new FormData()
  const fileInput = document.querySelector('input[type="file"]') as HTMLInputElement | null;
  if (fileInput && fileInput.files && fileInput.files[0]) {
    formData.append('avatar', fileInput.files[0]);
  }
  formData.append('name', form.value.name)
  formData.append('bio', form.value.bio)

  try {
    const response = await axios.put(`http://localhost:5000/api/user/${userId}/avatar`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    if (response.data.code === 200) {
      alert('头像更新成功！')
      form.value.avatar = response.data.data; // 更新头像预览
    } else {
      alert('更新失败，请重试！')
    }
  } catch (error) {
    console.error('保存失败:', error)
    alert('保存失败，请重试')
  }
}
</script>

<style scoped>
.profile-manage {
  padding: 24px;
}

.edit-form {
  max-width: 600px;
  background: white;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.form-item {
  margin-bottom: 20px;
}

.form-item label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

.form-item input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.avatar-upload {
  display: flex;
  align-items: center;
  gap: 16px;
}

.avatar-preview {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  object-fit: cover;
}

.submit-btn {
  background: #1890ff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

.submit-btn:hover {
  background: #40a9ff;
}
</style> 