import streamlit as st

# MBTI 유형과 설명 데이터 (이모지 추가 및 내용 확장)
mbti_types = {
    "🌟 INTJ": "Architect: 독창적이고, 목표를 향한 전략적인 접근을 중요시합니다. \n\n"
               "이들은 분석적인 사고 능력이 뛰어나며, 새로운 시스템과 아이디어를 개발하는 것을 즐깁니다. "
               "지도자가 되기 위해 노력하며, 목표를 성취하는 데 필요한 모든 것을 계획합니다.",

    "💡 INTP": "Thinker: 분석적이고, 다양한 가능성을 탐구하는 것을 즐깁니다. \n\n"
               "문제 해결에 대한 깊은 관심이 있으며, 논리적이고 창의적인 방법으로 접근합니다. "
               "이들은 아이디어를 끊임없이 발전시키고, 새로운 지식을 탐구하는 것을 좋아합니다.",

    "👨‍💼 ENTJ": "Commander: 천부적인 리더십과 결단력을 가진 사람들입니다. \n\n"
                "이들은 팀을 이끌고 목표를 달성하기 위해 필요한 모든 자원을 조직하는 데 뛰어난 능력을 발휘합니다. "
                "비전을 실행할 수 있는 능력이 있으며, 도전을 즐깁니다.",

    "🗣️ ENTP": "Debater: 혁신적인 아이디어와 토론을 즐기는 사람들입니다. \n\n"
              "이들은 기존의 틀을 깨고 새로운 관점을 제시하며, 창의적인 접근을 통해 문제를 해결합니다. "
              "끊임없이 새로운 것에 도전하는 것을 좋아합니다.",

    "💖 INFJ": "Advocate: 깊은 통찰력과 강한 가치관을 가진 사람들입니다. \n\n"
               "이들은 다른 사람들의 감정을 이해하고 돕기를 원하며, 변화의 촉매 역할을 합니다. "
               "감정적으로 연결되기를 원하고, 삶의 깊은 의미를 추구합니다.",

    "🌈 INFP": "Mediator: 이상주의적이며, 사람들과의 깊은 관계를 중요시합니다. \n\n"
               "이들은 자신의 가치와 신념에 따라 행동하며, 다른 사람들에게 영감을 주려는 마음이 큽니다. "
               "예술, 문학, 음악 등 창의적인 표현을 좋아합니다.",

    "🌍 ENFJ": "Protagonist: 사람들을 돕는 것에서 만족을 느끼는 자연스러운 리더입니다. \n\n"
               "이들은 팀워크와 조화를 중요시하며, 다른 사람들의 잠재력을 끌어내는 데 능숙합니다. "
               "공감 능력이 뛰어나고, 긍정적인 변화를 이끌어내고자 합니다.",

    "🎉 ENFP": "Campaigner: 창의적이며 열정적인 성격을 가지고 있습니다. \n\n"
               "이들은 다양한 경험을 추구하며 사람들과의 교류를 즐깁니다. "
               "자유롭고 재미있는 활동을 선호하며, 새로운 아이디어를 탐구합니다.",

    "🧑‍🏫 ISTJ": "Logistician: 신뢰할 수 있고 책임감 있는 사람들입니다. \n\n"
                "이들은 사실과 세부 사항을 중요하게 생각하며, 체계적이고 실용적인 접근을 선호합니다. "
                "안정과 일관성을 중시합니다.",

    "👩‍👧 ISFJ": "Defender: 배려가 많고, 타인을 도와주는 것을 중시합니다. \n\n"
                "이들은 조용하지만 강한 헌신과 책임감을 가지고 있으며, 주변 사람들을 보호하려고 합니다. "
                "감정적 안정과 조화를 중시합니다.",

    "📈 ESTJ": "Executive: 조직적이고 실용적인 접근을 중요시합니다. \n\n"
               "이들은 일을 계획하고 올바르게 실행하는 데 뛰어난 능력을 발휘하며, 다른 사람들이 올바른 방향으로 나아가도록 돕습니다.",

    "🤝 ESFJ": "Consul: 사교적이고 따뜻한 사람들입니다. \n\n"
               "이들은 친구와의 관계를 소중히 여길 뿐만 아니라, 다른 사람들이 행복하도록 돕는 것을 즐깁니다. "
               "공감 능력이 뛰어나며, 조화를 중시합니다.",

    "🛠️ ISTP": "Virtuoso: 즉각적인 문제 해결과 실용적인 사고를 선호합니다. \n\n"
               "이들은 독립적인 성격을 가지고 있으며, 새로운 기술과 방법을 배우는 것을 좋아합니다. "
               "모험 정신이 강하고, 정직한 피드백을 원합니다.",

    "🎨 ISFP": "Adventurer: 감각적이고 예술적인 경험을 추구합니다. \n\n"
               "이들은 감성을 풍부하게 표현하고 창의적인 활동을 즐기며, 자연 속에서의 평화를 추구합니다.",

    "🚀 ESTP": "Entrepreneur: 활동적이고 즉흥적인 성격을 가진 사람들입니다. \n\n"
               "이들은 새로운 경험을 추구하고, 흥미로운 모험을 즐깁니다. "
               "다양한 도전을 직관적으로 해결하는 능력을 가지고 있습니다.",

    "🎤 ESFP": "Entertainer: 사람들과의 교류를 즐기며, 스포트라이트를 받는 것을 좋아합니다. \n\n"
               "이들은 사교적이고, 재미있고 기분 좋은 경험을 만드는 데 재능이 있습니다. "
               "자유롭고 즐거운 활동을 즐깁니다."
}

# Streamlit 애플리케이션
st.title("🌈 MBTI 성격 유형 설명")

# MBTI 유형 선택
selected_type = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_types.keys()))

# 선택한 유형에 대한 설명 표시
if selected_type:
    st.write(f"**{selected_type}**: {mbti_types[selected_type]}")
