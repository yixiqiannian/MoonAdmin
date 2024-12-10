<template>
  <div class="dashboard">
    <div class="stats-grid">
      <div class="stat-card">
        <h3>访问量</h3>
        <div class="stat-value">1,234</div>
      </div>
      <div class="stat-card">
        <h3>用户数</h3>
        <div class="stat-value">567</div>
      </div>
      <div class="stat-card">
        <h3>订单数</h3>
        <div class="stat-value">89</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// 可以添加数据获取逻辑
</script>

<style scoped>
.dashboard {
  padding: 24px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}

.stat-card {
  background: white;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.stat-card h3 {
  color: #64748b;
  font-size: 14px;
  margin-bottom: 8px;
}

.stat-value {
  font-size: 32px;
  font-weight: 600;
  color: #1a1f36;
}
</style> 