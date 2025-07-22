<!-- src/components/ChatGuide.vue -->
<template>
    <div v-if="placeDescription" class="chat-guide-container">
        <el-card class="chat-guide-card" shadow="hover">
            <h3>AI 地标讲解 · {{ placeTitle }}</h3>
            <div class="chat-guide-content">
                <p>{{ placeDescription }}</p>
            </div>
        </el-card>
    </div>
</template>

<script setup>
    defineProps({
        placeDescription: {
            type: String,
            required: false,
            default: ''
        },
        placeTitle: {
            type: String,
            required: false,
            default: ''
        }
    })
</script>

<style scoped>
    .chat-guide-container {
        width: 320px;
        max-height: 260px;
        margin-left: 20px;
        display: flex;
        flex-direction: column;
        background: #f9fafb;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .chat-guide-card {
        flex: 1;
        padding: 16px;
        display: flex;
        flex-direction: column;
    }

        .chat-guide-card h3 {
            margin: 0 0 10px 0;
            font-weight: 700;
            font-size: 16px;
            color: #2c3e50;
            border-bottom: 1px solid #e1e4e8;
            padding-bottom: 6px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

    .chat-guide-content {
        flex: 1;
        max-height: 80px; /* 加这一行确保滚动区域有限高 */
        overflow-y: scroll;
        padding-right: 8px;
        white-space: pre-wrap;
        font-size: 14px;
        line-height: 1.6;
        color: #34495e;
        user-select: text;
    }


        /* 滚动条样式（Chrome / Edge / Safari 有效） */
        .chat-guide-content::-webkit-scrollbar {
            width: 6px;
        }

        .chat-guide-content::-webkit-scrollbar-thumb {
            background-color: rgba(100, 100, 100, 0.3);
            border-radius: 3px;
        }

        .chat-guide-content::-webkit-scrollbar-track {
            background-color: transparent;
        }
</style>
