# Author: Paul Quaife
# Date: 2/23/2021
# Description: Creates a private database for Employees.

class Employee:
    """Employee Class"""
    def __init__(self, emp_names, emp_ids, emp_salary, emp_emails):
        """ init method creating private names, ids, salaries, and emails"""
        self.emp_names = emp_names
        self.emp_ids = emp_ids
        self.emp_salary = emp_salary
        self.emp_emails = emp_emails

    def get_name(self):
        """returns name"""
        return self.emp_names

    def get_ID_number(self):
        """returns ID number"""
        return self.emp_ids

    def get_salary(self):
        """returns salary"""
        return self.emp_salary

    def get_email_address(self):
        """returns email address"""
        return self.emp_emails


def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):  # to make the list into employee object
    result = {}
    for i in range(len(emp_names)):
        emp = Employee(emp_names[i], emp_ids[i], emp_sals[i], emp_emails[i])
        result[emp_ids[i]] = emp
    return result
