import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  //配置代理
  server:{
      proxy: {
      '/map': {
        target: 'http://localhost:8010',
        changeOrigin: true,
        //rewrite: (path) => path.replace(/^\/map/, '/map')
      },
      '/api':{
        target:'http://localhost:8010',//后端服务器地址
        changeOrigin:true,
        rewrite: (path) => path.replace(/^\/api/, '')//将原有请求路径中的api替换为''
      },
      '/review': {              // 新增这个
        target: 'http://localhost:8010',
        changeOrigin: true,
      }
    }
  }
})
