import streamlit as st
from app.generator import generate_email
from app.config import TONE_OPTIONS, SUPPORTED_LANGUAGES

st.set_page_config(page_title="Global Biz-Email", layout="centered")

# --- 헤더 ---
st.title("Global Biz-Email")
st.divider()

# --- 입력 섹션 ---
col1, col2 = st.columns(2)
with col1:
    recipient = st.text_input("받는 사람 (Recipient)", placeholder="Mr. John Doe")
with col2:
    sender = st.text_input("보내는 사람 (Sender)", placeholder="Gildong Hong")

# 옵션 선택 (3단 컬럼)
opt_col1, opt_col2 = st.columns(2)
with opt_col1:
    tone_selection = st.selectbox("분위기 (Tone)", list(TONE_OPTIONS.keys()))
with opt_col2:
    # 언어 선택창 추가
    language_selection = st.selectbox("작성 언어 (Output Language)", SUPPORTED_LANGUAGES)

# 초안 입력
draft_text = st.text_area(
    "이메일 초안",
    height=150,
    placeholder="예시: 지난번에 보낸 샘플 잘 받았어. 근데 색깔이 우리가 원하던 거랑 좀 다르더라. 다음 주까지 수정해서 다시 보내줄 수 있어? 급한 건이라 부탁 좀 할게."
)

# --- 실행 버튼 ---
if st.button("프로페셔널한 이메일로 변환", type="primary", use_container_width=True):
    if not draft_text:
        st.warning("이메일 내용을 입력해주세요")
    else:
        with st.spinner("최고의 비즈니스 표현을 고르는 중..."):
            # 로직 호출
            final_email = generate_email(draft_text, recipient, tone_selection, sender, language_selection)

            st.success("작성완료! 아래 내용을 복사해서 사용하세요.")
            st.divider()

            # 결과 출력
            st.markdown("Generated Email")
            with st.container(border=True):
                st.markdown(final_email)

            # 팁
            st.info("Tip: '단호함' 톤을 선택하면 납기 지연이나 클레임 메일에 효과적입니다.")