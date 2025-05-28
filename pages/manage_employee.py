import streamlit as st 
from utils.database import get_all_employees, add_employee, update_employee, delete_employee

st.set_page_config(page_title="Employee Management System - Manage Employees",page_icon="👥")

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("Please login first!")
    st.stop()

st.title("Manage Employees")

tab1, tab2, tab3 = st.tabs(["Add Employee", "Edit Employee", "Delete Employee"])

with tab1:
    st.subheader("Add New Employee")
    with st.form("add_employee_form"):
        emp_code = st.text_input("Employee Code")
        name = st.text_input("Full Name")
        password = st.text_input("Password", type="password")
        department = st.selectbox(
            "Department",
            ["IT", "HR", "Finance", "Marketing", "Operations"]
        )

        submit = st.form_submit_button("Add Employee")

        if submit:
            if emp_code and name and password and department:
                success, message = add_employee(emp_code, name, password, department)
                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.warning("Please fill in all fields.")

with tab2:
    st.subheader("Edit Employee")                
    employees = get_all_employees()

    if employees:
        employee_options = {f"{emp['employee_code']} - {emp['name']}": emp for emp in employees}
        selected_employee_key = st.selectbox(
            "Select Employee to Edit",
            options=list(employee_options.keys())
        )

        if selected_employee_key:
            employee = employee_options[selected_employee_key]

            with st.form("edit_form"):
                name = st.text_input("Name", value=employee['name'])
                password = st.text_input("Password", type="password", value=employee['password'])
                designation = st.text_input("Designation", value=employee['designation'])

                submit = st.form_submit_button("Update Employee")

                if submit:
                    if name and password and designation:
                        success, message = update_employee(employee['employee_code'], name, password, designation)
                        if success:
                            st.success(message)
                            st.rerun()
                        else:
                            st.error(message)
                    else:
                        st.warning("Please fill in all fields.")
    else:
        st.info("No employees found in the database.")

with tab3:
    st.subheader("Delete Employee")
    if employees:
        employee_options = {f"{emp['employee_code']} - {emp['name']}": emp for emp in employees}
        selected_employee_key = st.selectbox(
            "Select Employee to Delete",
            options=list(employee_options.keys())
        )                                        

        if selected_employee_key:
            employee = employee_options[selected_employee_key]
             
            if st.button("Delete Selected Employee"):
                if st.session_state['emp_code'] == employee['employee_code']:
                    st.error("You cannot delete your own account!")
                else:
                    success, message = delete_employee(employee['employee_code'])
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
    else:
        st.info("No employees found in the database.")

if st.button("Back to Dashboard"):
    st.switch_page("pages/dashboard.py")        
