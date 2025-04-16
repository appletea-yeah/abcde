import streamlit as st

# MBTI 유형과 설명 데이터
mbti_types = {
    "INTJ": "Architect: 전략적이고 독창적인 사고를 하며, 목표 지향적입니다.",
    "INTP": "Thinker: 호기심이 많고 분석적인 문제 해결을 좋아합니다.",
    "ENTJ": "Commander: 리더십이 뛰어나고 결단력이 강합니다.",
    "ENTP": "Debater: 창의적이고 논쟁을 즐깁니다.",
    "INFJ": "Advocate: 깊은 통찰력과 강한 가치관을 가지고 있습니다.",
    "INFP": "Mediator: 이상주의적이며 감정적으로 깊이 연결되는 것을 원합니다.",
    "ENFJ": "Protagonist: 다른 사람을 돕는 것을 즐기며, 종종 지도자 역할을 맡습니다.",
    "ENFP": "Campaigner: 창의적이고 열정적이며 자유를 중시합니다.",
    "ISTJ": "Logistician: 신뢰할 수 있고 책임감 있으며, 세부 사항을 중요시합니다.",
    "ISFJ": "Defender: 친절하고 배려가 많으며, 남을 돕는 것을 선호합니다.",
    "ESTJ": "Executive: 조직적이고 책임감 있으며, 실용적으로 접근합니다.",
    "ESFJ": "Consul: 사교적이며 사람들과의 조화를 중시합니다.",
    "ISTP": "Virtuoso: 실용적이고 즉각적인 문제 해결을 선호합니다.",
    "ISFP": "Adventurer: 감각적이고 예술적인 경험을 선호합니다.",
    "ESTP": "Entrepreneur: 활동적이고 적응력이 뛰어나며, 모험을 즐깁니다.",
    "ESFP": "Entertainer: 사교적이며, 즐거움을 주는 것을 중요하게 생각합니다.",
}

# Streamlit 애플리케이션
st.title("MBTI 성격 유형 설명")

# MBTI 유형 선택
selected_type = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_types.keys()))

# 선택한 유형에 대한 설명 표시
if selected_type:
    st.write(f"**{selected_type}**: {mbti_types[selected_type]}")

import streamlit as st

st.title("나의 첫번째 스트림릿 사이트")
st.write("안녕하세요. 어수진입니다.")
