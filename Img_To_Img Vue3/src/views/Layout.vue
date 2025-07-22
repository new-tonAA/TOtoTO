<script setup>
    import { useRouter } from 'vue-router'
    import useUserInfoStore from '@/stores/userInfo.js'
    import { ElMessage, ElLoading } from 'element-plus'
    import { ref, watch, computed, onMounted } from 'vue'
    import ImageCarousel from '@/components/ImageCarousel.vue'//图片轮播组件
    const router = useRouter()

    import { useTokenStore } from '@/stores/token.js'
    const tokenStore = useTokenStore();
    const userInfoStore = useUserInfoStore();

    import ChatGuide from '@/components/ChatGuide.vue'//AI解说
    const placeDescription = ref('')  // AI地标描述
    const placeTitle = ref('')


    // 用户上传图片
    const uploadedImage = ref(null)
    // URL 图片文件
    const imageUrl = ref('')
    const fileName = ref('未选择图片')  // 图片名
    // 历史记录
    const historyTimes = ref([])
    const isHistory = ref(false)  // 用户是否在查看历史记录
    const isAsideCollapsed = ref(false)  // 控制侧边栏收起或展开
    // 搜索结果 + 搜索结果图片的数量
    const result_images = ref([])
    const preview_images = ref([])
    // 只要有搜索／历史结果就显示地图 
    const showMap = computed(() => result_images.value.length > 0) 
    // 动态地图 URL（默认是 /map/），这样每次用户操作，都会重新设置地图
    const mapUrl = ref('http://127.0.0.1:8010/map/')


    const resultNumber = computed(() => result_images.value.length)
    const button = ref(null)  // button 指定的按钮(button===recordId)会变深色
    // 判断是否有登录账号(用户一进入界面，系统就调用)
    const hasAccount = ref(false)
    // 初始化用户名（响应式）
    const username = ref(userInfoStore.info?.username || 'User');

    // 定位地址
    const userAddress = ref('定位中…')
    // 定位错误状态
    const locError = ref(false)

    // 获取用户信息(用户一进入界面就系统就调用该函数)
    import { getUserInfo } from '@/api/user.js'
    const get_userInfo = async () => {
        let result = await getUserInfo();
        if (result.message !== '未登录') {
            const userInfo = ref({
                username: result.username,
                email: result.email,
                role: result.role,
                phone: result.phone,
            })
            userInfoStore.setInfo(userInfo.value);
        }
    }

    // 页面加载时自动定位并请求后端地址
    onMounted(() => {
        if (!navigator.geolocation) {
            userAddress.value = '浏览器不支持定位'
            return
        }
        navigator.geolocation.getCurrentPosition(
            async ({ coords }) => {
                try {
                    const res = await fetch('http://127.0.0.1:8010/location/get', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            latitude: coords.latitude,
                            longitude: coords.longitude
                        })
                    })
                    const data = await res.json()
                    userAddress.value = data.address
                } catch {
                    userAddress.value = '获取地址失败'
                }
            },
            () => {
                userAddress.value = '定位被拒绝'
            }
        )
    })

    // 重新定位（如果自动定位失败）
    function retryLocate() {
        locError.value = false
        userAddress.value = '重新定位中…'
        onMounted()
    }

    const clear = async () => {
        if (tokenStore.token !== '') {
            hasAccount.value = true
        }
        else {
            tokenStore.removeToken();
            userInfoStore.removeInfo();
            username.value = 'User'
            hasAccount.value = false
            clearData()
        }
    }

    // 获取用户名, 数据发生改变时触发
    watch(() => userInfoStore.info, (newInfo) => {
        username.value = newInfo?.username || 'User';
    }, { immediate: true });

    import { SearchImage, ShowRecord, GetRecord } from '@/api/image.js'

    // 搜索图片
    const searchImage = async () => {
        result_images.value = []
        preview_images.value = []

        StartLoading()

        let result = await SearchImage(imageUrl.value);
        //ElMessage.success(result.message ? result.message : '图片搜索成功')

        if (result.map_url) {
            mapUrl.value = `http://127.0.0.1:8010${result.map_url}`
        }

        for (let key in result.responses) {
            result_images.value.push({
                image: result.responses[key].image,
                distance: result.responses[key].distance,
            })
            preview_images.value.push(result.responses[key].image)
        }
        if (result.create_time && hasAccount.value) {
            let temp = result.create_time.replace("T", " ")
            historyTimes.value.unshift({
                recordId: result.recordId,
                createTime: temp,
                isActive: false,
            })
        }
        //ai描述
        if (result.place_description) {
            placeDescription.value = result.place_description
        } else {
            placeDescription.value = ''
        }

        EndLoading()
    }

    // 从后端获取历史记录
    const showRecord = async () => {
        historyTimes.value = []

        if (tokenStore.token !== '') {
            let result = await ShowRecord();
            //ElMessage.success(result.message ? result.message : '获取历史记录信息成功')
            for (let key in result.all_createtime) {
                let temp = result.all_createtime[key].createtime.replace("T", " ")
                historyTimes.value.unshift({
                    recordId: result.all_createtime[key].id,
                    createTime: temp,
                    isActive: false,
                })
            }
        } else {
            username.value = 'User'
        }
    }

    // 获取历史记录详细信息
    const getRecord = async (time) => {
        clearData();
        if (time.recordId !== button.value) {
            let result = await GetRecord(time.recordId);
            //ElMessage.success(result.message ? result.message : "获取记录信息成功")

            if (result.map_url) {//加载地图用
                mapUrl.value = `http://127.0.0.1:8010${result.map_url}`
            }

            imageUrl.value = result.record
            for (let key in result.responses) {
                result_images.value.push({
                    image: result.responses[key].image,
                    distance: result.responses[key].distance
                })
                preview_images.value.push(result.responses[key].image)
            }
        }

        time.isActive = !time.isActive;

        if (button.value !== null && time.recordId !== button.value) {
            const temp = historyTimes.value.find(historyTime => historyTime.recordId === button.value)
            temp.isActive = false;
            button.value = time.recordId;
            isHistory.value = true;
        }
        else if (button.value !== null && time.recordId === button.value) {
            button.value = null;
            isHistory.value = false;
        }
        else if (button.value === null) {
            button.value = time.recordId
            isHistory.value = true
        }
    }

    // 处理图片
    const handleImageChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            fileName.value = file.name;
            const reader = new FileReader();
            reader.onload = (e) => {
                imageUrl.value = file
                uploadedImage.value = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    }

    // 清理数据
    const clearData = async () => {
        uploadedImage.value = null
        imageUrl.value = ''
        fileName.value = '未选择图片'
        result_images.value = []
        preview_images.value = []
        isHistory.value = false
        mapUrl.value = 'http://127.0.0.1:8010/map/'//变成默认地图

    }

    // 退出登录
    const logout = async () => {
        tokenStore.removeToken();
        userInfoStore.removeInfo();
        historyTimes.value = []
        clearData()
        hasAccount.value = false
    }

    // 去登录
    const login = async () => {
        tokenStore.removeToken();
        userInfoStore.removeInfo();
        clearData()
        router.push('/login')
    }

    // 加载动画
    const StartLoading = async () => {
        ElLoading.service({
            lock: true,
            text: 'Loading',
            background: 'rgba(0, 0, 0, 0.7)',
        })
    }

    // 结束加载
    const EndLoading = async () => {
        ElLoading.service().close()
    }

    const Autofunction = async () => {
        username.value = 'User'
        hasAccount.value = false
        get_userInfo();
        clear()
        showRecord();
    }
    Autofunction()



