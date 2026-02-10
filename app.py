import streamlit as st

# --- 1. 页面基础设置 ---
st.set_page_config(
    page_title="For You",  # 浏览器标签页标题
    page_icon="💌",        # 浏览器标签页图标
    layout="centered"      # 布局居中，适合手机
)

# --- 2. 自定义 CSS (极简温柔风) ---
# 这里设置了背景色为米白色，隐藏了右上角菜单，调整了按钮样式
st.markdown("""
    <style>
    /* 全局背景色 - 温暖的米色 */
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

    /* 按钮样式 - 柔和的粉色/豆沙色 */
    div.stButton > button {
        background-color: #E6Aac4; 
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 24px;
        font-size: 16px;
        width: 100%; /* 按钮宽度填满容器，适合手机点击 */
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #D48FA8;
        border: none;
        color: white;
    }
    
    /* 隐藏 Streamlit 默认的汉堡菜单和页脚，看起来更像原生网页 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. 页面内容区域 ---

# 标题或顶部留白
st.write("") 
st.write("") 

# === 核心文字区 (请在这里修改你想说的话) ===
content = """
致世界上最好的人：
 
Hi，最近过得好吗，是不是已经慢慢活成你
更喜欢的样子了，我真心为你高兴。
 
分开的这段日子，我成长了很多。谢谢你，
让曾经不够成熟的我，学会认真反思自己。
也谢谢你在这段感情里付出的一切，是你
让我真切感受到爱情的美好，让我知道，
被人坚定喜欢着，是一件多幸福的事。
 
我知道，是我之前做得不够好，
才让你攒够了失望。现在我只希望你不会
再因为过去不开心，能一直轻松、自在地往前走。
 
我也在和过去的自己告别，努力变成一个更靠谱、更值得信任的人。
今天是情人节，我不想给你任何压力，
更不想打乱你的生活，只是想安静告诉你：我一直都在，也一直在慢慢变好。
 
辛苦你看到这里啦，下面有个小按钮，是我为你准备的小小心意。
希望你今天开心，明天开心，永远都开心。
"""
# ==========================================

st.markdown(f'<div class="custom-text">{content.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

# 添加一些空行，让按钮自然地沉在下面
for _ in range(8):
    st.text("")

# --- 4. 按钮与惊喜 ---

# 创建两列，用来把按钮挤在中间（虽然 mobile 默认也是居中，这样更保险）
col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    # === 按钮文字 (请在这里修改) ===
    if st.button("✨ 点开，有一份小惊喜"):
        # 1. 撒花特效
        st.balloons() 
        
        # 2. 弹出信息 (请在这里修改礼物/快递信息)
        st.success("聪明可爱、温柔善良的公主✨\n你的专属小熊正乖乖等着被你解救～")
        
        st.info("""
        **📍 见面地点**: 幸福路 520 号 \n\n
        **🔐 专属暗号**: 小猪快跑 \n
        """)

