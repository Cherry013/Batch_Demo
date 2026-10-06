def veg_menu():
    print("===== Veg Menu =====")
    print("Butter panner: 350")
    print("Pani puri: 30")
    print("mushroom Biryani: 280")
    print("Veg fried rice: 120\n")


def non_vegmenu():
    print("===== Non Veg Menu =====")
    print("Chicken Biryani: 270")
    print("Mutton Biryani: 300")
    print("Fish fry: 400")
    print("prawns Biryani: 500")
    print("Crab fry: 800\n")

def menu():
    veg_menu()
    non_vegmenu()

# menu()

def details(name,age=18,branch="CSE"):
    print(f"name : {name}")
    print(f"age : {age}")
    print(f"branch : {branch}")

# details("Teja", 21,branch="CSE")

def axis(x,y,z):
    print(f"x : {x}")
    print(f"y : {y}")
    print(f"z : {z}")

# axis(23,45,67)
# axis(z=47,y=67,x=66)


# def fun(*x):
#     # print(f"x : {x}")
#     print(*x) # print(24, 56, 67, 65, 4, 5, 6878)
#     # print(24, 56, 67, 65, 4, 5, 6878)
#     print(x)
#     axis(*x) # axis(24,56,67)
# fun(24,56,67)



def fun2(**k):
    print(f"k : {k}")
    axis(**k) # axis(x=50,y=20,z=30)
    # print(**k)

# fun2(x=50,y=20,z=30)
def total(*a):
    print(f"a : {a[1::2]}")
    print(f"total_sum : {sum(a[1::2])}")
    s = 0
    for i in a:
        s+=i
    print(f"total sum : {s}")

# total(1,2,3,4,56,89,90,90,45,78,89,67) # total_sum :



def fun(x,y):
    print(f"x : {x}")
    print(f"y : {y}")
    return x+y

# print(fun(33,44))
# k = fun(1,2)
# print(k**k)

def fun7(x,y):
    if x%2:
        return x+y
    else:
        return x*y
# print(fun7(3,4))
# l = fun7
# x = print
# x(l(4,8))
# print(l.__name__)
# print(l.__doc__)



def fun9(z:str,y:int) -> list:
    """Just a Function"""
    return [z,y]
#
# print(fun9.__doc__)
# print(fun9.__annotations__)
# print(fun9("z","y"))

# def guidelines(func):
#     # print("Just checking")
#     def inner(*args,**kwargs):
#         print("Rule 1: No copying")
#         print("Rule 2: No Ai")
#         print("Rule 3: Do your own work")
#         func(*args,**kwargs)
#     return inner
#
# @guidelines
# def exam(name):
#     print(f'Exam started {name} start writing')
# @guidelines
# def login(us,psd):
#     print(f"{us} login successful Start the exam")

# exam("Shivani")
# exam(name="trisha")
# login("Cherry","1234567890")

def upper(func):
    def inner(name):
        # st = func(name)
        # return st.upper()
        return func(name).upper()
    return inner
@upper
def greet(name):
    return f"Hello {name}"

# print(greet("Manohar"))
# print(greet("Sravani"))
# print(greet("Vinay"))
#
# users = {"manohar":"manohar-IAS", "sravani":"SI-sravani", "vinay":"HM-Vinay", "dinesh":"PM-dinesh"}
#
# def verification(func):
#     def inner():
#         un = input("Enter your Username: ")
#         p = input("Enter Your Password: ")
#         if un.lower() in users.keys():
#             if users[un.lower()] == p:
#                 func()
#             else:
#                 print("Invalid Credentials")
#         else:
#             print("Invalid Credentials")
#     return inner
#
# @verification
# def login():
#     print("Login Successful")
#
# login()

