import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    page_title="🏢 Office Hours Tracker",
    page_icon="🏢",
    layout="centered"
)

# ---------- SETTINGS ----------
WORKDAY_HOURS = 8
# ------------------------------

st.title("🏢 Office Hours Tracker")
st.caption("Track your working day in real time.")

start_time = st.time_input(
    "🕗 What time did you start working today?",
    value=datetime.now().replace(hour=9, minute=0).time()
)

now = datetime.now()

start = datetime.combine(now.date(), start_time)

# If someone starts before midnight and checks after midnight
if start > now:
    start -= timedelta(days=1)

worked = now - start

worked_seconds = worked.total_seconds()

goal_seconds = WORKDAY_HOURS * 3600

progress = min(worked_seconds / goal_seconds, 1.0)

remaining = max(goal_seconds - worked_seconds, 0)

leave_time = start + timedelta(hours=WORKDAY_HOURS)

# ---------- HEADER ----------
st.markdown("---")

col1, col2 = st.columns(2)

col1.metric(
    "🕒 Current Time",
    now.strftime("%I:%M:%S %p")
)

col2.metric(
    "🏃 Leave At",
    leave_time.strftime("%I:%M %p")
)

st.markdown("---")

# ---------- BIG TIMER ----------

hours = int(worked_seconds // 3600)
minutes = int((worked_seconds % 3600) // 60)
seconds = int(worked_seconds % 60)

st.markdown(
    f"""
    <h1 style='text-align:center;font-size:70px'>
    {hours:02}:{minutes:02}:{seconds:02}
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<h4 style='text-align:center'>Time worked today</h4>",
    unsafe_allow_html=True,
)

st.progress(progress)

st.write(f"### {progress*100:.1f}% of your workday completed")

st.markdown("---")

# ---------- STATS ----------

c1, c2, c3 = st.columns(3)

c1.metric(
    "✅ Worked",
    f"{hours}h {minutes}m"
)

remaining_hours = int(remaining // 3600)
remaining_minutes = int((remaining % 3600)//60)

c2.metric(
    "⌛ Remaining",
    f"{remaining_hours}h {remaining_minutes}m"
)

coffee = int(worked_seconds // (2 * 3600))

c3.metric(
    "☕ Coffee Earned",
    coffee
)

st.markdown("---")

if progress >= 1:
    st.balloons()

    st.success("🎉 Congratulations! You completed today's workday.")
else:
    st.info(
        f"Keep going! Only {remaining_hours}h {remaining_minutes}m left."
    )