</script>

<template>
    <div class="common-layout">
        <el-container class="app-container">

            <!-- Header -->
            <el-header class="header">
                <div class="logo">图to图</div>
                <div class="user-info">
                    <span class="username">{{ username }}</span>
                    <span class="address">{{ userAddress }}</span>
                    <el-button v-if="locError" size="mini" type="primary" @click="retryLocate">
                        重新定位
                    </el-button>
                    <el-button v-if="hasAccount" class="btn btn-danger" @click="logout">Logout</el-button>
                    <el-button v-else class="btn btn-primary" @click="login">Login</el-button>
                </div>
            </el-header>

            <el-container style="flex: 1;">
                <!-- 左侧历史记录 可展开关闭-->
                <el-aside :width="isAsideCollapsed ? '48px' : '260px'" :class="['aside', { collapsed: isAsideCollapsed }]">
                    <!-- 折叠按钮 -->
                    <div class="collapse-btn" @click="isAsideCollapsed = !isAsideCollapsed">
                        <span>{{ isAsideCollapsed ? '▶' : '◀' }}</span>
                    </div>

                    <!-- 历史记录内容（加 v-if 控制） -->
                    <template v-if="!isAsideCollapsed">
                        <h2>历史记录</h2>
                        <el-scrollbar class="scrollbar">
                            <div v-for="time in historyTimes"
                                 :key="time.recordId"
                                 class="history-item"
                                 :class="{ active: time.isActive }"
                                 @click="getRecord(time)">
                                {{ time.createTime }}
                            </div>
                        </el-scrollbar>
                    </template>

                </el-aside>

                <!-- 右侧上传 & 搜索 & 结果 -->
                <el-main class="upload-area">
                    <div class="content-wrapper">
                        <div class="left-panel">

                            <div class="card">

                                <!-- 加 v-if 控制搜索控件显示 -->
                                <div class="upload-controls" v-if="!isHistory">
                                    <input type="file"
                                           accept="image/*"
                                           @change="handleImageChange"
                                           class="btn" />
                                    <span class="file-name">{{ fileName }}</span>
                                    <el-button class="btn btn-primary" @click="searchImage">搜索图片</el-button>
                                </div>

                                <!-- 上传图片显示 + AI 讲解 -->
                                <div v-if="(uploadedImage && !isHistory) || (imageUrl && isHistory)" class="results-section">
                                    <h1>您上传的图片</h1>

                                    <!-- 改为：AI文本仅非历史时显示，横向排列 -->
                                    <div class="image-guide-container">
                                        <!-- 用户图片 -->
                                        <div class="result-card">
                                            <el-image :src="isHistory ? imageUrl : uploadedImage"
                                                      class="result-img clickable"
                                                      fit="cover"
                                                      @click="() => window.open(isHistory ? imageUrl : uploadedImage, '_blank')" />
                                            <el-tag type="success">用户图片</el-tag>
                                        </div>

                                        <!-- 右边：AI 讲解，只有非历史时显示 -->
                                        <div class="guide-panel" v-if="!isHistory">
                                            <ChatGuide :placeDescription="placeDescription" :placeTitle="placeTitle" />
                                        </div>

                                    </div>
                                </div>


                                <el-divider />

                                <!-- 搜索结果显示 -->
                                <div v-if="result_images.length" class="results-section">
                                    <h1>搜索结果（{{ resultNumber }} 张）</h1>
                                    <div class="image-container">
                                        <div v-for="(res, idx) in result_images" :key="idx" class="result-card">
                                            <el-image :src="res.image"
                                                      class="result-img clickable"
                                                      fit="cover"
                                                      @click="() => window.open(res.image, '_blank')" />
                                            <el-tag type="info">相似度: {{ (1 - res.distance).toFixed(4) }}</el-tag>
                                        </div>
                                    </div>
                                </div>

                                <!-- ✅ 只有在未上传、未点击历史、也没搜索结果时显示轮播图 -->
                                <ImageCarousel v-if="!uploadedImage && !imageUrl && !result_images.length && !isHistory" />


                            </div>
                        </div>
                        <div class="map-panel" v-if="showMap">
                            <iframe :src="mapUrl"
                                    frameborder="0"
                                    loading="lazy"
                                    width="100%"
                                    height="100%"
                            ></iframe>
                        </div>
                    </div> 

                </el-main>
            </el-container>
        </el-container>
    </div>
