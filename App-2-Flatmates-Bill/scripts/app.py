import streamlit as st
from flat import Bill,Flatmate
from bill_pdf import Pdfreport
import os
import base64
from pathlib import Path

st.title('Flatmate Bill Calculator')

# Get the Bill Amount and period
bill_amount = st.number_input('Enter the Bill Amount : ')
period = st.text_input('Enter the Month and Year : ')

the_bill = Bill(bill_amount, period)

# Get the Number of Days
f1_no_of_days = st.number_input('Enter the Number of days Arvind has stayed: ')
f2_no_of_days = st.number_input('Enter the Number of days Roshini has stayed: ')

# Initialize Flatmates
arvind = Flatmate("Arvind", f1_no_of_days)
roshini = Flatmate("Roshini", f2_no_of_days)

# Calculate  the amount
arvind_amount = arvind.pay_bill(the_bill, roshini)
roshini_amount = roshini.pay_bill(the_bill, arvind)

if st.button("Calculate"):

    st.write('Arvind Pays : ', arvind_amount)
    st.write('Roshini Pays : ', roshini_amount)



    pdf_path = os.path.join(os.path.dirname(__file__), '..', 'files', 'bill_generator.pdf')
    Pdfreport(pdf_path).generate_pdf(arvind, roshini, the_bill)

    st.title('Bill PDF')

    with open(pdf_path,'rb') as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)












