//导入request.js请求工具
import request from '@/utils/request.js'

//提供调用注册接口的函数
export const userRegisterService = (registerData)=>{
    //借助于UrlSearchParams完成传递
    const params = new URLSearchParams()
    for(let key in registerData){
        params.append(key,registerData[key]);
    }
    return request.post('/user/register',params);
}

//提供调入登录接口的函数
export const userLoginService = (loginData)=>{
    return request.get('/user/login',{
        params:loginData,
    })
}

//绑定邮箱时发送验证码
export const userRegisterEmail = (registerEmailData)=>{
    return request.get('/user/register/email',{
        params:registerEmailData,
    })
}

//绑定邮箱时收到验证码进行验证
export const userRegisterVerify = (registerVerifyData)=>{
    const params = new URLSearchParams()
    for(let key in registerVerifyData){
        params.append(key,registerVerifyData[key]);
    }
    return request.patch('/user/register/verify',params);
}


//邮箱登录收到验证码进行验证
export const userEmailVerify = (emailVerifyData)=>{
    return request.get('/user/verify', {
        params: emailVerifyData,  // axios 会自动转成 URL 查询参数
    });
}

//向邮箱发送验证码
export const userEmail=(emailData)=>{
    return request.get('/user/login/email', {
        params: emailData,  // axios 会自动转成 URL 查询参数
    });
}

//获取用户信息
export const getUserInfo=()=>{
    return request.get('/user/userInfo')
}