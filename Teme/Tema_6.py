# # Ex . 1
#
# PI = 3.14
# class circle:
#     range = None
#     color = None
#
#     def __init__(self, range, color):
#         self.range = range
#         self.color = color
#
#     def describe_circle(self):
#         print(self.range)
#         print(self.color)
#
#     def area_cirlce(self):
#         area = PI * circle.range
#         format_area = "{:.2f}".format(area)
#         return format_area
#
#     def diameter(self):
#         diameter = 2 * circle.range
#         return diameter
#
#     def circumference(self):
#         circumference = 2 * PI * circle.range
#         format_circumference = "{:.2f}".format(circumference)
#         return format_circumference
#
#
# circle = circle(27, 'green')
# circle.describe_circle()
# print(f'Area of circle is : {circle.area_cirlce()}')
# print(f'Diameter of circle is : {circle.diameter()}')
# print(f'Circumference of circle is : {circle.circumference()}')
#
# #EX 2
#
# class rectangle:
#     lenght=None
#     width=None
#     color=None
#
#
#     def __int__(self,lenght,width,color):
#         self.lenght=lenght
#         self.width=width
#         self.color
#
#
#     def describe_rectangle(self):
#         print(self.lenght)
#         print(self.width)
#         print(self.color)
#
#
#     def area_rectangle(self):
#       area=rectangle.width*rectangle.lenght
#       return area
#
#     def perimeter(self):
#         perimeter = 2 * (rectangle.length + rectangle.width)
#         return perimeter
#
#     def change_color(self):
#         rectangle.color='Blue'
#
#
# rectangle = rectangle(20, 10, 'yellow')
# rectangle.describe()
# print(f'Area of rectangle is : {rectangle.area_rectangle()}')
# print(f'Perimeter of rectangle is : {rectangle.perimeter()}')
# rectangle.change_color()
# rectangle.describe()
#

#  # Ex. 3
#
# class employee:
#     first_name = None
#     last_name = None
#     salary = None
#
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#
#     def describe(self):
#         print(f'The first name of employee is : {employee.first_name}.')
#         print(f'The last name of employee is : {employee.last_name}.')
#         print(f'The salary of employee is : {employee.salary} ron.')
#
#     def complet_name(self):
#         print(f'The complete name of employee it is : {employee.first_name +" " + employee.last_name}.')
#
#     def monthly_salary(self):
#         print(f'The monthly salary is : {employee.salary} ron.')
#
#     def annual_salary(self):
#         annual_salary = 12 * employee.salary
#         print(f'The annual salary is : {annual_salary} ron.')
#
#     def salary_increase(self):
#         salary_increase = employee.salary / 5000 / 10
#         # salary_increase = salary_increase * 100
#         salary_increase = "{:.1%}".format(salary_increase)
#         print(f'The salary_raise is {salary_increase}')
#
#
# employee = employee('Marius-Alexandru', 'Tahis', 5000)
# employee.describe()
# employee.complet_name()
# employee.monthly_salary()
# employee.annual_salary()
# employee.salary_increase()


# # Ex. 4
#
# class account:
#     iban = None
#     account_holder = None
#     balance = None
#
#     def __init__(self, iban, account_holder, balance):
#         self.iban = iban
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def balance_display(self):
#         print(f'Account holder, {account.account_holder} has in the account,'
#               f' {account.iban} amount of {account.balance} ron.')
#
#     def account_debit(self):
#         debit = 597
#         print(f'The bank account was debited with the amount of {debit} ron.')
#
#     def account_credit(self):
#         credit = 100000
#         print(f'The bank account was credited with amount of {credit} ron.')
#
#
# account = account('RO19710256789AA133A2', 'Tahis Marius-Alexandru', 25000)
# account.balance_display()
# account.account_debit()
# account.account_credit()


