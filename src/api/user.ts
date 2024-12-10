import request from '@/utils/request'

export interface LoginData {
  username: string
  password: string
}

export interface UserInfo {
  id: string
  username: string
  email: string
  avatar: string
  role: string
}

export const login = (data: LoginData) => {
  return request({
    url: '/login',
    method: 'post',
    data
  })
}

export const getUserInfo = (userId: string) => {
  return request({
    url: `/user/${userId}`,
    method: 'get'
  })
}

export const updateUserInfo = (userId: string, data: Partial<UserInfo>) => {
  return request({
    url: `/user/${userId}`,
    method: 'put',
    data
  })
} 