import streamlit as st
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

st.set_page_config(
    page_title="Office Time Calculator",
    page_icon="🏢",
    layout="centered"
)

st.title("🏢 Office Time Calculator")
st.caption("Calculate how long you've been at the company.")

start_date = st.date_input(
    "📅 Select your start date",
    value=date.today()
)

today = date.today()

if start_date > today:
    st.error("Start date cannot be in the future.")
    st.stop()

diff = relativedelta(today, start_date)

total_days = (today - start_date).days
total_weeks = total_days // 7
total_months = diff.years * 12 + diff.months

st.divider()

c1, c2, c3 = st.columns(3)

c1.metric("Years", diff.years)
c2.metric("Months", diff.months)
c3.metric("Days", diff.days)

st.divider()

c4, c5, c6 = st.columns(3)

c4.metric("Total Days", f"{total_days:,}")
c5.metric("Total Weeks", f"{total_weeks:,}")
c6.metric("Total Months", total_months)

next_anniversary = date(start_date.year + diff.years + 1, start_date.month, start_date.day)
days_left = (next_anniversary - today).days

st.divider()

st.success(
    f"🎉 You've been at the company for **{diff.years} years, {diff.months} months, and {diff.days} days.**"
)

st.info(f"🏆 Next work anniversary in **{days_left} days**.")
