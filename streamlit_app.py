import streamlit as st

st.set_page_config(
    page_title="My Introduction",
    page_icon="🌸",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff6f8 0%, #f6f7ff 48%, #f1fbf7 100%);
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        text-align: center;
        padding: 3rem 1.5rem 2.5rem;
        margin-bottom: 2rem;
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 24px;
        box-shadow: 0 12px 30px rgba(120, 105, 140, 0.08);
    }

    .profile-photo {
        width: 112px;
        height: 112px;
        margin: 0 auto 1rem;
        display: grid;
        place-items: center;
        border-radius: 50%;
        background: #d9e7ff;
        color: #5d668a;
        font-size: 3rem;
    }

    .hero h1 {
        margin-bottom: 0.35rem;
        color: #4f5269;
        font-size: 2.6rem;
        letter-spacing: 0;
    }

    .hero p {
        margin: 0;
        color: #777a91;
        font-size: 1.05rem;
    }

    .section-title {
        margin: 0 0 1rem;
        color: #55586d;
        font-size: 1.45rem;
    }

    .info-card {
        min-height: 155px;
        padding: 1.25rem;
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(100, 100, 120, 0.07);
    }

    .lavender { background: #ebe6ff; }
    .peach { background: #ffe9dc; }
    .mint { background: #dff4ea; }
    .blue { background: #deefff; }
    .pink { background: #ffe5ed; }

    .card-emoji {
        font-size: 1.8rem;
        margin-bottom: 0.55rem;
    }

    .info-card h3 {
        margin: 0 0 0.55rem;
        color: #55586d;
        font-size: 1.05rem;
    }

    .info-card p {
        margin: 0;
        color: #707287;
        line-height: 1.55;
    }

    .intro-text {
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border-left: 5px solid #c9c1ee;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.68);
        color: #66687b;
        line-height: 1.7;
    }

    div[data-testid="stMarkdownContainer"] p {
        color: inherit;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="hero">
        <div class="profile-photo">🌷</div>
        <h1>안녕하세요, 저는 이수영입니다.</h1>
        <p>배우고 성장하는 것을 좋아하는 사람입니다.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="intro-text">저의 꿈과 관심사를 담은 작은 소개 페이지입니다. 아래 내용을 나만의 이야기로 자유롭게 바꾸어 보세요.</p>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">About me</h2>', unsafe_allow_html=True)
left, right = st.columns(2, gap="medium")

with left:
    st.markdown(
        """
        <article class="info-card lavender">
            <div class="card-emoji">🎓</div>
            <h3>소속</h3>
            <p>청주교육대학교 컴퓨터교육과에 재학 중입니다.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <article class="info-card peach">
            <div class="card-emoji">🌱</div>
            <h3>나의 꿈</h3>
            <p>사람에게 도움이 되는 서비스를 만드는 사람이 되고 싶습니다.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<h2 class="section-title" style="margin-top: 2rem;">My story</h2>', unsafe_allow_html=True)
story_col1, story_col2, story_col3 = st.columns(3, gap="medium")

with story_col1:
    st.markdown(
        """
        <article class="info-card mint">
            <div class="card-emoji">✈️</div>
            <h3>여행</h3>
            <p>제주도, 부산, 일본 등 새로운 곳을 여행하며 기억을 쌓고 있습니다.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with story_col2:
    st.markdown(
        """
        <article class="info-card blue">
            <div class="card-emoji">💙</div>
            <h3>좋아하는 것</h3>
            <p>좋아하는 음악을 듣고, 맛있는 카페를 찾고, 아름다운 하늘을 보는 것을 좋아합니다.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with story_col3:
    st.markdown(
        """
        <article class="info-card pink">
            <div class="card-emoji">🎨</div>
            <h3>취미</h3>
            <p>사진 찍기, 독서, 그림 그리기, 산책처럼 일상을 채우는 취미를 즐깁니다.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #88899c;'>오늘도 조금씩 성장하는 중 ✨</p>",
    unsafe_allow_html=True,
)
