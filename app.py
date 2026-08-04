import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Office Time Calculator")

st.title("🏢 Office Time Calculator")

start_date = st.date_input(
    "When did you join the company?",
    value=date.today()
)

today = date.today()

if start_date <= today:

    diff = relativedelta(today, start_date)

    total_days = (today - start_date).days
    total_weeks = total_days // 7
    total_months = diff.years * 12 + diff.months

    st.metric(
        "Time at the company",
        f"{diff.years} years, {diff.months} months"
    )

    st.write(f"**Days:** {total_days}")
    st.write(f"**Weeks:** {total_weeks}")
    st.write(f"**Months:** {total_months}")

else:
    st.error("Choose a valid date.")
