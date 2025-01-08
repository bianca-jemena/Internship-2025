import streamlit as st

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Electricity Distribution Network",
    layout="centered"
)

col1, col2, col3 = st.columns([9, 11, 11])

# ---------------------------
# Jemena Image 
# ---------------------------
with col2:
    st.image(
        r"C:\Users\bpoort\OneDrive - onlineeportal\Desktop\web_app\images\Jemena_BrandMark_RGB_000.png"
    )

# ---------------------------
# Main Title
# ---------------------------
st.title("What is an Electricity Distribution Network?")

st.write(
    """
    An **electricity distribution network** is the portion of the power delivery system 
    that carries electricity from higher-voltage transmission lines to homes, businesses, 
    and other end users at a lower voltage level.
    """
)

# ---------------------------
# Transmission vs. Distribution Section
# ---------------------------
st.header("1. Transmission vs. Distribution")

# Two columns to compare Transmission and Distribution side-by-side
col1, col2 = st.columns(2)

with col1:
    st.subheader("Transmission")
    st.markdown("""
    - Transfers **high-voltage** electricity (typically tens or hundreds of kilovolts) over long distances.
    - Connects power plants (generation sources) to substations in populated or industrial areas.
    - Infrastructure: High-voltage transmission lines (often on tall towers), designed to move large quantities of electricity efficiently over distances.
    """)

with col2:
    st.subheader("Distribution")
    st.markdown("""
    - Steps down the high transmission voltage to lower voltages suitable for end users.
    - Delivers electricity from local substations directly to residential, commercial, and industrial customers.
    - Infrastructure: Usually consists of medium-voltage (e.g., 4 kV to 35 kV) and low-voltage lines (e.g., 120 V or 240 V for homes), often on street poles or underground in urban settings.
    """)

# ---------------------------
# Interactive Quiz / Elements
# ---------------------------
st.subheader("Test Your Understanding")

# 1. Checkbox-based question
st.write("**Q1: Which part of the grid handles the highest voltage?**")
if st.checkbox("Transmission"):
    st.success("Correct! Transmission lines handle the highest voltages.")
if st.checkbox("Distribution"):
    st.error("Distribution lines carry electricity at lower voltages to the end users.")

# 2. Buttons question
st.write("**Q2: Which segment of the network typically operates at 120 V or 240 V for homes?**")
answer_q2 = st.radio(
    "",
    ["Transmission Network", "Distribution Network"]
)
if answer_q2 == "Transmission Network":
    st.error("Not quite. Transmission lines operate at much higher voltages.")
elif answer_q2 == "Distribution Network":
    st.success("Correct! Distribution lines usually serve customers at these lower voltage levels.")

# 3. Slider to guess typical medium voltage range
st.write("**Q3: Guess the typical medium-voltage range (in kV) used in distribution.**")
medium_voltage_guess = st.slider("Select kV range", min_value=1, max_value=50, value=15)
if 4 <= medium_voltage_guess <= 35:
    st.success("You're correct! Medium-voltage lines are often between 4 kV and 35 kV.")
else:
    st.info("Typically, medium-voltage lines range from about 4 kV to 35 kV.")

# ---------------------------
# Conclusion / Thank You
# ---------------------------
st.write("---")
st.write("### Thank you for learning about Electricity Distribution Networks!")
st.write(
    """
    Feel free to explore more about how power is transmitted and distributed 
    to our homes, businesses, and industries. 
    """
)
