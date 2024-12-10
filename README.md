# Moonlove Admin

一个基于 Vue 3 + TypeScript 的后台管理系统。

## 项目结构

```
src/
├── assets/               # 静态资源
│   └── dmn1.jpg         # Logo和头像图片
├── components/          # 公共组件
│   ├── Footer.vue       # 页脚组件（包含运行时间和备案信息）
│   └── icons/           # 图标组件
│       ├── EmailIcon.vue
│       ├── GithubIcon.vue
│       ├── QQIcon.vue
│       └── WechatIcon.vue
├── layouts/             # 布局组件
│   └── BasicLayout.vue  # 基础布局（包含侧边栏和顶部导航）
├── router/              # 路由配置
│   └── index.ts        # 路由定义和守卫
├── store/               # 状态管理
│   └── user.ts         # 用户状态管理
├── views/               # 页面组件
│   ├── admin/
│   │   └── profile.vue # 后台个人主页管理
│   ├── dashboard/
│   │   └── index.vue   # 仪表盘页面
│   ├── home/
│   │   └── index.vue   # 首页（包含项目动态）
│   ├── login/
│   │   └── index.vue   # 登录页面
│   └── public/
│       └── profile.vue  # 公开的个人主页
└── App.vue             # 根组件
```

## 主要功能

1. 布局系统
   - 可折叠侧边栏
   - 顶部导航栏
   - 响应式设计

2. 路由系统
   - 基于角色的路由控制
   - 路由守卫实现登录控制
   - 支持嵌套路由

3. 个人主页
   - 公开访问的个人主页
   - 后台个人信息管理
   - 支持头像上传

4. 项目动态
   - 时间轴展示
   - 更新记录管理

5. 统计面板
   - 访问量统计
   - 用户数据统计
   - 订单数据展示

## 近期更新记录
### 2024-12-01
- 新增首页上次登录时间显示

### 2024-11-30
- 新增个人主页管理功能
- 添加了个人资料编辑功能
- 实现了头像上传功能

### 2024-11-30
- 优化后台布局
- 重构了导航菜单
- 修复了路由配置

### 2024-11-30
- 初始化项目
- 配置基础开发环境
- 创建项目架构

## 技术栈

- Vue 3
- TypeScript
- Vue Router
- Pinia
- Axios
- Vite

## 开发说明

1. 安装依赖
```bash
npm install
```

2. 启动开发服务器
```bash
npm run dev
```

3. 构建生产版本
```bash
npm run build
```

## 注意事项

1. 确保 Node.js 版本 >= 16
2. 开发时需要配置正确的环境变量
3. 部署时需要配置正确的服务器信息

## 备案信息

- ICP备案号：粤ICP备2024019082号-1

## 作者

- Moonlove
- Email: example@example.com
- GitHub: github.com/moonlove

```
moonlove
├─ .env.development
├─ .gitignore
├─ babel.config.js
├─ backend
│  └─ app.py
├─ index.html
├─ package-lock.json
├─ package.json
├─ pnpm-lock.yaml
├─ public
│  └─ favicon.ico
├─ README.md
├─ src
│  ├─ api
│  │  └─ user.ts
│  ├─ App.vue
│  ├─ assets
│  │  ├─ dmn1.jpg
│  │  └─ logo.png
│  ├─ components
│  │  ├─ Footer.vue
│  │  ├─ HelloWorld.vue
│  │  └─ icons
│  │     ├─ EmailIcon.vue
│  │     ├─ GithubIcon.vue
│  │     ├─ QQIcon.vue
│  │     └─ WechatIcon.vue
│  ├─ layouts
│  │  └─ BasicLayout.vue
│  ├─ main.ts
│  ├─ router
│  │  ├─ index.ts
│  │  ├─ modules
│  │  │  ├─ index.ts
│  │  │  └─ look-forward.ts
│  │  └─ permission.ts
│  ├─ shims-vue.d.ts
│  ├─ store
│  │  └─ user.ts
│  ├─ types
│  │  └─ user.ts
│  ├─ utils
│  │  ├─ index.ts
│  │  └─ request.ts
│  └─ views
│     ├─ AboutView.vue
│     ├─ admin
│     │  ├─ profile-manage.vue
│     │  └─ profile.vue
│     ├─ dashboard
│     │  └─ index.vue
│     ├─ home
│     │  └─ index.vue
│     ├─ HomeView.vue
│     ├─ login
│     │  └─ index.vue
│     ├─ profile
│     │  └─ index.vue
│     └─ public
│        └─ profile.vue
├─ structure.txt
├─ tsconfig.json
├─ vite.config.ts
├─ vue.config.js
└─ yarn.lock

```