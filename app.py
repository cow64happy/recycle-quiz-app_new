import streamlit as st

st.set_page_config(page_title="재활용 지도 앱", page_icon="🌍", layout="wide")
st.title("♻️ 2023년 분리배출량 지도 보기")

st.write("2023년 도시별 재활용 분리배출량 데이터를 시각화한 지도입니다.")

st.markdown(
    '[🗺️ 2023년 지도 보기](https://cow64happy.github.io/recycle-quiz-app_new/재활용_맵_2023.html)',
    unsafe_allow_html=True
)
