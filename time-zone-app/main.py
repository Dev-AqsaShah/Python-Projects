
#rquird lebs
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Define available time zones
TIME_ZONE = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("Time Zone App")

# Select multiple timezones
selected_timezone = st.multiselect("Select Timezones", TIME_ZONE, default=["UTC", "Asia/Karachi"])

st.subheader("Selected Timezones")
for tz in selected_timezone:
    try:
        current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        st.write(f"**{tz}**: {current_time}")
    except Exception as e:
        st.error(f"Error fetching time for {tz}: {e}")

# Time conversion section
st.subheader("Current Time Between Timezones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONE, index=0)  # Fixed here
to_tz = st.selectbox("To Timezone", TIME_ZONE, index=1)

if st.button("Convert Time"):
    try:
        # Get the current date and combine with selected time
        dt = datetime.now(ZoneInfo(from_tz)).replace(
            hour=current_time.hour,
            minute=current_time.minute,
            second=current_time.second,
            microsecond=0
        )

        # Convert to target timezone
        converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")

        st.success(f"Converted Time in {to_tz}: {converted_time}")
    except Exception as e:
        st.error(f"Error in time conversion: {e}")
