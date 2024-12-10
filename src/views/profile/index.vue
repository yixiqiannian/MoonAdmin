<template>
  <div class="profile-manage">
    <h2>个人主页管理</h2>
    
    <form class="edit-form" @submit.prevent="handleSubmit">
      <div class="form-item">
        <label>用户名</label>
        <input v-model="form.username" type="text" required>
      </div>
      
      <div class="form-item">
        <label>邮箱</label>
        <input v-model="form.email" type="email" required>
      </div>

      <div class="form-item">
        <label>联系方式</label>
        <input v-model="form.contact" type="text" required>
      </div>
      
      <button type="submit" class="submit-btn">保存更改</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const form = ref({
  username: '',
  email: '',
  contact: ''
});

const handleSubmit = async () => {
  const userId = '1'; // 替换为实际用户 ID
  const response = await fetch(`http://localhost:5000/api/user/${userId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(form.value),
  });
  const data = await response.json();
  if (data.code === 200) {
    alert('更新成功！');
  } else {
    alert('更新失败，请重试！');
  }
};
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