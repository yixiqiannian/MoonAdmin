import router from './index'
import { useUserStore } from '@/store/user'

const whiteList = ['/login', '/profile']

router.beforeEach(async (to, from, next) => {
  const userStore = useUserStore()
  const token = localStorage.getItem('token')

  if (token) {
    if (to.path === '/login') {
      next({ path: '/' })
    } else {
      if (!userStore.userInfo) {
        try {
          await userStore.fetchUserInfo(token)
          next({ ...to, replace: true })
        } catch (error) {
          userStore.logout()
          next(`/login?redirect=${to.path}`)
        }
      } else {
        next()
      }
    }
  } else {
    if (whiteList.includes(to.path)) {
      next()
    } else {
      next(`/login?redirect=${to.path}`)
    }
  }
})

router.afterEach(() => {
  // 路由切换后的操作，比如关闭loading等
})

export default router 