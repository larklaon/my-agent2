import requests
import streamlit as st

CURRENCIES = ["USD", "KRW", "EUR", "JPY", "GBP", "CNY", "AUD", "CAD", "CHF", "HKD", "SGD"]

st.title("환율 조회")

with st.form("exchange_rate"):
    amount = st.number_input("환전 금액", min_value=0.0, value=100.0, step=1.0)
    base_column, quote_column = st.columns(2)
    base = base_column.selectbox("기준 통화", CURRENCIES)
    quote = quote_column.selectbox("환산 통화", CURRENCIES, index=1)
    submitted = st.form_submit_button("환율 조회", type="primary")

if submitted:
    if base == quote:
        st.metric("환산 금액", f"{amount:,.2f} {quote}")
        st.caption(f"1 {base} = 1 {quote}")
    else:
        try:
            response = requests.get(
                f"https://api.frankfurter.dev/v2/rate/{base}/{quote}", timeout=10
            )
            response.raise_for_status()
            data = response.json()
            rate = float(data["rate"])
            date = data["date"]
        except (requests.RequestException, ValueError, KeyError, TypeError):
            st.error("환율을 가져오지 못했습니다. 잠시 후 다시 시도해 주세요.")
        else:
            st.metric("환산 금액", f"{amount * rate:,.2f} {quote}")
            st.caption(f"1 {base} = {rate:,.8g} {quote} · {date} 기준 · Frankfurter")
