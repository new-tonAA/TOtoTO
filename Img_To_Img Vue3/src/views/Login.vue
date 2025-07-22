<script setup>
import { User, Lock, Message } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { ref,computed, onBeforeUnmount } from 'vue'

//控制注册与登录表单的显示，默认显示注册
const isRegister = ref(false);
//控制邮箱的注册与登录表单的显示，默认不显示邮箱操作
const isEmail=ref(false) 
//验证码按钮显示
const countdown = ref(0)
const timer = ref(null)
//定义数据类型
const registerData = ref({
    username:'',
    password:'',
    repassword:'',
    email:'',
    verify:'',     //验证码
    role:0,  //管理员的账号不能通过注册实现
})

//校验密码
const checkRePassword = (rule,value,callback)=>{
    if(value === ''){
        callback(new Error('请再次确认密码'))
    } else if(value !== registerData.value.password){
        callback(new Error('请确保两次输入的密码一样'))
    } else{
        callback()
    }
}

//校验邮箱
const check_email = (rule,value,callback)=>{

    const re = /^([a-zA-Z0-9]+[-_\.]?)+@[a-zA-Z0-9]+\.[a-z]+$/;
    if (value !== '' && !re.test(value)){
        callback(new Error('不合规范'))
    } else{
        callback()
    }
}

//定义表单校验规则
const rules = {
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' },
        { min: 5, max: 16, message: '长度为5~16位非空字符', trigger: 'blur' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' },  //blur只有提交的时候才会验证
        { min: 5, max: 16, message: '长度为5~16位非空字符', trigger: 'blur' }
    ],
    repassword: [
        { require:true, checkRePassword, trigger: 'blur' } //blur失去焦点时触发验证
    ],
    email: [
        { required:true, validator: check_email, trigger:'blur'}
    ],
}

import {userRegisterService, userEmail,userRegisterVerify, userEmailVerify, userLoginService,userRegisterEmail} from '@/api/user.js'
import {useTokenStore} from '@/stores/token.js'
import {useRouter} from 'vue-router'
const router = useRouter()
const tokenStore = useTokenStore();

const register = async () => {  //注册接口
    let result = await userRegisterService(registerData.value);
    ElMessage.success(result.message?result.message:'注册成功');
    isEmail.value= true
}

const register_email = async() =>{  //注册时绑定邮箱
    let result = await userRegisterEmail(registerData.value);
    sendCode(); //发送验证码成功后开始倒计时
    ElMessage.success(result.message?result.message:'验证码已经发送,120秒后验证码过期')
}

const register_email_verify = async() =>{  //绑定邮箱时验证码核对
    let result = await userRegisterVerify(registerData.value);
    ElMessage.success(result.message?result.message:'验证成功')
    clearRegisterData();
    isEmail.value= false;
    isRegister.value=false;
    countdown.value=0;
}

const login_email = async() =>{
    let result = await userEmail(registerData.value);
    sendCode(); //发送验证码成功后开始倒计时
    ElMessage.success(result.message?result.message:'验证成功')
}

const login_email_verify = async() =>{  //邮箱登录验证码核对
    let result = await userEmailVerify(registerData.value);
    ElMessage.success(result.message?result.message:'验证成功')
    countdown.value=0
    tokenStore.setToken(result.token);
    clearRegisterData();
    //跳转到首页，借助路由完成跳转
    router.push('/')
}

const login = async() =>{
    //调用接口,完成登录
    let result = await userLoginService(registerData.value);
    ElMessage.success(result.message?result.message:'登录成功')
    //把得到的token存储到pinia中
    tokenStore.setToken(result.token);
    //把得到的userInfo存储到pinia中
    //跳转到首页，借助路由完成跳转
    router.push('/')
}

const pass =async() =>{
    router.push('/')  //不登陆以无账号的状态下使用
}

//定义函数,清空数据模型的数据
const clearRegisterData = ()=>{
    registerData.value={
        username:'',
        password:'',
        repassword:'',
        email:'',
        verify:''
    }
}

const buttonText = computed(() => {
  return countdown.value > 0 ? `${countdown.value}s` : '获取验证码'
})

const sendCode = () => {
  if (countdown.value > 0) return
  
  console.log('发送验证码...')
  
  countdown.value = 120
  timer.value = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(timer.value)
      timer.value=null
    }
  }, 1000)
}
onBeforeUnmount(() => {
  if (timer.value) {
    clearInterval(timer.value)
  }
})
</script>

