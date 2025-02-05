import random
import streamlit as st
import time

# 로또 번호 생성 함수
def when_start():
    로또번호맞추기 = []
    while len(로또번호맞추기) < 6:
        이미뽑은숫자 = random.randint(1, 45)
        if 이미뽑은숫자 not in 로또번호맞추기:
            로또번호맞추기.append(이미뽑은숫자)
    return 로또번호맞추기

# Streamlit 설정
st.set_page_config(page_title="로또 번호 추첨기", page_icon="🎰", layout="centered")

# 헤더와 설명 추가
st.title("🎉 로또 번호 추첨기 🎉")
st.write("자, 이제 로또 번호를 추첨해볼 시간입니다! 버튼을 눌러 로또 번호를 확인해보세요.")
st.markdown("___")

# 추첨 버튼을 누르면 로또 번호를 생성하는 코드
if st.button("로또 번호 추첨 시작!"):
    with st.spinner("로또 번호를 뽑는 중... 잠시만 기다려주세요."):
        time.sleep(2)  # 약간의 지연 효과
        로또번호 = when_start()
    # 로또 번호 출력
    st.subheader("🎟️ 당첨 번호 🎟️")
    st.write("이번 주 로또 당첨 번호는 다음과 같습니다!")
    st.markdown(f"**{', '.join(map(str, 로또번호))}**")
    st.success("🎉 축하합니다! 당첨을 기원합니다! 🎉")

# 예쁘게 꾸미기
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stMarkdown {
        font-size: 18px;
        text-align: center;
    }
    .stTitle {
        font-size: 36px;
        text-align: center;
    }
    .stSubheader {
        font-size: 28px;
        font-weight: bold;
        color: #ff6347;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)
