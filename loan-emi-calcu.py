import streamlit as st
st.title("Calulate Loan EMI")
 
col1,col2,col3 =st.columns(3)

with col1:
    
    amt=st.slider("Loan Amount",100000,2500000,500000)
    rt=st.slider("Loan Amount",6,12,8)
    tr=st.slider("Tenure",1,8,5)

if st.button("Calculate Personal Loan EMI"):
    with col3:
        mt=rt/(12*100)
        tenure_months=tr*12
        emi=(amt*mt*(1+mt)**tenure_months)/((1+mt)**tenure_months-1)
        total_payment=emi*tenure_months
        total_int=total_payment-amt
        st.write("Total Payment :",round(total_payment,0))
        st.write("Total Intrest :",round(total_int,0))
        st.write("EMI:",round(emi,2))
        
