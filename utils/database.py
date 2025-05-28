import mysql.connector

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='12345678',
            database='user'
        )
        return connection
    except:
        print("Could not connect to databse")
        return None
    
def verify_login(emp_code,password):
    conn = get_db_connection()
    if not conn:
        return False,"Database connection failed"
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT employee_code, password FROM user.test WHERE employee_code = %s",(emp_code,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result is None:
            return False, "Employee not found"
        elif emp_code == result[0] and password == result[1]:
            return True, "Login Successful"
        else:
            return False, "Wrong password"
    except:
        return False, "Error checking login"

def get_all_employees():
    conn = get_db_connection() 
    if not conn:
        return []

    try:
        cursor = conn.cursor(dictionary=True) 
        cursor.execute("SELECT * FROM user.test")
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return employees
    except:
        return []
    
def add_employee(emp_code, name, password, department):
    conn = get_db_connection()
    if not conn:
        return False, "Database connection failed"

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO user.test(employee_code, name, password, designation) VALUES (%s, %s, %s, %s)",
            (emp_code, name, password, department)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True, "Employee added successfully"
    except:
        return False, "Error adding employee"  
    
def update_employee(emp_code, name, password, designation):
    conn = get_db_connection()
    if not conn:
        return False, "Database connection failed"
    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE user.test SET name = %s, password = %s, designation = %s WHERE employee_code = %s",
            (name, password, designation, emp_code)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True, "Employee updated successfully"
    except:
        return False, "Error updating employee"

def delete_employee(emp_code):
    conn = get_db_connection()
    if not conn:
        return False, "Database connection failed"
    
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user.test WHERE employee_code = %s", (emp_code,))
        conn.commit()
        cursor.close()
        conn.close()
        return True, "Employee deleted successfully"
    except:
        return False, "Error deleting employee"

