<template>
  <footer class="site-footer">
    <div class="footer-content">
      <div class="running-time">
        网站已运行: {{ runningTime }}
      </div>
      <div class="beian-info">
        <a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener">
          粤ICP备2024019082号-1
        </a>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const runningTime = ref('')
const startTime = new Date('2024-11-20')

const calculateRunningTime = () => {
  const now = new Date()
  const diff = now.getTime() - startTime.getTime()
  
  const days = Math.floor(diff / (1000 * 60 * 60 * 24))
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60))
  const seconds = Math.floor((diff % (1000 * 60)) / 1000)
  
  runningTime.value = `${days}天${hours}小时${minutes}分${seconds}秒`
}

onMounted(() => {
  calculateRunningTime()
  setInterval(calculateRunningTime, 1000)
})
</script>

<style scoped>
.site-footer {
  margin-top: auto;
  padding: 20px;
  background: white;
  box-shadow: 0 -1px 2px rgba(0,0,0,0.1);
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
  color: #666;
  font-size: 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.beian-info a {
  color: #666;
  text-decoration: none;
  transition: color 0.3s;
}

.beian-info a:hover {
  color: #1890ff;
}
</style>

export default {
  name: 'Footer'
} 