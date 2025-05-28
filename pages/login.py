import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.database import verify_login

st.set_page_config(page_title="Employee Management System - Login",page_icon="🔐")

st.title("Employee Management System")
st.subheader("Login")

with st.form("login_form"):
    emp_code = st.text_input("Employee code")
    password = st.text_input("Password", type="password")

    submit = st.form_submit_button("Login")

    if submit:
        if emp_code and password:
            success, message = verify_login(emp_code, password)

            if success:
                st.success(message)
                st.session_state['logged_in'] = True
                st.session_state['emp_code'] = emp_code
                st.switch_page("pages/dashboard.py")
            else:
                st.error(message)
        else:
            st.warning("Please enter both employee code and password.")            