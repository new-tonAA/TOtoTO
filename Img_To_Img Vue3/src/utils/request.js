//导入axios  npm install axios
import axios from 'axios';
//定义一个变量,记录公共的前缀  ,  baseURL
const baseURL = '/api';
const instance = axios.create({baseURL})

import {useTokenStore} from '@/stores/token.js'

//添加请求拦截器
instance.interceptors.request.use(
    (config)=>{
        //请求前的回调
        //添加token
        const tokenStore = useTokenStore();
        //判断有没有token
        if(tokenStore.token){
            config.headers.Authorization = tokenStore.token
        }
        return config;
    },
    (err)=>{
        //请求错误的回调
        Promise.reject(err)
    }
)


//添加响应拦截器
instance.interceptors.response.use(
    result=>{
        return result.data;
    },
    err=>{
        const tokenStore = useTokenStore();
        if(err.response.data.msg === 'Token has expired' && err.response.status===401){
            tokenStore.removeToken()
            alert("登录已过期")
        }
        if(err.response.status===401 || err.response.status===400){
            alert(err.response.data.error)
        }
        else{
            alert('服务异常');
        }
        return Promise.reject(err);//异步的状态转化成失败的状态
    }
)

export default instance;