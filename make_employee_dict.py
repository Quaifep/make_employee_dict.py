# Author: Paul Quaife
# Date: 2/23/2021
# Description: Creates a private database for Employees.

class Employee:
    """Employee Class"""
    def __init__(self, _name, _ids, _salary, _emails):
        """ init method creating private names, ids, salaries, and emails"""
        self._name = _name
        self._ids = _ids
        self._salary = _salary
        self._emails = _emails

    def get_name(self):
        """returns name"""
        return self._name

    def get_ID_number(self):
        """returns ID number"""
        return self._ids

    def get_salary(self):
        """returns salary"""
        return self._salary

    def get_email_address(self):
        """returns email address"""
        return self._emails


def make_employee_dict(_name, _ids, _salary, _emails):
    result = {}
    for i in range(len(_name)):
        emp = Employee(_name[i], _ids[i], _salary[i], _emails[i])
        result[_ids[i]] = emp
    return result
