
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
Exercise 1: BookShelf

Create a class called BookShelf.

It should store a list of books.

Add:

__len__
__getitem__
__contains__
'''


class BookShelf:
    def __init__(self,books):
        self.books=books

    def __len__(self):
        return len(self.books)

    def __getitem__(self,index):
        return self.books[index]

    def __contains__(self, item):
        return item in self.books


shelf = BookShelf(["Python Basics", "Django Intro", "OOP Mastery"])

print(len(shelf))
print(shelf[0])
print("Django Intro" in shelf)
print("Java Basics" in shelf)



class Playlist:
    def __init__(self,playlists):
        self.playlists=playlists

    def __len__(self):
        return len(self.playlists)

    def __getitem__(self, index):
        return self.playlists[index]

    def __contains__(self, item):
        return item in self.playlists









playlist = Playlist(["Song A", "Song B", "Song C"])

print(len(playlist))
print(playlist[2])
print("Song B" in playlist)







class StudentGroup:
    def __init__(self,students):
        self.students=students

    def __len__(self):
        return len(self.students)

    def __getitem__(self,index):
        return self.students[index]

    def __contains__(self, item):
        return item in self.students

group = StudentGroup(["Ali", "Sara", "John", "Zara"])

print(len(group))
print(group[1])
print(group[0:2])
print("John" in group)




class BaseView:
    def dispatch(self):
        self.setup()
        self.handle()
        self.finish()

    def setup(self):
        print("Preparing request")

    def handle(self):
        raise NotImplementedError(
            "Child class must define handle()"
        )
    def finish(self):
        print("Sending response")


class HomeView(BaseView):
    def handle(self):
        print("Showing homepage")
view = HomeView()
view.dispatch()
view.handle()




class BaseForm:
    def process(self):
        self.validate()
        self.save()

    def validate(self):
        raise NotImplementedError('Must be implemented by the child class validate()')
    def save(self):
          raise NotImplementedError('Must be implemented by the child class save()')

class UserForm(BaseForm):
    def validate(self):
        print("Validating user data")

    def save(self):
        print("Saving user data")

form = UserForm()
form.process()



class BaseReport:
    def generate(self):
        print("Generating base report")


class SalesReport(BaseReport):
    def generate(self):
        print("Preparing sales data")
        super().generate()
        print("Sales report ready")

report = SalesReport()
report.generate()


class ArticleView:
    model="Article"
    template_name = "article_detail.html"

    def __init__(self,article_id):
        self.article_id=article_id

    def show(self):
        print(
            f'Model: {self.model}'
        )
        print(
            f'Template: {self.template_name}'
        )
        print(
            f'Article ID: {self.article_id}'
        )


view = ArticleView(101)
view.show()



class PublishedPostView:
    def get_queryset(self):
        posts = [
            {"title": "Python Classes", "published": True},
            {"title": "Django Draft", "published": False},
            {"title": "Django CBV", "published": True},
        ]
        return [post for post in posts if post['published']]
    def show(self):
        posts = self.get_queryset()
        for post in posts:
            print(post['title'])

c= PublishedPostView()
c.show()

class CoursePageView:
    def get_queryset(self):
        return ["Python", "Django", "REST API"]


    def get_context_data(self,**kwargs):
        return {
            "page_title":"Course",
            "total_courses":len(self.get_queryset())
        }
    def show(self):
        context = self.get_context_data()
        return context


context=CoursePageView()
context=context.get_context_data()
print(context["page_title"])
print(context["total_courses"])


class UserSerializer:
    pass

class BaseAPIView:
    serializer_class=None
    def get_serializer_class(self):
        return self.serializer_class
    def show_serializer(self):
        serializer = self.get_serializer_class()
        print(serializer.__name__)



class UserListAPIView(BaseAPIView):
    serializer_class=UserSerializer

test = UserListAPIView()
test.show_serializer()





class ProductListSerializer:
    pass

class ProductDetailSerializer:
    pass


class ModelViewSet:
    pass


class ProductViewSet(ModelViewSet):
    action = "list"
    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        return ProductDetailSerializer



view = ProductViewSet()

print(view.get_serializer_class().__name__)

view.action = "retrieve"

print(view.get_serializer_class().__name__)














class IsAuthenticated:
    def has_permission(self,user):
        return user is not None

class BaseAPIView:
    permission_classes =[]

    def get_permissions(self):
        return [
          permission()  for permission in self.permissions
        ]

    def check_permission(self,user):
        for permission in self.get_permissions():
            if not permission.has_permission(user):
                return False
            return True









#
