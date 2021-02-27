# Author: Paul Quaife
# Date: 2/23/2021
# Description: Creates a private database for Employees.

class Employee:
    """Employee Class"""
    def __init__(self, _emp_names, _emp_ids, _emp_salary, _emp_emails):
        """ init method creating private names, ids, salaries, and emails"""
        self.emp_names = _emp_names
        self.emp_ids = _emp_ids
        self.emp_salary = _emp_salary
        self.emp_emails = _emp_emails

    def get_name(self):
        """returns name"""
        return self._emp_names

    def get_ID_number(self):
        """returns ID number"""
        return self._emp_ids

    def get_salary(self):
        """returns salary"""
        return self._emp_salary

    def get_email_address(self):
        """returns email address"""
        return self._emp_emails


def make_employee_dict(_emp_names, _emp_ids, _emp_sals, _emp_emails):  # to make the list into employee object
    result = {}
    for i in range(len(_emp_names)):
        emp = Employee(_emp_names[i], _emp_ids[i], _emp_sals[i], _emp_emails[i])
        result[_emp_ids[i]] = emp
    return result
