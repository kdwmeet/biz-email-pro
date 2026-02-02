from openai import OpenAI
from dotenv import load_dotenv
import os
from app.config import MODEL_NAME, TONE_OPTIONS, SYSTEM_PROMPT_TEMPLATE

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email(draft, recipient, tone_key, sender_name, language):
    """
    이메일 초안을 받아 비즈니스 이메일로 변환하는 함수
    """
    try:
        # 선택된 톤에 맞는 상제 지침 가져오기
        tone_description = TONE_OPTIONS.get(tone_key, TONE_OPTIONS["Professional (기본)"])

        # 시스템 프롬프트 완성
        system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
            recipient=recipient,
            tone_description=tone_description,
            language=language
        )

        # 사용자 메시지 구성
        user_message = f"""
        [발신자 이름]: {sender_name}
        [초안 내용]:
        {draft}
        """

        # API 호출
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=1
        )

        return response.choices[0].message.content
    
    except Exception as e:
        return f"이메일 생성 중 오류가 발생했습니다: {str(e)}"