# Author: Paul Quaife
# Date: 2/23/2021
# Description: Creates a private database for Employees.

class Employee:
    """Employee Class"""
    def __init__(self, _name, _ID_number, _salary, _email_address):
        """ init method creating private names, ids, salaries, and emails"""
        self._name = _name
        self._ID_number = _ID_number
        self._salary = _salary
        self._email_address = _email_address

    def get_name(self):
        """returns name"""
        return self._name

    def get_ID_number(self):
        """returns ID number"""
        return self._ID_number

    def get_salary(self):
        """returns salary"""
        return self._salary

    def get_email_address(self):
        """returns email address"""
        return self._email_address


def make_employee_dict(_name, _ID_number, _salary, _email_address):
    result = {}
    for i in range(len(_name)):
        emp = Employee(_name[i], _ID_number[i], _salary[i], _email_address[i])
        result[_ID_number[i]] = emp
    return result
