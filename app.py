import streamlit as st
import time

# --- 1. 页面基础设置 ---
st.set_page_config(
    page_title="For You",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS 样式与动画逻辑 ---
# 这里包含了信封、纸飞机、飞行动画以及隐藏蒙版的代码
animation_code = """
<style>
    /* 全局背景色 */
    .stApp {
        background-color: #FDFCF5;
    }
    
    /* 1. 覆盖全屏的蒙版 (Loading Screen) */
    #loading-mask {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: #FDFCF5; /* 和背景色一致，制造无缝感 */
        z-index: 99999; /* 保证在最上层 */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        transition: opacity 1s ease-out; /* 消失时的淡出效果 */
    }

    /* 2. 信封/纸飞机容器 */
    #emoji-container {
        font-size: 80px; /* 图标大小 */
        cursor: pointer;
        transition: all 0.5s ease;
        user-select: none;
    }
    
    /* 提示文字 */
    #click-hint {
        margin-top: 20px;
        font-family: "Helvetica Neue", sans-serif;
        color: #888;
        font-size: 14px;
        opacity: 0.8;
        animation: pulse 2s infinite; /* 轻微呼吸效果 */
    }

    /* 3. 动画定义 */
    
    /* 呼吸灯动画 */
    @keyframes pulse {
        0% { opacity: 0.5; }
        50% { opacity: 1; }
        100% { opacity: 0.5; }
    }

    /* 纸飞机飞走动画 */
    @keyframes flyAway {
        0% {
            transform: translate(0, 0) rotate(0deg) scale(1);
        }
        20% {
            transform: translate(-10px, 10px) rotate(-10deg) scale(0.9); /* 先后退蓄力 */
        }
        100% {
            transform: translate(100vw, -100vh) rotate(45deg) scale(0.5); /* 向右上方飞走 */
            opacity: 0;
        }
    }

    /* 添加这个类名就会触发飞行 */
    .flying {
        animation: flyAway 1.5s ease-in forwards;
    }
    
    /* 内容淡入效果 */
    .content-hidden {
        opacity: 0;
        transition: opacity 2s ease-in;
    }
    .content-visible {
        opacity: 1;
    }

</style>

<div id="loading-mask" onclick="startAnimation()">
    <div id="emoji-container">💌</div>
    <div id="click-hint">点我打开</div>
</div>

<script>
    function startAnimation() {
        var container = document.getElementById('emoji-container');
        var mask = document.getElementById('loading-mask');
        var hint = document.getElementById('click-hint');
        
        // 1. 瞬间变身：信封 -> 纸飞机
        container.innerText = "✈️"; 
        hint.style.display = 'none'; // 隐藏提示字
        
        // 2. 添加飞行 class，开始动画
        container.classList.add('flying');
        
        // 3. 1.2秒后，淡出蒙版
        setTimeout(function() {
            mask.style.opacity = '0';
            // 穿透蒙版，让用户可以点击下面的按钮 (虽然后面会display:none，但这样保险)
            mask.style.pointerEvents = 'none'; 
        }, 1200);
        
        // 4. 2秒后，彻底移除蒙版层
        setTimeout(function() {
            mask.style.display = 'none';
        }, 2000);
    }
</script>
"""

# 注入 HTML/JS 代码
st.components.v1.html(animation_code, height=0)


# --- 3. 下面是正式的内容 (原本的代码) ---

# 自定义 CSS 优化按钮和文字
st.markdown("""
    <style>
    .custom-text {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 18px;
        color: #5D5D5D;
        line-height: 1.8;
        margin-bottom: 50px;
        animation: fadeIn 3s ease; /* 让文字有个缓慢浮现的效果 */
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    div.stButton > button {
        background-color: #E6Aac4; 
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 24px;
        font-size: 16px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# 顶部留白
st.write("") 
st.write("") 

# === 你的情书内容 ===
content = """
亲爱的：

当你看到这个信封时，
我其实有点紧张。

有些话当面说会脸红，
所以让这个小小的程序替我传达。

遇见你是我最大的幸运，
生活因为有你而变得温柔。

往下翻，
还有一个小东西给你。
"""
# ===================

st.markdown(f'<div class="custom-text">{content.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

# 占位符，把按钮挤下去
for _ in range(5):
    st.text("")

col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    if st.button("✨ 点开，有一份小惊喜"):
        st.balloons() 
        
        # === 礼物信息 ===
        st.success("🎁 礼物已发出！")
        
        # 这里为了防止文字挤在一起，加了换行符
        st.info("""
        **📍 见面地点**: 幸福路 520 号 \n\n
        **🔐 专属暗号**: 小猪快跑 \n
        """)
