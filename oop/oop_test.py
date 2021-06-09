class Employee:

    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def fullname(self):

        return f"'{self.first} {self.last}' "


    def apply_raise(self):
        self.pay = int(self.pay + Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount  = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str
        return cls(first, last, pay)


    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False

        else:
            return True


emp1 = Employee('corey', 'scholar', 5000)
emp2 = Employee('steve', 'anyah', 6000)
print(emp1.pay)
print(emp2.first) 
emp1.apply_raise()
print(Employee.raise_amount)
#print(Employee.__dict__)
print(emp1.fullname())


import datetime
my_date = datetime.date(2020, 2, 20)
print(Employee.is_weekday(my_date))


class Developer(Employee):
    raise_amount = 1.5

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def  remove_emp(self,emp):
        if emp in self.employees:
            self.employees.append(emp)  

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


dev1 = Developer('sammy', 'ejikeh', 30000, 'python')
dev2 = Developer('maje', 'Anyah', 70000, 'java')

mgr_1 = Manager('jimmy', 'Idu', 6000, [dev2])


print(dev1.email)
print(dev2.email)
#print(help(Developer))
print(dev2.pro_lang)
print(dev1.pro_lang)
print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(dev1)
print(isinstance(mgr_1, Employee))