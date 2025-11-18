import streamlit as st
from PIL import Image
import base64

# --------------------------------------------
# Background Image Function
# --------------------------------------------
def add_bg(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .card {{
            padding: 25px;
            background: rgba(100, 134, 234, 0.85);
            border-radius: 20px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        }}

        .title-card {{
            padding: 10px;
            background: rgba(111, 222, 123, 0.7);
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
add_bg("bg.jpg")

# --------------------------------------------
# Title Section
# --------------------------------------------
col_img, col_title = st.columns([1, 5])

with col_img:
    st.image("loan.png", width=80)

with col_title:
    st.markdown("<div class='title-card'>", unsafe_allow_html=True)
    st.title("💰Loan EMI Calculator")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("### Adjust the values to calculate your EMI.")

# --------------------------------------------
# Two Main Columns Layout
# --------------------------------------------
left, right = st.columns(2)

# --------------------------------------------
# LEFT COLUMN → Input Fields
# --------------------------------------------
with left:
    st.subheader("📥 Loan Details")

    amt = st.slider("Loan Amount (₹)", 100000, 2500000, 500000)
    rt = st.slider("Annual Interest Rate (%)", 6, 20, 8)
    tr = st.slider("Tenure (Years)", 1, 15, 5)

    calculate = st.button("🔍 Calculate EMI")

# --------------------------------------------
# RIGHT COLUMN → Result Card
# --------------------------------------------
with right:
    if calculate:
        monthly_rate = rt / (12 * 100)
        tenure_months = tr * 12

        emi = (amt * monthly_rate * (1 + monthly_rate) ** tenure_months) / (
                (1 + monthly_rate) ** tenure_months - 1
        )

        total_payment = emi * tenure_months
        total_interest = total_payment - amt

        st.markdown("### 📊 EMI Summary")
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.write(f"**💵 Loan Amount:** ₹ {amt:,.0f}")
        st.write(f"**📅 Monthly EMI:** ₹ {emi:,.2f}")
        st.write(f"**📈 Total Interest:** ₹ {total_interest:,.0f}")
        st.write(f"**🏦 Total Payment:** ₹ {total_payment:,.0f}")

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: center; padding: 20px; margin-top: 40px;
                color: white; font-size: 16px; background: rgba(0,0,0,0.4);
                border-radius: 10px;'>
        © 2025 <b>Manoj C. Narware</b>. All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True
)