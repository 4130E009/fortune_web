import tkinter as tk
import random
import datetime
from tkinter import messagebox

# 計算星座
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

# 算命邏輯
def tell_fortune():
    name = entry_name.get()
    birthday = entry_birthday.get()

    if not name or not birthday:
        messagebox.showwarning("⚠️ 警告", "請把名字、生日都填好！")
        return

    try:
        birth_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("😵‍💫 錯誤", "生日格式錯誤！請用 YYYY-MM-DD 格式。")
        return

    zodiac = get_zodiac(birth_date.month, birth_date.day)

    results = [
        "在非洲，每六十秒，就有一分鐘過去",
        "凡是每天喝水的人，有高機率在100年內死去",
        "只要每天省下買一杯奶茶的錢，十天後就能買十杯奶茶",
        "你的笑容將打開一扇門，只是別太快關上它。",
        "當你的左臉被人打，那你的左臉就會痛",
        "成功的男人背後都有一個脊椎"
        "如果你瞎了你就會看不見"
    ]

    fortune = random.choice(results)
    result_text.set(f"✨ {name}（{zodiac}） ✨\n\n{fortune}")

# --- 視覺設定 ---
root = tk.Tk()
root.title("每日一句")
root.geometry("420x460")
root.resizable(False, False)
root.configure(bg="#2e1a47")

# 標題
tk.Label(
    root,
    text="每日一句",
    font=("微軟正黑體", 20, "bold"),
    fg="#fcd34d",
    bg="#2e1a47"
).pack(pady=15)

# 名字
tk.Label(root, text="名字：", fg="#e9d5ff", bg="#2e1a47").pack()
entry_name = tk.Entry(root, justify="center", relief="flat", bg="#f3e8ff")
entry_name.pack(pady=3)

# 生日
tk.Label(root, text="生日（YYYY-MM-DD）：", fg="#e9d5ff", bg="#2e1a47").pack()
entry_birthday = tk.Entry(root, justify="center", relief="flat", bg="#f3e8ff")
entry_birthday.pack(pady=3)

# 按鈕
tk.Button(
    root,
    text="開始",
    command=tell_fortune,
    bg="#7c3aed",
    fg="white",
    activebackground="#a78bfa",
    activeforeground="white",
    relief="flat",
    font=("微軟正黑體", 12, "bold"),
    padx=15, pady=5
).pack(pady=15)

# 結果框
frame_result = tk.Frame(root, bg="#3b1d5f", bd=3, relief="groove")
frame_result.pack(padx=20, pady=10, fill="both", expand=True)

result_text = tk.StringVar()
tk.Label(
    frame_result,
    textvariable=result_text,
    wraplength=350,
    justify="center",
    font=("微軟正黑體", 12),
    fg="#fcd34d",
    bg="#3b1d5f"
).pack(pady=20)

root.mainloop()
import streamlit as st
import datetime

# 🌐 頁面設定
st.set_page_config(page_title="命運算命機", page_icon="🔮", layout="centered")

# 🧙‍♀️ 標題區
st.markdown(
    """
    <h1 style='text-align:center; color:#fcd34d;'>🔮 命運算命機 🔮</h1>
    <p style='text-align:center; color:#e9d5ff;'>輸入名字與生日，揭開今日的宇宙預言。</p>
    """,
    unsafe_allow_html=True,  # 這個就是讓 HTML / CSS 生效的關鍵
)

# 🧾 表單
with st.form("fortune_form"):
    name = st.text_input("名字：", "")
    birthday = st.date_input("生日：", datetime.date.today())
    submitted = st.form_submit_button("開始算命 🪄")

# 🪄 當使用者送出後要顯示的內容（你自己的算命邏輯塞這裡）
if submitted:
    # 這裡換成你自己的邏輯，例如星座、運勢、顏色、物品等等
    st.markdown(
        f"""
        <div style='background-color:#3b1d5f; border-radius:15px; padding:20px; margin-top:15px;'>
        <h3 style='text-align:center; color:#fcd34d;'>✨ {name} 的命運 ✨</h3>
        <p style='text-align:center; color:#f9fafb; font-size:18px;'>這裡顯示你的算命結果</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

