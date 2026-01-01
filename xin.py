import streamlit as st
import google.generativeai as genai

# 設定頁面配置
st.set_page_config(page_title="古風譯站", page_icon="📜")

# 設定背景風格 (簡單的 CSS 營造書卷氣)
st.markdown("""
    <style>
    .main { background-color: #f5f5dc; }
    h1 { color: #5d4037; font-family: "Microsoft JhengHei", serif; }
    </style>
""", unsafe_allow_html=True)

st.title("📜 古風文言文翻譯器")
st.subheader("將你的現代白話，化作千古名篇")

# 1. 配置 AI (這裡以 Gemini 為例，你需要自己的 API Key)
# 如果沒有 Key，也可以改用簡單的提示詞介面
api_key = st.sidebar.text_input("輸入你的 Gemini API Key:", type="password")

# 2. 側邊欄選項
style = st.sidebar.selectbox(
    "選擇文體風格",
    ["標準文言文", "江湖武俠風格", "朝廷奏摺風格", "詩經四言風格", "婉約宋詞風格"]
)

# 3. 輸入區域
input_text = st.text_area("在此輸入你的白話文 (例如：我今天不想上班，想去吃拉麵):", height=150)

if st.button("開始轉譯"):
    if not api_key:
        st.error("請在左側輸入 API Key 才能召喚文曲星下凡！")
    elif input_text:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"請將以下這段現代白話文翻譯成{style}的文言文。僅輸出翻譯後的結果，不要有任何解釋：\n\n{input_text}"
            
            with st.spinner("正在研墨揮毫..."):
                response = model.generate_content(prompt)
                
            # 4. 顯示結果
            st.divider()
            st.markdown(f"### 【{style}結果】")
            st.success(response.text)
            st.button("複製結果", on_click=lambda: st.write(f"已複製: {response.text}")) # 註：複製功能通常需配合 JS

        except Exception as e:
            st.error(f"文思枯竭，發生錯誤: {e}")
    else:
        st.warning("請先輸入文字。")