</template>



<style scoped>

    /* 右侧区域让 flex 自动分配，宽度变化同样平滑 */
    .content-wrapper {
        display: flex;
        flex: 1;
        height: 100%;
        gap: 24px;
        /* 让左右子项宽度变化有动画 */
        transition: gap 0.3s ease;
    }

    .left-panel {
        flex: 5 1 0;
        min-width: 0; /* 防止卡片宽度挤爆 */
    }

    /* 右栏（地图） */
    .map-panel {
        flex: 2 1 0;
        min-width: 400px; /* 想更窄可改 */
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
    }

    .map-panel iframe {
        width: 100%;
        height: 100%;
    }

    .app-container {
        display: flex;
        flex-direction: column;
        height: 100vh;
        background: linear-gradient(135deg, #eef2f7 0%, #ffffff 100%);
    }

    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #ffffff;
        padding: 0 24px;
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.06);
    }

    .logo {
        font-size: 20px;
        font-weight: 700;
        color: #334155;
    }

    .user-info {
        display: flex;
        align-items: center;
    }

    .username {
        margin-right: 16px;
        color: #475569;
    }

    /* 地址样式 */
    .address {
        margin-right: 8px;
        color: #64748b;
        font-size: 14px;
    }
    /* 重新定位按钮微调 */
    .user-info .el-button--mini {
        margin-right: 16px;
    }

    .aside {
        background: #ffffff;
        padding: 20px;
        box-shadow: 2px 0 12px rgba(0, 0, 0, 0.04);
        transition: /* ⬅️ 关键 */
        width 0.3s ease, padding 0.3s ease; /* 折叠时 padding 也会变 */
    }

        .aside h2 {
            margin-bottom: 12px;
            font-size: 18px;
            color: #334155;
        }

    .scrollbar {
        max-height: calc(100vh - 160px);
    }

    .history-item {
        padding: 8px 10px;
        margin-bottom: 6px;
        border-radius: 6px;
        cursor: pointer;
        transition: background 0.2s, transform 0.2s;
        color: #475569;
        font-size: 14px;
    }

        .history-item:hover {
            background: #f0f9ff;
            transform: translateX(2px);
        }

        .history-item.active {
            background: #bae7ff;
            font-weight: 600;
        }

    .upload-area {
        flex: 1;
        padding: 24px;
        overflow-y: auto;
        height: 100%;
        display: flex;
    }

    .card {
        background: #ffffff;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        transition: box-shadow 0.3s ease;
    }

        .card:hover {
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.06);
        }

    .upload-controls {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 16px;
    }

    .file-name {
        color: #64748b;
        font-size: 14px;
    }

    .btn {
        padding: 6px 16px;
        border-radius: 6px;
        font-weight: 500;
        cursor: pointer;
        transition: background 0.2s, transform 0.2s;
        font-size: 14px;
    }

    .btn-primary {
        background: #3b82f6;
        color: #fff;
        border: none;
    }

    .btn-danger {
        background: #ef4444;
        color: #fff;
        border: none;
    }

    .btn-outline {
        background: transparent;
        color: #3b82f6;
        border: 2px solid #3b82f6;
    }

    .btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
    }

    .image-preview {
        text-align: center;
        margin-bottom: 16px;
    }

    .preview-img {
        max-width: 100%;
        border-radius: 8px;
    }

        .preview-img:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        }

    .results-section h1 {
        margin-top: 20px;
        font-size: 20px;
        color: #334155;
    }

    .image-container {
        display: flex;
        flex-wrap: wrap;
        gap: 14px;
        margin-top: 16px;
        justify-content: flex-start;
    }

    .result-card {
        background: #fafafa;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        transition: transform 0.3s, box-shadow 0.3s;
        width: 150px;
    }

        .result-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.08);
        }

    .result-img {
        width: 140px;
        height: 140px;
        border-radius: 8px;
        object-fit: cover; /* 保持裁剪显示 */
        transition: transform 0.3s, box-shadow 0.3s;
    }
        .result-img:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12);
        }

    .clickable {
        cursor: pointer;
    }

    .el-divider__text {
        color: #94a3b8;
        font-size: 13px;
    }

    /* 折叠按钮样式 */
    .collapse-btn {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 30px;
        cursor: pointer;
        border-radius: 6px;
        background: #f3f4f6;
        margin-bottom: 10px;
        font-size: 14px;
        color: #334155;
        transition: background 0.2s; /* 悬停变色 */
    }

        .collapse-btn:hover {
            background-color: #e2e8f0;
        }

    /* 当折叠时 */
    .aside.collapsed {
        padding: 10px 6px;
    }

    .image-guide-container {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        gap: 20px;
        margin-top: 16px;
    }

    .guide-panel {
        flex-shrink: 0;
    }


</style>

