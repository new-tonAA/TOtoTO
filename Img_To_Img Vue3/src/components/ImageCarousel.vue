<template>
  <div
    class="carousel-container"
    @wheel.prevent="handleWheel"
    role="region"
    aria-label="Image Carousel"
  >
    <div class="carousel-inner">
      <div
        v-for="(item, i) in visibleItems"
        :key="item.filename"
        class="carousel-item"
        :style="getItemStyle(i)"
      >
        <img :src="getImageUrl(item.filename)" :alt="item.name" />
      </div>

      <!-- caption-container放这，和图片同级 -->
      <div class="caption-container" aria-live="polite">
        <transition name="fade" mode="out-in">
          <div class="caption-text" :key="list[idx]?.filename">{{
            list[idx]?.name || ""
          }}</div>
        </transition>
      </div>

      <!-- 弹幕容器，注意 z-index < 图片，图片会遮挡弹幕 -->
      <div
        class="danmaku-container"
        aria-live="off"
        aria-label="弹幕评论"
      >
        <div
          v-for="(danmaku, index) in activeDanmakus"
          :key="danmaku.id + '-' + danmaku.runId"
          class="danmaku-item"
          :style="{
            top: (danmaku.track * trackHeight - 150 ) + 'px',
            left: danmaku.left + 'px',
            color: danmaku.color,
            textShadow: danmaku.color === '#fff' ? '0 0 5px black' : 'none'
          }"
        >
          {{ danmaku.comment }}
        </div>
      </div>
    </div>

    <div class="dots" role="tablist" aria-label="Carousel Pagination">
      <button
        v-for="(item, i) in list"
        :key="item.filename"
        :class="{ active: i === idx }"
        class="dot"
        @click="goTo(i)"
        role="tab"
        :aria-selected="i === idx"
        :aria-label="`Go to slide ${i + 1}`"
      ></button>
    </div>

    <!-- 评论输入框-->
    <div class="review-box">
      <input
        v-model="comment"
        class="review-input"
        type="text"
        placeholder=""
        @keydown.enter.prevent="submitComment"
      />
      <button
        class="review-button"
        :disabled="!comment.trim() || comment.trim().length > 45"
        @click="submitComment"
        aria-label="发送评论"
      >
        <!-- 发送箭头SVG -->
        <svg
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="white"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <line x1="22" y1="2" x2="11" y2="13"></line>
          <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ref, computed, onMounted, onBeforeUnmount } from "vue";

