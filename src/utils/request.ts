import axios from 'axios'

const request = axios.create({
  baseURL: 'http://localhost:5000/api',
  timeout: 5000
})

// 请求拦截器
request.interceptors.request.use(
  config => {
    // 可以在这里添加token等认证信息
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

// 响应拦截器
request.interceptors.response.use(
  response => {
    const res = response.data
    if (res.code !== 200) {
      // 处理错误
      return Promise.reject(new Error(res.message || 'Error'))
    }
    return res
  },
  error => {
    console.error('请求错误:', error)
    return Promise.reject(error)
  }
)

export default request