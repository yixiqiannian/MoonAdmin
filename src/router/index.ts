import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import BasicLayout from '@/layouts/BasicLayout.vue';
import PublicProfile from '@/views/public/profile.vue'; // 公共个人资料组件

const routes: Array<RouteRecordRaw> = [
  {
    path: '/profile',
    name: 'PublicProfile',
    component: PublicProfile, // 指向公共个人资料组件
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/login/index.vue'),
  },
  {
    path: '/',
    redirect: '/profile',
  },
  {
    path: '/home',
    component: BasicLayout,
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import('@/views/home/index.vue'),
      },
    ],
  },
  {
    path: '/dashboard',
    component: BasicLayout,
    children: [
      {
        path: '',
        name: 'Dashboard',
        component: () => import('@/views/dashboard/index.vue'),
      },
    ],
  },
  {
    path: '/admin',
    component: BasicLayout,
    children: [
      {
        path: 'profile',
        name: 'AdminProfile',
        component: () => import('@/views/admin/profile.vue'),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 路由守卫
router.beforeEach((to, from, next) => {
  const isLoggedIn = localStorage.getItem('token'); // 检查用户是否登录

  // 允许访问 /profile 和 /login 路径
  if (to.path === '/profile' || to.path === '/login') {
    next(); // 允许访问
  } else if (!isLoggedIn) {
    // 如果用户未登录且访问其他路径，重定向到登录页面
    next('/login');
  } else {
    next(); // 继续访问
  }
});

export default router;