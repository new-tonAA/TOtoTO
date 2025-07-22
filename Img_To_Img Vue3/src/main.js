import './assets/main.scss'

import { createApp } from 'vue'  //导入Vue
import ElementPlus from 'element-plus'  //导入element-plus
import 'element-plus/dist/index.css'  //导入element-plus的样式
import router from '@/router'
import App from './App.vue'  //导入app.vue
import {createPinia} from 'pinia'
import { createPersistedState } from 'pinia-persistedstate-plugin'
import locale from 'element-plus/dist/locale/zh-cn.js'

const app = createApp(App);  //创建应用实例
const pinia = createPinia();
const persist = createPersistedState();
pinia.use(persist)
app.use(pinia)
app.use(router)
app.use(ElementPlus,{locale});  //使用html元素
app.mount('#app')