<template>
    <el-row class="login-page">
       <div class="container">
            <el-col :span="16" :offset="4" class="form">
                <!-- 注册表单 -->
                <el-form ref="form" size="large" autocomplete="off" v-if="isRegister&&!isEmail" :model="registerData" :rules="rules">
                    <el-form-item>
                        <h1>注册</h1>
                    </el-form-item>
                    <el-form-item prop="username">
                        <el-input :prefix-icon="User" placeholder="请输入用户名" v-model="registerData.username"></el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input :prefix-icon="Lock" type="password" placeholder="请输入密码"
                            v-model="registerData.password"></el-input>
                    </el-form-item>
                    <el-form-item prop="rePassword">
                        <el-input :prefix-icon="Lock" type="password" placeholder="请输入再次密码"
                            v-model="registerData.repassword"></el-input>
                    </el-form-item>
                    <!-- 注册按钮 -->
                    <el-form-item>
                        <el-button class="button" type="primary" auto-insert-space @click="register">
                            注册
                        </el-button>
                    </el-form-item>
                    <el-form-item class="flex">
                        <el-link type="info" :underline="false" @click="isRegister = false;clearRegisterData()">
                            ← 返回
                        </el-link>
                    </el-form-item>
                </el-form>
                <!-- 注册邮箱绑定表单 -->
                <el-form ref="form" size="large" autocomplete="off" v-if="isRegister && isEmail" :model="registerData" :rules="rules">
                    <el-form-item>
                        <h1>邮箱绑定</h1>
                    </el-form-item>
                     <el-form-item prop="email">
                        <el-input :prefix-icon="Message" placeholder="请输入邮箱(可选)" v-model="registerData.email"></el-input>
                    </el-form-item>
                    <el-form-item prop="verify">
                        <el-input placeholder="请输入验证码"
                            v-model="registerData.verify"></el-input>
                        <el-button class ="code-btn" :disabled="countdown > 0" @click="register_email">
                            {{ buttonText }}
                        </el-button>
                    </el-form-item>
                    
                    <!-- 邮箱绑定按钮 -->
                    <el-form-item>
                        <el-button class="button" type="primary" auto-insert-space @click="register_email_verify">
                            邮箱绑定
                        </el-button>
                    </el-form-item>
                    <el-form-item>
                        <el-button class="button" type="primary" auto-insert-space @click="clearRegisterData;isEmail= false;isRegister=false">
                            跳过
                        </el-button>
                    </el-form-item>
                </el-form>
                <!-- 登录表单 -->
                <el-form ref="form" size="large" autocomplete="off" v-else-if="!isRegister && !isEmail" :model="registerData" :rules="rules">
                    <el-form-item>
                        <h1>登录</h1>
                    </el-form-item>
                    <el-form-item prop="username">
                        <el-input :prefix-icon="User" placeholder="请输入用户名" v-model="registerData.username"></el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input name="password" :prefix-icon="Lock" type="password" placeholder="请输入密码" v-model="registerData.password"></el-input>
                    </el-form-item>
                    <el-form-item class="flex">
                        <div class="flex">
                            <el-checkbox>记住我</el-checkbox>
                            <el-link type="primary" :underline="false" @click="isEmail=true">忘记密码？</el-link>
                        </div>
                    </el-form-item>
                    <!-- 登录按钮 -->
                    <el-form-item>
                        <el-button class="button" type="primary" auto-insert-space @click="login">登录</el-button>
                    </el-form-item>
                    <el-form-item>
                        <el-button class="button" type="primary" auto-insert-space @click="pass">暂不登录</el-button>
                    </el-form-item>
                    <el-form-item class="flex">
                        <el-link type="info" :underline="false" @click="isRegister = true;clearRegisterData()">
                            注册 →
                        </el-link>
                    </el-form-item>
                </el-form>
                <!-- 邮箱登录表单 -->
                <el-form ref="form" size="large" autocomplete="off" v-if="!isRegister && isEmail" :model="registerData" :rules="rules">
                       <el-form-item>
                        <h1>邮箱登录</h1>
                    </el-form-item>
                     <el-form-item prop="email">
                        <el-input :prefix-icon="Message" placeholder="请输入邮箱" v-model="registerData.email"></el-input>
                    </el-form-item>
                    <el-form-item prop="verify">
                        <el-input type="verify" placeholder="请输入验证码"
                            v-model="registerData.verify"></el-input>
                    <el-button class ="code-btn" :disabled="countdown > 0" @click="login_email">
                            {{ buttonText }}
                    </el-button>
                </el-form-item>
                <!--邮箱登录按钮  -->
                    <el-form-item>
                        <el-button class="button" type="primary" auto-insert-space @click="login_email_verify">登录</el-button>
                    </el-form-item>
                    <el-form-item class="flex">
                        <el-link type="info" :underline="false" @click="isEmail = false;clearRegisterData()">
                            ← 返回
                        </el-link>
                    </el-form-item>
                </el-form>
            </el-col>
        </div>
    </el-row>
</template>


<style lang="scss" scoped>
/* 样式 */
.login-page {
    position: absolute; top: 50%; 
    left: 50%; transform: translate(-50%, -50%);

    .container {
        width: 375px;
        height: 450px;
        background-color: #fff;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        position: relative;
        border-radius: 20px;
        margin: 20px;

        .form {
        display: flex;
        flex-direction: column;
        justify-content: center;
        user-select: none;

            .title {
                margin: 0 auto;
            }

            .button {
                width: 100%;
            }

            .flex {
                width: 100%;
                display: flex;
                justify-content: space-between;
            }

            .code-btn {
                width: 100px;
                height: 20px;
                position: absolute;
                top: 10px;
                right: 5px;
                z-index: 222;
                color: #ef8466;
                font-size: 14px;
                border: none;
                border-left: 1px solid #bababa;
                padding-left: 10px;
                background-color: #fff;
                cursor: pointer;
            }
        }
    }
}
</style>