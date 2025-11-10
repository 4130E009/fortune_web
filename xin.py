import streamlit as st
import random
import datetime

# 🌐 頁面設定
st.set_page_config(page_title="每日一句", page_icon="🔮", layout="centered")

# 🧙‍♀️ 頁首設計
st.markdown(
    """
    <h1 style='text-align:center; color:#fcd34d;'>🔮 每日一句 🔮</h1>
    <p style='text-align:center; color:#e9d5ff;'>輸入名字與生日，讓宇宙告訴你今日的命運與靈光。</p>
    """,
    unsafe_allow_html=True,
)

# 🧮 星座判斷
def get_zodiac(month, day):
    zodiacs = [
        ("摩羯座", (12, 22), (1, 19)),
        ("水瓶座", (1, 20), (2, 18)),
        ("雙魚座", (2, 19), (3, 20)),
        ("牡羊座", (3, 21), (4, 19)),
        ("金牛座", (4, 20), (5, 20)),
        ("雙子座", (5, 21), (6, 20)),
        ("巨蟹座", (6, 21), (7, 22)),
        ("獅子座", (7, 23), (8, 22)),
        ("處女座", (8, 23), (9, 22)),
        ("天秤座", (9, 23), (10, 22)),
        ("天蠍座", (10, 23), (11, 21)),
        ("射手座", (11, 22), (12, 21)),
    ]
    for sign, start, end in zodiacs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "未知星座"

# 🧧 運勢與元素
fortunes = [
    "在非洲，每六十秒，就有一分鐘過去。",
    "凡是每天喝水的人，有高機率在100年內死去。",
    "只要每天省下買一杯奶茶的錢，十天後就能買十杯奶茶。",
    "你的笑容將打開一扇門，只是別太快關上它。",
    "當你的左臉被人打，那你的左臉就會痛。",
    "成功的男人背後都有一個脊椎。",
    "如果你瞎了你就會看不見。",
]

items = ["一坨狗屎", "一顆原子彈", "大拇指指甲", "好市多胡椒鹽", "冰箱裡最後一顆蛋", "一支鐵鎚", "口袋裡的垃圾"]

# 🧾 表單區
with st.form("fortune_form"):
    name = st.text_input("名字：", "")
    birthday = st.date_input(
        "生日：",
        datetime.date(2000, 1, 1),
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today()
    )
    submitted = st.form_submit_button("開始 ✨")

# 🎯 結果顯示區
if submitted:
    zodiac = get_zodiac(birthday.month, birthday.day)
    fortune = random.choice(fortunes)
    item = random.choice(items)

    st.markdown(
        f"""
        <div style='background-color:#3b1d5f; border-radius:15px; padding:20px; margin-top:15px;'>
        <h3 style='text-align:center; color:#fcd34d;'>✨ {name}（{zodiac}） ✨</h3>
        <p style='text-align:center; color:#f9fafb; font-size:18px;'>{fortune}</p>
        <hr style='border:1px solid #a78bfa;'>
        <p style='text-align:center; color:#c4b5fd;'>🍀 幸運物：<b>{item}</b></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
