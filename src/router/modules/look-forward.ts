import type { RouteRecordRaw } from 'vue-router'

const lookForward: RouteRecordRaw = {
  path: '/look-forward',
  name: 'look-forward',
  component: () => import('@/views/profile/index.vue'),
  meta: {
    title: '个人中心',
    requiresAuth: true,
    icon: 'mdi:account',
    order: 2
  }
}

export default lookForward 