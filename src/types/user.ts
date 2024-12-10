export interface LoginForm {
  username: string
  password: string
}

export interface UserInfo {
  id: number
  username: string
  email: string
  avatar?: string
  roles: string[]
} 