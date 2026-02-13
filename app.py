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
致世界上最好的宝宝：

Hi，我最可爱美丽善良大方的宝宝。

能重新走近你，是我这段时间以来最幸福的事。
谢谢你愿意再次走向我，也谢谢你让我在失去之后，
更清楚地看见自己该成为怎样的人。这段路让我明白，
真正珍贵的东西，不是不会失去，而是失而复得之后，会更懂得握紧。

是你让我知道，被人坚定地喜欢是多么幸福；
也是你让我学会，该怎么去坚定地珍惜一个人。
过去我没有做好的那些，这一次，我一定会紧紧握住你，稳稳地、好好地，
一起走更长的路。你不需要改变什么，做你自己就足够好。
而我，会努力成为那个始终让你安心、值得你信任的人。

今天情人节，虽然我们还没有真正重新出发，
但我还是想认真地对你说：我会把你在的每一天都当作礼物，
你的快乐，永远是我的头等大事。

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
        st.success("聪明可爱、温柔善良的公主宝宝✨\n 你的专属小熊正乖乖等着被你解救～")
        
        # 3. 详细信息
        st.info("""
        **📍 接头地点**: 【兔喜生活】万嘉学府店 \n\n
        **🔐 专属暗号**: 74-13075，61-13062 \n
        """)

