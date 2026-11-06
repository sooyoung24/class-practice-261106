import html

import streamlit as st


st.set_page_config(
    page_title="나의 소개",
    page_icon="🌸",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff8fb 0%, #f7fbff 50%, #f8fff8 100%);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .hero {
        padding: 3rem 2rem;
        margin-bottom: 1.5rem;
        border-radius: 24px;
        background: linear-gradient(120deg, #ffd9e8, #dceeff);
        text-align: center;
        box-shadow: 0 12px 30px rgba(96, 104, 120, 0.08);
    }

    .hero h1 {
        margin-bottom: 0.3rem;
        color: #4a4055;
        font-size: 3rem;
    }

    .hero p {
        color: #686176;
        font-size: 1.1rem;
    }

    .profile-card {
        min-height: 180px;
        height: 100%;
        padding: 1.4rem;
        border-radius: 18px;
        background: rgba(255, 255, 255, 0.78);
        border: 1px solid rgba(255, 255, 255, 0.9);
        box-shadow: 0 8px 24px rgba(96, 104, 120, 0.08);
    }

    .profile-card h3 {
        margin-top: 0;
        color: #56505f;
        font-size: 1.15rem;
    }

    .profile-card p {
        color: #67616d;
        white-space: pre-wrap;
    }

    .section-title {
        margin-top: 1.5rem;
        color: #4f4859;
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea {
        border-radius: 12px;
        background-color: rgba(255, 255, 255, 0.9);
    }

    div.stButton > button {
        border-radius: 999px;
        border: none;
        padding: 0.55rem 1.4rem;
        background: #b7d8f2;
        color: #37485a;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background: #ffd0de;
        color: #57404a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

defaults = {
    "name": "OOO",
    "affiliation": "OO대학교 OOO학과",
    "dream": "사람들에게 도움이 되는 서비스를 만들고 싶어요.",
    "travels": "제주도, 부산, 일본 도쿄",
    "likes": "좋아하는 음식, 음악, 영화, 계절",
    "hobbies": "독서, 사진 찍기, 산책하기, 맛집 탐방",
    "introduction": "저는 새로운 것을 배우고 직접 만들어 보는 것을 좋아합니다. 작은 경험을 쌓아 저만의 이야기를 만들어 가고 싶어요.",
}

if "profile" not in st.session_state:
    st.session_state.profile = defaults.copy()

safe_profile = {
    key: html.escape(str(value))
    for key, value in st.session_state.profile.items()
}

st.markdown(
    f"""
    <section class="hero">
        <h1>🌸 안녕하세요, 저는 {safe_profile['name']}입니다</h1>
        <p>배우고, 여행하고, 좋아하는 일을 찾아가는 일상을 기록합니다.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h2 class="section-title">나에 대해</h2>', unsafe_allow_html=True)
profile_col1, profile_col2 = st.columns([2, 3])

with profile_col1:
    st.markdown(
        f"""
        <div class="profile-card" style="background: #fff0f5;">
            <h3>👋 한 줄 소개</h3>
            <p>{safe_profile['introduction']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with profile_col2:
    st.markdown(
        f"""
        <div class="profile-card" style="background: #edf7ff;">
            <h3>🎓 소속</h3>
            <p>{safe_profile['affiliation']}</p>
            <h3>🚀 나의 꿈</h3>
            <p>{safe_profile['dream']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<h2 class="section-title">취향과 경험</h2>', unsafe_allow_html=True)
card1, card2, card3 = st.columns(3)

card_data = [
    (card1, "🧳 여행했던 곳", "travels", "#fff4d8"),
    (card2, "💗 좋아하는 것", "likes", "#f6edff"),
    (card3, "🎨 취미", "hobbies", "#e8f8ef"),
]

for column, title, key, background in card_data:
    with column:
        st.markdown(
            f"""
            <div class="profile-card" style="background: {background};">
                <h3>{title}</h3>
                <p>{safe_profile[key]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<h2 class="section-title">내 소개 직접 작성하기</h2>', unsafe_allow_html=True)
st.caption("아래 내용을 자유롭게 수정한 뒤 저장 버튼을 눌러주세요.")

with st.form("profile_form"):
    input_col1, input_col2 = st.columns(2)

    with input_col1:
        name = st.text_input("이름", value=st.session_state.profile["name"], max_chars=30)
        affiliation = st.text_input("소속", value=st.session_state.profile["affiliation"])
        dream = st.text_area("나의 꿈", value=st.session_state.profile["dream"])
        travels = st.text_area("여행했던 곳", value=st.session_state.profile["travels"])

    with input_col2:
        likes = st.text_area("좋아하는 것", value=st.session_state.profile["likes"])
        hobbies = st.text_area("취미", value=st.session_state.profile["hobbies"])
        introduction = st.text_area("한 줄 소개", value=st.session_state.profile["introduction"])

    saved = st.form_submit_button("소개 저장하기")

if saved:
    st.session_state.profile = {
        "name": name,
        "affiliation": affiliation,
        "dream": dream,
        "travels": travels,
        "likes": likes,
        "hobbies": hobbies,
        "introduction": introduction,
    }
    st.success("소개가 저장되었습니다! 위쪽 카드도 함께 변경됩니다.")
    st.rerun()
