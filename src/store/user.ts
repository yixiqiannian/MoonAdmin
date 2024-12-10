import { defineStore } from 'pinia'
import { login, getUserInfo, updateUserInfo } from '@/api/user'
import type { LoginData, UserInfo } from '@/api/user'

interface UserState {
  userInfo: UserInfo | null
  token: string | null
}

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    userInfo: null,
    token: localStorage.getItem('token') || null
  }),

  getters: {
    isLoggedIn: (state) => !!state.token,
    username: (state) => state.userInfo?.username,
    avatar: (state) => state.userInfo?.avatar
  },

  actions: {
    async login(loginData: LoginData) {
      try {
        const res = await login(loginData)
        this.token = res.data.token
        localStorage.setItem('token', res.data.token)
        await this.fetchUserInfo(res.data.id)
        return res
      } catch (error) {
        console.error('Login failed:', error)
        throw error
      }
    },

    async fetchUserInfo(userId: string) {
      try {
        const res = await getUserInfo(userId)
        this.userInfo = res.data
        return res.data
      } catch (error) {
        console.error('Fetch user info failed:', error)
        throw error
      }
    },

    logout() {
      this.token = null
      this.userInfo = null
      localStorage.removeItem('token')
    }
  }
}) 