import streamlit as st

# --- 1. 页面基础设置 ---
st.set_page_config(
    page_title="For You",
    page_icon="💌",
    layout="centered"
)

# --- 2. 自定义 CSS (极简温柔风) ---
st.markdown("""
    <style>
    /* 全局背景色 */
    .stApp {
        background-color: #FDFCF5;
    }
    
    /* 文字样式 */
    .custom-text {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 18px;
        color: #5D5D5D;
        line-height: 1.8;
        margin-bottom: 50px;
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
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #D48FA8;
        border: none;
        color: white;
    }
    
    /* 隐藏菜单 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. 页面内容区域 ---

st.write("") 
st.write("") 

# === 核心文字区 (这里是上面的长文字) ===
content = """
这里是第一段文字。
你可以写一些平时不好意思开口的话，
或者记录一个特别的日子。

不需要华丽的排版，
简简单单的文字就很好。

这也是我想对你表达的心意。
往下翻，有一个小东西给你。
"""
# ==========================================

st.markdown(f'<div class="custom-text">{content.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

for _ in range(8):
    st.text("")

# --- 4. 按钮与惊喜 ---

col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    # === 按钮部分 (注意：下面的代码必须保持这种阶梯状的缩进) ===
    if st.button("✨ 点开，有一份小惊喜"):
        # 1. 撒花特效
        st.balloons() 
        
        # 2. 弹出文字
        st.success("🎁 礼物已发出！")
        
        # 3. 详细信息
        st.info("""
        **📍 见面地点**: 幸福路 520 号 \n\n
        **🔐 专属暗号**: 小猪快跑 \n
        """)
