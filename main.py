import streamlit as st

# 이모지 딕셔너리
mbti_emoji = {
    "ISTJ": "📊💼🔍",
    "ISFJ": "🧑‍⚕️🌿🎨",
    "INFJ": "🔮📝🌌",
    "INTJ": "🧠📐🚀",
    "ISTP": "🔧🚗🕵️",
    "ISFP": "🎨🌈🐾",
    "INFP": "📖🎭🌱",
    "INTP": "🧪💡🤖",
    "ESTP": "🏎️🎯🎉",
    "ESFP": "🎤🎬🌟",
    "ENFP": "🧚🎨🌍",
    "ENTP": "🛠️🧠💬",
    "ESTJ": "📈🏛️🧭",
    "ESFJ": "🎀👩‍🏫🍰",
    "ENFJ": "🌟📢🤝",
    "ENTJ": "🏆📊👑"
}

career_recommendation = {
    "ISTJ": ["회계사", "데이터 분석가", "법무사"],
    "ISFJ": ["간호사", "초등교사", "미술 치료사"],
    "INFJ": ["상담가", "작가", "사회운동가"],
    "INTJ": ["과학자", "전략기획가", "AI 연구원"],
    "ISTP": ["기계공학자", "탐정", "자동차 기술자"],
    "ISFP": ["디자이너", "수의사", "플로리스트"],
    "INFP": ["시인", "심리학자", "환경운동가"],
    "INTP": ["프로그램 개발자", "이론 물리학자", "로봇공학자"],
    "ESTP": ["스턴트 배우", "기업 영업", "이벤트 플래너"],
    "ESFP": ["연예인", "패션 스타일리스트", "MC"],
    "ENFP": ["브랜드 디자이너", "여행 작가", "홍보 전문가"],
    "ENTP": ["혁신가", "정치 컨설턴트", "UX 디자이너"],
    "ESTJ": ["프로젝트 매니저", "군인", "경영 컨설턴트"],
    "ESFJ": ["학교 선생님", "파티 기획자", "간호조무사"],
    "ENFJ": ["사회복지사", "강연가", "홍보부장"],
    "ENTJ": ["CEO", "변호사", "금융 전략가"]
}

career_explanation = {
    "회계사": "ISTJ의 꼼꼼하고 신중한 성격은 정확한 숫자 계산과 재무 관리에 매우 적합합니다.",
    "데이터 분석가": "ISTJ는 분석적 사고에 강하고 체계적인 성향이 있어 데이터 기반 직업에 잘 어울립니다.",
    "법무사": "책임감 있고 원칙을 중요시하는 ISTJ는 법률과 관련된 일에 뛰어난 능력을 발휘합니다.",
    "간호사": "ISFJ는 헌신적이고 따뜻한 마음을 지녀 타인을 돌보는 직업에 잘 맞습니다.",
    "초등교사": "아이들을 섬세하게 배려하는 ISFJ는 교육 분야에서 안정적이고 효과적인 역할을 할 수 있습니다.",
    "미술 치료사": "감성적이고 치유적인 성향의 ISFJ에게 이상적인 창의-치유 융합 직업입니다.",
    # (추가적으로 필요한 설명은 이어서 입력 가능)
}

st.set_page_config(page_title="✨MBTI 직업 추천기✨", page_icon="🧠")
st.title("🌟 MBTI 기반 직업 추천 웹앱 🌈")
st.markdown("""
<div style='text-align:center; font-size:20px;'>
    당신의 MBTI에 어울리는 멋진 직업을 추천해드릴게요! 💖<br>
    아래에서 MBTI를 선택하세요 😄
</div>
""", unsafe_allow_html=True)

mbti_types = list(mbti_emoji.keys())
selected_mbti = st.selectbox("🔍 MBTI를 선택하세요:", mbti_types, index=0)

if selected_mbti:
    st.markdown(f"### 당신의 MBTI: **{selected_mbti}** {mbti_emoji[selected_mbti]}")
    st.markdown("---")
    st.subheader("🎯 추천 직업 리스트")
    selected_job = st.radio("아래 직업 중 하나를 클릭해보세요:", career_recommendation[selected_mbti])

    if selected_job:
        st.markdown(f"#### 💬 {selected_job} 추천 이유")
        st.info(career_explanation.get(selected_job, "아직 설명이 준비되지 않았어요. 조금만 기다려 주세요! 🙏"))

    st.balloons()
    st.markdown("---")
    st.markdown("""
    <div style='text-align:center;'>
        더 많은 콘텐츠가 곧 업데이트될 예정입니다! 🚀<br>
        언제든 돌아와 주세요 😊
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to right, #fceabb, #f8b500);
        color: #333333;
        font-family: 'Comic Sans MS', cursive;
    }
</style>
""", unsafe_allow_html=True)
