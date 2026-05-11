"""
Problem 1
Create a class called Student.

Requirements:

__init__(self, name, age) should store name and age
Create a method introduce() that prints:
"My name is <name> and I am <age> years old."
Then:

create 2 student objects
call introduce() for both
"""

from re import S


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return print(f"My name is {self.name} and I am {self.age} years old.")


student1 = Student("Uzair", age=12)
student2 = Student(name="James", age=32)

student1.introduce()
student2.introduce()


"""
Problem 2
Create a class called Employee.

Requirements:

create a class attribute company with value "Google"
__init__(self, name, salary) should store name and salary
create a method show_details() that prints:
"<name> works at <company> and earns <salary>"

Then:

create 2 employee objects
call show_details() for both
Bonus
After that, print the company name using:

the class itself
one object

"""


class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"{self.name} works at {self.company} and earn {self.salary}.")


emp1 = Employee(name="uzair", salary=230)
print(Employee.company)
print(emp1.company)


"""

Create a class Bank.

Requirements:

class attribute: bank_name = "State Bank"

__init__(self, account_holder, balance) stores both values

instance method show_account() prints:
"<account_holder> has balance <balance> in <bank_name>"

class method change_bank_name(cls, new_name):
changes the class attribute bank_name

static method is_minimum_balance(balance):
returns True if balance is at least 1000, otherwise False

Then:

create 2 objects
call show_account() for both
change bank name using class method
call show_account() again to prove both objects see changed bank name
test static method with one value above 1000 and one below 1000
"""


class Bank:
    bank_name = "State Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def show_account(self):
        print(f"{self.account_holder} has balance {self.balance} in {self.bank_name}.")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def is_minimum_balance(balance):
        if balance >= 1000:
            return True
        return False


account1 = Bank("uzair", balance=2000)
account2 = Bank("james", balance=32000)

account1.show_account()
account2.show_account()

Bank.change_bank_name("Axis Bank")


account1.show_account()
account2.show_account()

print(Bank.is_minimum_balance(account1.balance))


"""
__str__ -> readable for users
__repr__ -> useful for developers/debugging
Problem 4
Create a class Book.

Requirements:

__init__(self, title, author, price)
__str__(self) should return:
"Book: <title> by <author>, Price: <price>"
__repr__(self) should return:
"Book('<title>', '<author>', <price>)"
Then:

create one object
print it using print(book1)
print its repr using print(repr(book1))
"""


class Book:
    def __init__(self, title, author, price) -> None:
        self.title = title
        self.author = author
        self.price = price

    def __str__(self) -> str:
        #
        return f"Book({self.title}, {self.author}, {self.price})"

    def __repr__(self) -> str:
        #
        return f"Book({self.title}, {self.author}, {self.price})"


book1 = Book(title="Harry Potter", author="uzair", price=100)
print(book1)
print(repr(book1))


"""
Problem 5
Create a parent class Person.

Requirements:

__init__(self, name, age)
method show_person() that prints:
Name: <name>, Age: <age>
Create a child class Teacher(Person).

Extra requirements for Teacher:

add subject
method show_teacher() that prints:
Name: <name>, Age: <age>, Subject: <subject>
Then:

create one Teacher object
call both:
show_person()
show_teacher()
Small hint:
Inside Teacher.__init__, use super().__init__(name, age)

Send your solution and I’ll review it like an examiner, then we’ll move to method overriding.
"""


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show_person(self):
        print(f"Name: <{self.name}>, Age: <{self.age}>")


class Teacher(Person):
    def __init__(self, name, age, subject) -> None:
        super().__init__(name, age)
        self.subject = subject

    def show_teacher(self):
        print(f"Name: <{self.name}>, Age: <{self.age}>, Subject: <{self.subject}>")


teacher1 = Teacher("Uzair", 23, subject="English")

teacher1.show_person()
teacher1.show_teacher()




'''

'''
