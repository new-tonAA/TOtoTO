//导入request.js请求工具
import request from '@/utils/request.js'


//搜索图片
export const SearchImage = (image) =>{
    if (!image || !(image instanceof File)) {
        return Promise.reject(new Error('请提供有效的图片文件'));
    }
    const params = new FormData();  //form格式
    params.append('image', image);
    return request.post('/image/search',params);
}

//展示之前历史记录
export const ShowRecord = ()=>{
    return request.get('/image/record')
}

//获取其中历史记录的详细内容
export const GetRecord = (hid)=>{
     return request.get(`/image/record/${hid}`)
}