class Student:
    total = 0
    # print("Hello")
    def __init__(self,name,age,gender,cgpa,course):
        # print("__init__ function")
        self.name = name
        self.age = age
        self.gender = gender
        self.cgpa = cgpa
        self.course = course
        Student.total += 1
    College = "Malla Reddy"

    def display_details(self):
        print(f"name : {self.name}")
        print(f"age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"CGPA: {self.cgpa}")
        print(f"Course: {self.course}")

    def is_pass(self):
        if self.cgpa >= 5:
            return "Pass"
        return "Fail"
    def change_cgpa(self,n):
        self.cgpa = n


# print(Student.College)
s1 = Student("Prabhas",50,"Male",4.0,"Bahubali")
# print(s1.total)
s2 = Student("Ganesh YT", 35,"Male", 0.0,"Data Science")
# print(s2.total)
s3 = Student("Trisha",90, "Female", 9.05,"CSE")
# print(s3.total)
s4 = Student("Vaishnavi", 11,"Female", 8.0, "IT")
# s1.display_details()
# # Student.display_details(s1)
# s2.display_details()
# print(s1.is_pass())
# s1.change_cgpa(5.1)
# print(s1.is_pass())

class Bank:
    Bank_Name = "Axis"
    def __init__(self,name,accno):
        self.name = name
        self.accno = accno
        self.balance = 0
    @classmethod
    def change_bank(cls,new):
        cls.Bank_Name = new

    def display(self):
        print(f"Name: {self.name}")
        print(f"Account No: {self.accno}")
        print(f"Balance: {self.balance}")

    def deposite(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount
# print(Bank.Bank_Name)
# Bank.change_bank("DBS")
# print(Bank.Bank_Name)
# b1 = Bank("Dinesh",143143)
# b1.change_bank("HSBC")
# print(Bank.Bank_Name)
# b1.display()
# b1.deposite(100000000)
# b1.withdraw(100000)
# b1.display()

class Swiggy:
    offer = 0.2
    def __init__(self,un,order=[],one=False):
        self.username = un
        self.order = order
        self.one = one

    def display(self):
        print(f"UserName: {self.username}")
        print(f"Orders: {self.order}")
        print(f"Swiggy One: {self.one}")

    @classmethod
    def menu_display(cls):
        print("Chicken Biryani : 230$")
        print("Mutton Biryani : 350$")
        print("Prawns Biryani : 450$")
        print("Mushroom 65 : 300$")

    @classmethod
    def new_offer(cls,new):
        cls.offer = new

    def ordered(self,item_name):
        self.order.append(item_name)

    def order_history(self):
        print(self.order)

# s1 = Swiggy("vinay",["Mutton Biryani Family pack"],True)
# s1.order_history()
# s1.ordered("Cheese Pasta")
# s1.order_history()
# s1.display()
# print(Swiggy.offer)
# s1.new_offer(0.1)
# print(Swiggy.offer)

class Krishna:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            self.start += 1
            return self.start
        raise StopIteration
#
# k = Krishna(10,25)
# for i in k:
#     print(i)



class Prime:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            self.start += 1
            if self.is_prime(self.start):
                return self.start
            # else:
            #     return next(self)
        raise StopIteration

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
#
# a=Prime(1,50)
# for i in a:
#     print(i)


class User:
    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age

    def login(self):
        print("Login Successful")

    def logout(self):
        print("Logged out")

class Snap(User):
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# s1 = Snap('Harsha',22)
# s1.display()
# print(Snap.mro())
# print(Snap.__mro__)


class RBI(User):
    pass
class HDFC(RBI):
    def m1(self):
        print("HDFC Class")
# r1 = RBI('Dinesh',26)
# r1.m1()
# print(HDFC.mro())
# print(RBI.mro())

class Messanger:
    pass

class Payments:
    pass

class Whatsapp(User, Messanger, Payments):
    pass


# print(Whatsapp.mro())
# print(Messanger.mro())
# print(Payments.mro())



# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class E:
#     pass
# class D(B,C,E):
#     pass


# print(D.mro())