import mysql.connector

def main():

    # Connect to the employee_info database.
    connection = initialize_database()
    cursor = connection.cursor()

    choice = None
    while choice != "8":
        print()
        print("1) Display Employees")
        print("2) Insert Employee")
        print("3) Modify Employee")
        print("4) Delete Employee")
        print("5) Display Departments")
        print("6) Insert Department")
        print("7) Display Department Names and Employee Names")
        print("8) Quit")
        choice = input("> ")
        print()

        if choice == "1":
            # Display Employees.
            display_employees(cursor)
        
        elif choice == "2":
            # Add New Employee.
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            date_hired = input("Date Hired (YYYY-MM-DD): ")
            hourly_wage = input("Hourly Wage: $")
            display_departments(cursor)
            departments_id = input("Department ID: ")
            if not department_id_is_valid(cursor, departments_id):
                continue
            else:
                cursor.execute(f"INSERT INTO employees (first_name, last_name, date_hired, hourly_wage, departments_id) VALUES ('{first_name}', '{last_name}', '{date_hired}', '{hourly_wage}', '{departments_id}')")
                connection.commit()
        
        elif choice == "3":
            # Modify Employee.
            while choice != "6":
                display_employees(cursor)
                print("\nChoose a field to modify:")
                print("1) First Name")
                print("2) Last Name")
                print("3) Date Hired")
                print("4) Hourly Wage")
                print("5) Department ID")
                print("6) Back to Main Menu")
                choice = input("> ")

                if choice == "1":
                    field_to_alter = "first_name"
                elif choice == "2":
                    field_to_alter = "last_name"
                elif choice == "3":
                    field_to_alter = "date_hired"
                elif choice == "4":
                    field_to_alter = "hourly_wage"
                elif choice == "5":
                    field_to_alter = "departments_id"
                    display_departments(cursor)
                else:
                    break
                
                new_field = input(f"What would you set {field_to_alter} to? ")

                if (field_to_alter == "5" and not department_id_is_valid(cursor, new_field)):
                    continue
                else:
                    employee_first_name = input("What is the current first name of the employee you wish to modify? ")
                    employee_last_name = input("What is the current last name of the employee you wish to modify? ")

                    cursor.execute(f"UPDATE employees SET {field_to_alter} = '{new_field}' WHERE (first_name = '{employee_first_name}' AND last_name = '{employee_last_name}')")
                    connection.commit()
                    print(cursor.rowcount, "record(s) affected\n")
                    
                    if cursor.rowcount == 0:
                        print("Unable to process request: Invalid information entered.")
                        break
        
        elif choice == "4":
            # Delete Employee.
            display_employees(cursor)
            employee_first_name = input("\nWhat is the current first name of the employee you wish to delete? ")
            employee_last_name = input("What is the current last name of the employee you wish to delete? ")

            cursor.execute(f"DELETE FROM employees WHERE (first_name = '{employee_first_name}' AND last_name = '{employee_last_name}')")
            connection.commit()
            print(cursor.rowcount, "record(s) deleted\n")
            if cursor.rowcount == 0:
                print("Unable to process request: Invalid information entered.")
        
        elif choice == "5":
            # Display Departments.
            display_departments(cursor)
        
        elif choice == "6":
            # Add New Department.
            dept_name = input("Department Name: ")
            values = (dept_name)
            cursor.execute(f"INSERT INTO departments (dept_name) VALUES ('{dept_name}')")
            connection.commit()
            print(cursor.rowcount, "record inserted.")
        
        elif choice == "7":
            # Display Department Names and Employee Names.
            cursor.execute("SELECT departments.dept_name AS 'Department Name', \
            GROUP_CONCAT(DISTINCT CONCAT(' ', employees.first_name, ' ', employees.last_name)) \
            FROM departments \
            INNER JOIN employees ON departments.id = employees.departments_id \
            GROUP BY dept_name \
            ORDER BY departments.dept_name")

            record_list = []
            print("{:<25}  {:<25}".format("DEPARTMENT NAME", "EMPLOYEES"))
            for record in cursor.fetchall():
                record_list.append(record)
            for record in record_list:
                print("{:<25}  {:<25}".format(record[0], record[1]))

def initialize_database():

    # Connect to the MySQL server.
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="218028kk")

    cursor = connection.cursor()

    try:
        # Creates database.
        cursor.execute(f"CREATE DATABASE employee_info")
        
        new_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="218028kk",
                database="employee_info")
        
        cursor = new_connection.cursor()

        # Generates departments table.
        cursor.execute("CREATE TABLE departments (id INT AUTO_INCREMENT PRIMARY KEY, dept_name VARCHAR(45))")

        # Generates employees table.
        cursor.execute("CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(25), last_name VARCHAR(25), date_hired DATE, hourly_wage DECIMAL(5,2), departments_id INT, FOREIGN KEY (departments_id) REFERENCES departments(id))")

    except:
        new_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="218028kk",
                database="employee_info")
    
        cursor = new_connection.cursor()

    return new_connection

# Checks whether the departments_id is valid.
def department_id_is_valid(cursor, departments_id):
    
    departments_list = []
    cursor.execute("SELECT * FROM departments")
    for record in cursor.fetchall():
        departments_list.append(record[0])
    if int(departments_id) not in departments_list:
        print("Unable to process request: Invalid Department ID")
        return False
    else:
        return True

# Displays all fo the employees and their information.
def display_employees(cursor):

    cursor.execute("SELECT * FROM employees")
    print("{:<5}  {:<15}  {:<15} {:<15}  {:<15}  {:<15}".format("ID", "FIRST NAME", "LAST NAME", "DATE HIRED", "HOURLY WAGE", "DEPARTMENT ID"))
    for record in cursor.fetchall():
        print("{:<5}  {:<15}  {:<15} {:<15}  ${:<15}  {:<15}".format(record[0], record[1], record[2], record[3].strftime("%Y-%m-%d"), record[4], record[5]))

# Displays all fo the departments and their IDs.
def display_departments(cursor):

    cursor.execute("SELECT * FROM departments")
    print("{:<5}  {:<15}".format("ID", "DEPARTMENT NAME"))
    for record in cursor.fetchall():
        print("{:<5}  {:<15}".format(record[0], record[1]))

if __name__ == "__main__":
    main()
