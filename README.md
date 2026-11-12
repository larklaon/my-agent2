# Streamlit 실습

- **챗봇**은 LangChain과 GPT-5.4 mini를 사용하며, 최신 정보가 필요할 때 Tavily로 웹을 검색해 답변 아래에 출처를 표시합니다. 페이지를 이동해도 현재 세션의 대화 기록을 유지합니다.
- **엑셀 미리보기**에서 하나 이상의 `.xlsx` 또는 `.xls` 파일을 올려 첫 번째 시트를 확인할 수 있습니다.
- **환율 조회**는 Frankfurter에서 최신 기준 환율을 가져와 입력한 금액을 환산합니다. 환율 조회에는 API 키가 필요 없습니다.

## 로컬 실행

Python 3.13 가상환경에서 실행합니다.

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

챗봇을 사용하려면 `app.py` 옆의 `.env` 파일에 OpenAI API 키를 저장하세요. 웹 검색에는 Tavily API 키도 필요합니다. 키를 저장한 뒤 앱을 다시 실행하세요. [Tavily API 키 발급](https://app.tavily.com/)

```dotenv
OPENAI_API_KEY=여기에_OpenAI_API_키_입력
TAVILY_API_KEY=여기에_Tavily_API_키_입력
```

## Streamlit Community Cloud 배포

저장소를 선택하고 메인 파일을 `app.py`로 지정합니다. 고급 설정에서 Python 3.13을 선택하고, 챗봇과 웹 검색에 사용할 키를 Secrets에 추가합니다.

```toml
OPENAI_API_KEY = "여기에_OpenAI_API_키_입력"
TAVILY_API_KEY = "여기에_Tavily_API_키_입력"
```