export default {
  name: "ImageCarousel",
  setup() {
    const list = ref([]);
    const idx = ref(0);
    const comment = ref("");
    const comments = ref([]);

    const trackCount = 10;
    const trackHeight = 30;
    const danmakuWidth = 910; // 弹幕显示区域宽度
    const danmakuSpeed = 0.12; // px/ms，调速用

    const activeDanmakus = ref([]);
    let runIdCounter = 0;
    const tracksEndTime = new Array(trackCount).fill(0);
    let animationFrameId = null;

    const fetchList = async () => {
      try {
        const res = await axios.get("/api/ShowImages/list");
        list.value = res.data;
      } catch (e) {
        console.error("获取图片列表失败", e);
      }
    };

    const fetchComments = async () => {
      try {
        const res = await axios.get("/review/list");
        comments.value = res.data;
      } catch (e) {
        console.error("获取评论失败", e);
      }
    };

    const submitComment = async () => {
      const trimmed = comment.value.trim();
      if (!trimmed) return alert("评论不能为空");
      if (trimmed.length > 45) return alert("评论不能超过45字");

      try {
        await axios.post("/review", { comment: trimmed });
        comment.value = "";
        await fetchComments();
        startDanmaku(); // 重新启动弹幕，刷新评论
      } catch (err) {
        alert("发送评论失败：" + (err.response?.data?.error || err.message));
      }
    };

    const prev = () => {
      idx.value = (idx.value - 1 + list.value.length) % list.value.length;
    };

    const next = () => {
      idx.value = (idx.value + 1) % list.value.length;
    };

    const goTo = (i) => {
      idx.value = i;
    };

    const handleWheel = (e) => {
      e.deltaY > 0 ? next() : prev();
    };

    const visibleItems = computed(() => {
      if (list.value.length === 0) return [];
      const total = list.value.length;
      return [
        list.value[(idx.value - 1 + total) % total],
        list.value[idx.value],
        list.value[(idx.value + 1) % total],
      ];
    });

    const getImageUrl = (filename) => `/api/ShowImages/${filename}`;

    const getItemStyle = (i) => {
      const base = {
        transition: "all 0.9s ease-in-out",
        position: "absolute",
        top: "50%",
        transformStyle: "preserve-3d",
        opacity: 0,
        zIndex: 0,
        filter: "brightness(0.85)",
      };

      if (i === 1) {
        return {
          ...base,
          left: "50%",
          transform: "translate(-50%, -50%) translateZ(0) scale(1)",
          width: "504px",
          height: "336px",
          opacity: 1,
          zIndex: 10,
          filter: "none",
          boxShadow: "0 14px 35px rgba(0, 0, 0, 0.3)",
          borderRadius: "17px",
        };
      } else if (i === 0) {
        return {
          ...base,
          left: "0%",
          transform: "translateY(-50%) translateZ(-200px) rotateY(15deg) scale(0.85)",
          width: "224px",
          height: "168px",
          opacity: 0.6,
          zIndex: 5,
        };
      } else if (i === 2) {
        return {
          ...base,
          right: "0%",
          transform: "translateY(-50%) translateZ(-200px) rotateY(-15deg) scale(0.85)",
          width: "224px",
          height: "168px",
          opacity: 0.6,
          zIndex: 5,
        };
      }

      return base;
    };

    // 弹幕动画函数，使用 requestAnimationFrame 实现
    const colors = [
  { color: '#fff', shadow: '0 0 5px black' },  // 白色，带阴影
  { color: '#888', shadow: 'none' },          // 灰色，无阴影
  { color: '#222', shadow: 'none' },          // 黑色，无阴影
];

const startDanmaku = () => {
  if (animationFrameId) cancelAnimationFrame(animationFrameId);

  activeDanmakus.value = [];
  runIdCounter = 0;

  const tracks = Array.from({ length: trackCount }, () => []);

  const queue = [...comments.value];
  if (queue.length === 0) return;

  let index = 0;
  let lastTime = performance.now();

  const safetyGap = 20; // 额外安全距离，防止重叠

  const animate = (now) => {
    if (!now) now = performance.now();
    const delta = now - lastTime;
    lastTime = now;

    if (!animate.lastAddTime) animate.lastAddTime = now;
    if (now - animate.lastAddTime > 400) {
      animate.lastAddTime = now;

      const commentItem = queue[index % queue.length];
      const estimatedWidth = commentItem.comment.length * 14;

      let track = -1;

      trackLoop:
      for (let i = 0; i < trackCount; i++) {
        const trackDanmakus = tracks[i];

        for (const dm of trackDanmakus) {
          const dmRight = dm.left + dm.estimatedWidth + safetyGap;
          if (dmRight > danmakuWidth) {
            continue trackLoop;
          }
        }

        track = i;
        break;
      }

      if (track !== -1) {
        index++;

        const duration = (danmakuWidth + estimatedWidth) / danmakuSpeed;

        // 随机颜色
        const colorIndex = Math.floor(Math.random() * colors.length);
        const { color, shadow } = colors[colorIndex];

        const newDanmaku = {
          ...commentItem,
          track,
          left: danmakuWidth,
          runId: runIdCounter++,
          estimatedWidth,
          duration,
          color,
          shadow,
        };

        activeDanmakus.value.push(newDanmaku);
        tracks[track].push(newDanmaku);
      }
    }

    // 更新位置，移除弹幕
    for (let i = activeDanmakus.value.length - 1; i >= 0; i--) {
      const d = activeDanmakus.value[i];
      d.left -= danmakuSpeed * delta;

      if (d.left + d.estimatedWidth < 0) {
        activeDanmakus.value.splice(i, 1);

        const trackArr = tracks[d.track];
        const idxInTrack = trackArr.findIndex(dm => dm.runId === d.runId);
        if (idxInTrack !== -1) {
          trackArr.splice(idxInTrack, 1);
        }
      }
    }

    animationFrameId = requestAnimationFrame(animate);
  };

  animationFrameId = requestAnimationFrame(animate);
};



    onMounted(async () => {
      await fetchList();
      await fetchComments();
      startDanmaku();
    });

    onBeforeUnmount(() => {
      if (animationFrameId) cancelAnimationFrame(animationFrameId);
    });

    return {
      list,
      idx,
      visibleItems,
      getImageUrl,
      handleWheel,
      goTo,
      getItemStyle,
      comment,
      submitComment,
      activeDanmakus,
      trackHeight,
    };
  },
};
</script>

