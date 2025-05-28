import streamlit as st
from utils.database import get_all_employees

st.set_page_config(page_title="Employee Management System - Dashboard",page_icon="🔐")

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("Please login first!")
    st.stop()

st.title("Employee Dashboard")
st.subheader("Employee List")

employees = get_all_employees()

if employees:
    st.dataframe(
        employees,
        column_config={
            "employee_code": "Employee Code",
            "name": "Name",
            "designation":"Department",
        },
        hide_index=True
    )
else:
    st.info("No employees found in the database.")

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("pages/login.py")        