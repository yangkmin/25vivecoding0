import streamlit as st

# 이모지 딕셔너리 (예시로 일부만 수록)
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
    for job in career_recommendation[selected_mbti]:
        st.markdown(f"- 🌟 **{job}**")

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