<style scoped>
.carousel-container {
  max-width: 910px;
  margin: 0 auto;
  padding: 28px 14px;
  background: linear-gradient(135deg, #fafafa 0%, #e8f0f8 100%);
  border-radius: 13px;
  box-shadow: 0 7px 24px rgba(0, 0, 0, 0.1);
  user-select: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: visible;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  position: relative;
}

.carousel-inner {
  position: relative;
  width: 100%;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  perspective: 1500px;
  overflow: visible;
  margin-bottom: 16.8px;
}

.carousel-item {
  border-radius: 14px;
  box-shadow: 0 8.4px 24.5px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  background: white;
  cursor: grab;
  user-select: none;
  position: absolute;
}

.carousel-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  pointer-events: none;
  user-select: none;
}

.caption-container {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 504px;
  height: 336px;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 4rem;
  font-weight: 900;
  user-select: none;
  display: flex;
  justify-content: center;
  align-items: center;
  text-transform: capitalize;
  pointer-events: none;
  transition: none !important;
  animation: none !important;
  z-index: 20;
  text-align: center;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.dots {
  display: flex;
  gap: 12px;
  justify-content: center;
  margin-top: 14px;
}

.dot {
  width: 10px;
  height: 10px;
  display: block;
  border-radius: 50%;
  background: #ccc;
  border: 1.5px solid transparent;
  cursor: pointer;
  transition: background-color 0.3s, border-color 0.3s;
  padding: 0;
  line-height: 0;
  font-size: 0;
}

.dot:hover {
  border-color: #555;
}

.dot.active {
  background: #222;
  border-color: #222;
}

.review-box {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 16px;
  width: 100%;
  max-width: 700px;
}

.review-input {
  flex: 1;
  padding: 12px 20px;
  border-radius: 9999px;
  border: none;
  box-shadow: 0 1px 6px rgba(32, 33, 36, 0.28);
  font-size: 1.1rem;
  outline: none;
  transition: box-shadow 0.2s ease;
}

.review-input::placeholder {
  color: #888;
}

.review-input:focus {
  box-shadow: 0 2px 8px rgba(32, 33, 36, 0.45);
}

.review-button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background-color: #222;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.review-button:disabled {
  background-color: #555;
  cursor: not-allowed;
}

.review-button:hover:enabled {
  background-color: #000;
}

.review-button svg {
  stroke: white;
  width: 20px;
  height: 20px;
  pointer-events: none;
  user-select: none;
}

/* 弹幕容器，位于图片后面，z-index低于图片 */
.danmaku-container {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 910px;
  height: 150px;
  pointer-events: none;
  overflow: visible;
  z-index: 8; /* 小于图片的z-index(10) */
}

/* 弹幕弹出条目 */
.danmaku-item {
  position: absolute;
  white-space: nowrap;
  font-size: 16px;
  font-weight: 600;
  user-select: none;
  will-change: transform;
  pointer-events: none;
  /* 这里的left和top由JS动态控制 */
}
</style>

