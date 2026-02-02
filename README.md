# Global Biz-Email Pro

## 1. 프로젝트 개요

Global Biz-Email Pro는 사용자가 입력한 비정형의 이메일 초안(Rough Draft)을 분석하여, 상황과 목적에 맞는 전문적인 비즈니스 이메일로 자동 변환해 주는 생성형 AI 솔루션입니다.

언어 장벽과 비즈니스 에티켓으로 인한 커뮤니케이션 비용을 절감하기 위해 개발되었으며, OpenAI의 최신 경량화 모델인 **gpt-5-mini**를 활용하여 높은 정확도와 빠른 응답 속도를 제공합니다. 사용자는 단순한 의도만 입력하면, 선택한 언어와 톤앤매너(Tone & Manner)에 맞춰 완벽하게 격식을 갖춘 이메일을 즉시 생성할 수 있습니다.

### 주요 특징
* **다국어 비즈니스 지원:** 영어, 일본어(경어), 중국어, 스페인어 등 주요 비즈니스 언어 지원.
* **톤앤매너 조절:** 상황에 따라 '정중함', '단호함', '친근함', '사과', '설득' 등 5가지 화법 선택 가능.
* **페르소나 기반 생성:** 단순 번역이 아닌, '비즈니스 커뮤니케이션 전문가' 페르소나를 통해 문맥에 맞는 고급 표현 사용.
* **모듈형 아키텍처:** 설정, 로직, UI가 분리된 구조로 유지보수 및 확장이 용이함.

## 2. 시스템 아키텍처

본 프로젝트는 사용자 입력을 받아 프롬프트를 최적화하고, LLM을 통해 텍스트를 생성하는 파이프라인으로 구성됩니다.

1.  **Input Layer:** 사용자가 수신자, 발신자, 상황별 톤, 언어, 그리고 초안 내용을 입력.
2.  **Prompt Engineering Layer:** 선택된 옵션(언어, 톤)을 기반으로 최적화된 시스템 프롬프트 동적 생성.
3.  **Generation Layer:** OpenAI gpt-5-mini 모델이 입력된 의도를 해석하고 타겟 언어의 비즈니스 양식으로 변환.
4.  **Output Layer:** 생성된 이메일을 사용자가 복사 및 수정 가능한 형태로 UI에 출력.

## 3. 기술 스택

* **Language:** Python 3.10 이상
* **AI Model:** OpenAI gpt-5-mini
* **Framework:** Streamlit (Web UI)
* **Client:** OpenAI Python SDK
* **Configuration:** python-dotenv

## 4. 프로젝트 구조

실무 환경을 고려하여 설정 파일과 비즈니스 로직을 분리한 모듈형 구조를 채택하였습니다.

```text
biz-email-pro/
├── .env                  # 환경 변수 (API Key)
├── requirements.txt      # 의존성 패키지 목록
├── main.py               # 애플리케이션 진입점 (UI)
└── app/                  # 핵심 모듈 패키지
    ├── __init__.py
    ├── config.py         # 지원 언어, 톤앤매너 옵션, 프롬프트 템플릿 관리
    └── generator.py      # OpenAI API 호출 및 응답 처리 로직
```
## 5. 설치 및 실행 가이드
### 5.1. 사전 준비
Python 환경이 설치되어 있어야 합니다. 터미널에서 저장소를 복제하고 프로젝트 디렉토리로 이동하십시오.

```Bash
git clone [레포지토리 주소]
cd biz-email-pro
```
### 5.2. 의존성 설치
필요한 라이브러리를 설치합니다.

```Bash
pip install -r requirements.txt
```
### 5.3. 환경 변수 설정
프로젝트 루트 경로에 .env 파일을 생성하고, 유효한 OpenAI API 키를 입력하십시오. 본 프로젝트는 gpt-5-mini 모델을 사용합니다.

```Ini, TOML
OPENAI_API_KEY=sk-your-api-key-here
```
### 5.4. 실행
Streamlit 애플리케이션을 실행합니다.

```Bash
streamlit run main.py
```
## 6. 사용 시나리오 예시
### 시나리오 1: 납기 지연에 대한 항의 (영어)
* **입력**: "물건이 약속한 날짜에 안 왔습니다. 내일까지 안 오면 계약 파기합니다."

* **설정**: 톤(Firm/단호함), 언어(English)

* **결과**: "We are writing to express our serious concern regarding the delay... If the delivery is not completed by tomorrow, we will be forced to terminate the contract."

### 시나리오 2: 거래처 안부 인사 및 제안 (일본어)
* **입력**: "오랜만입니다. 잘 지내시죠? 이번에 저희 신제품 나왔는데 한번 검토 부탁드립니다."

* **설정**: 톤(Friendly/친근함), 언어(Japanese)

* **결과**: "平素より大変お世話になっております。ご無沙汰しておりますが、いかがお過ごしでしょうか... つきましては、ぜひ貴社にてご検討いただけますと幸いです。"

## 실행화면
<img width="722" height="634" alt="스크린샷 2026-02-02 145859" src="https://github.com/user-attachments/assets/fc6c74f7-87bc-40d7-8104-a340a03be7d7" />

<img width="706" height="764" alt="스크린샷 2026-02-02 145905" src="https://github.com/user-attachments/assets/8a7d681f-4bb8-4985-bd76-a6a98f37d7b8" />
