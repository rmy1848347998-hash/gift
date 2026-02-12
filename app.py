import streamlit as st

# --- 1. 页面配置 ---
st.set_page_config(
    page_title="For You",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 检查是否是第一次打开 (防止点按钮时信封又弹出来) ---
if 'first_visit' not in st.session_state:
    st.session_state['first_visit'] = True
else:
    st.session_state['first_visit'] = False

# --- 3. 动画代码 (核心修改部分) ---
# 只有第一次访问时，才注入这段动画 HTML/CSS
if st.session_state['first_visit']:
    st.markdown("""
        <style>
            /* 1. 覆盖全屏的蒙版 */
            #loading-mask {
                position: fixed; /* 固定定位，无视文档流 */
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background-color: #FDFCF5;
                z-index: 999999; /* 层级最高，盖住一切 */
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: opacity 1s ease-out;
            }

            /* 2. 信封图标 */
            #emoji-container {
                font-size: 80px;
                cursor: pointer;
                user-select: none;
                transition: transform 0.5s ease;
            }

            /* 3. 提示文字 */
            #click-hint {
                margin-top: 20px;
                font-family: sans-serif;
                color: #888;
                font-size: 14px;
                animation: pulse 1.5s infinite;
            }

            /* 呼吸动画 */
            @keyframes pulse {
                0% { opacity: 0.6; }
                50% { opacity: 1; }
                100% { opacity: 0.6; }
            }

            /* 飞行动画 */
            @keyframes flyAway {
                0% { transform: scale(1) rotate(0deg); }
                20% { transform: scale(0.9) rotate(-10deg) translate(-10px, 10px); }
                100% { 
                    transform: scale(0.4) rotate(45deg) translate(100vw, -100vh); 
                    opacity: 0;
                }
            }

            .flying {
                animation: flyAway 1.2s ease-in forwards;
            }
        </style>

        <div id="loading-mask" onclick="startAnimation()">
            <div id="emoji-container">💌</div>
            <div id="click-hint">点开信封</div>
        </div>

        <script>
            function startAnimation() {
                var container = document.getElementById('emoji-container');
                var mask = document.getElementById('loading-mask');
                var hint = document.getElementById('click-hint');
                
                // 1. 变身纸飞机
                container.innerHTML = "✈️";
                hint.style.display = 'none';
                
                // 2. 开始飞
                container.classList.add('flying');
                
                // 3. 飞走后淡出蒙版
                setTimeout(function() {
                    mask.style.opacity = '0';
                    mask.style.pointerEvents = 'none'; // 让点击能穿透过去
                }, 1000);
                
                // 4. 彻底移除 (防止挡路)
                setTimeout(function() {
                    mask.style.display = 'none';
                }, 2000);
            }
        </script>
    """, unsafe_allow_html=True)

# --- 4. 正文内容 CSS (美化) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #FDFCF5;
    }
    .custom-text {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 18px;
        color: #5D5D5D;
        line-height: 1.8;
        margin-bottom: 50px;
        margin-top: 20px;
    }
    /* 按钮样式 */
    div.stButton > button {
        background-color: #E6Aac4; 
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 24px;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        background-color: #D48FA8;
        color: white;
    }
    /* 隐藏掉不需要的元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 5. 页面布局 ---

st.write("") # 顶部占位

# === 文字内容 (请在这里修改) ===
content = """
亲爱的：

当你看到这个信封时，
其实我有点紧张。

有些话当面说会脸红，
所以让这个小程序替我传达。

遇见你是我最大的幸运，
生活因为有你而变得温柔。

往下翻，
有一个小东西给你。
"""
# ============================

st.markdown(f'<div class="custom-text">{content.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

# 占位空行
for _ in range(6):
    st.text("")

# 按钮布局
col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    if st.button("✨ 点开，有一份小惊喜"):
        st.balloons() 
        
        st.success("🎁 礼物已发出！")
        
        # === 礼物信息 (请在这里修改) ===
        st.info("""
        **📍 见面地点**: 幸福路 520 号 \n\n
        **🔐 专属暗号**: 小猪快跑 \n
        """)
