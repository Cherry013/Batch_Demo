def adding(x:str,y:str) -> str:
    return x+y

# list, tuple, str, dict, int, float, bool

# print(adding("asd","asd"))
# print(adding.__annotations__)

def add(x,y):
    return x+y
# print(add.__name__)
# print(add)

# a = add
# print(add(10,20))
# print(a(10,20))

def fun4():
    def fun5():
        print("Hello")
    return fun5

# fun = fun4() # fun = fun5
# fun()

def fun6():
    def inner(name):
        print(f"Hello {name}")
    return inner
#
# l = fun6()
# l("Prabhas")


def dec(x):
    def inner(y):
        print(x+y)
        return y
    return inner

# k = dec(50)
# print(k(30))
# print(k.__closure__)
# print(k.__closure__[0].cell_contents)
# k.__closure__[0].cell_contents = 100
# print(k.__closure__[0].cell_contents)
# print(k(30))


def validation(func):
    def inner(*args):
        # print(args)
        # l = []
        # for i in args:
        #     if isinstance(i,int):
        #         l.append(i)
        # l = tuple(l)

        l = tuple(filter(lambda x: isinstance(x,int),args))
        return func(*l)

    return inner

@validation
def just(*args):
    print(f"args: {args}")
    return sum(args)

# print(just(1,2,3,'66',[45],123,'78'))

def password_validator(func):
    def inner(psd:str):
        sp = ['@','*','!','#','$','%','&','_','-','=','+','/']
        if len(psd)>=8:
            up = list(filter(lambda x: x.isupper(),psd))
            sc = list(filter(lambda x:x in sp, psd))
            dg = list(filter(lambda x: x.isdigit(),psd))

            print(up,sc,dg,sep='\n')

            if up and sc and dg:
                print("Strong Password")
                func(psd)
            else:
                print("Weak Password")
        else:
            print("password must contain 8 characters")
    return inner

@password_validator
def password(ps):
    print(f"password {ps} is accepted")

#
# password("23456fghbnkH")
# password("765FHGDk#$")


# def register(func):
#     uns = []
#     def inner(us,psd,age):
#         nonlocal uns
#         if us not in uns:
#             sp = ['@', '*', '!', '#', '$', '%', '&', '_', '-', '=', '+', '/']
#             if len(psd) >= 8:
#                 up = list(filter(lambda x: x.isupper(), psd))
#                 sc = list(filter(lambda x: x in sp, psd))
#                 dg = list(filter(lambda x: x.isdigit(), psd))
#
#                 print(up, sc, dg, sep='\n')
#
#                 if up and sc and dg:
#                     print("Strong Password")
#                     if age >= 18:
#                         func(us,psd,age)
#                         uns.append(us)
#                     else:
#                         print("Age must be >= 18")
#                 else:
#                     print("Weak Password")
#             else:
#                 print("password must contain 8 characters")
#         else:
#             print("Username already exists")
#     return inner

# @register
# def registration(us,psd,age):
#     print(f"{us}'s Registration Successful")

# registration("cherry","CG4576#@$",19)
# registration("cherry","CG4576#@$",19)


import functools

def Dec(func):
    @functools.wraps(func)
    def inner(x,y):
        return func(x,y)
    return inner

@Dec
def ann(x:str,y:str) -> list:
    """Just a doc"""
    print(x+y)
    return [x,y]
#
# print(ann.__name__)
# print(ann.__doc__)
# print(ann.__annotations__)


class Student:
    def __init__(self,i,n,m):
        self.Id = i
        self.name = n
        self.marks = m
    def __gt__(self, other):
        return self.marks > other.marks
    def __lt__(self, other):
        return self.marks < other.marks
    def __eq__(self, other):
        return self.marks == other.marks
    # def __hash__(self):
    #     return hash(self.Id)
    def __repr__(self):
        return f"{self.Id} : {self.name}"
# s1 = Student(25,"Sai",100)
# s2 = Student(30,"Sai",100)
# s3 = Student(1,"Mahesh",100)
# print(s1)
# s = {s1,s2,s3}
# print(s)

from random import randint
# print(randint(1,25))
# list()
# l = ["Hii", "Byee", 6, 7, 8]
# it = iter(l)
# p = l.__iter__()
# print(f"it: {it}\np: {p}")
# print(next(it))
# print(p.__next__())
# print(it.__next__())
# print(next(it))
# print(it.__next__())
# print(next(it))
# for i in l:
#     print(i)

class A:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.end:
            self.start += 1
            return self.start-1
        else:
            raise StopIteration

# a1 = A(1,3)
# k = iter(a1)
# print(k,a1,sep="\n")
# a1.__iter__()
# A.__iter__(a1)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# for i in a1:
#     # if i is None:
#     #     break
#     print(i)


class Even:
    def __init__(self,l):
        self.l = l
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.l):
            self.index += 1
            if self.l[self.index-1]%2 == 0:
                return self.l[self.index-1]
        else:
            raise StopIteration
# obj = Even([1,2,4,909,78,55,3,23,80])
# for i in obj:
#     print(i)
def greet(name):
    print(f"Hello {name}")

# greet("Shivani")
# greet.__call__("Harshitha")
#
# class Student:
#     def __init__(self,name,sec,marks):
#         self.name = name
#         self.sec = sec
#         self.marks = marks
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Section: {self.sec}")
#         print(f"Marks: {self.marks}")
#     def __call__(self):
#         print("Called by object")
#         self.display()
#
#
# s1 = Student("Usha",'A',99.99)
# s1()


# gen = (x*x for x in range(11))
# even = [f"{i} even" for i in range(10) if i%2==0]
# even_odd = [f"{i} even" if i%2==0 else f"{i} odd" for i in range(10)]
# l = {i for i in range(11)}
# j = {chr(64+i):i for i in range(1,25)}
# print(even,even_odd,sep="\n")
# print(l)
# print(j)
# for i in gen:
#     print(i)




#
# l = []
# for i in range(10):
#     l.append(i)
#
# result = [i*i for i in range(10)]
# print(result)
#
# even = [f"{i} even" for i in result if i%2==0]
# even_odd = [f"{i} odd" if i%2 else f"{i} even" for i in result]
# print(even,even_odd,sep="\n")
# s = {i for i in range(10)}
# print(s)
# di = {i:chr(i) for i in range(10)}
# print(di)
#
# def is_prime(n):
#     for i in range(2,(n//2)+1):
#         if n%i==0:
#             return False
#     return True
#
# prime_numbers = [i for i in range(2,100) if is_prime(i)]
# numbers = {i:"prime" if is_prime(i) else "composite" for i in range(2,10)}
# print(prime_numbers,numbers,sep="\n")
# t = tuple(i for i in range(10))
# print(t)
# gen = (i for i in range(11) if i%2==0)
# print(type(t),type(prime_numbers),type(numbers),type(s),type(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# from random import randint
# l = [chr(i) for i in range(65,75)]
# marks = [randint(25,100) for i in range(10)]
#
# for i,j in zip(l,marks):
#     print(f"{i} : {j}")
# stu = {i:"Pass" if j >35 else "Fail" for i,j in zip(l,marks)}
# print(stu)

#
# class A:
#     Y = 100
#     def m1(self):
#         print('A Class')
#
# class B(A):
#     Y = 200
#     def m1(self):
#         print("B class")
#         super().m1()
#         print(super().Y)
#
# class C(B):
#     def m1(self):
#         print("C class")
#         super().m1()
#         print(super().Y)


# b1 = B()
# b1.m1()
# C().m1()


# class A:
#     def m1(self):
#         print('A Class')
#         super().m1()
#
# class B(A):
#     def m1(self):
#         print('B Class')
#         super().m1()
#
# class C(A):
#     def m1(self):
#         print('C Class')
#         super().m1()
# class E:
#     def m1(self):
#         print('E Class')
#
# class D(B,C,E):
#     def m1(self):
#         print('D Class')
#         super().m1()
# print(D.mro())
# D().m1()
# print(C.mro())
# C().m1()

class B:
    def m1(self):
        print('B Class',end=" ")
        super().m1()

class C:
    def m1(self):
        print('C Class')

class D(B,C):
    def m1(self):
        print('D Class',end=" ")
        super().m1()

# print(D.__mro__)
# D().m1()
# print(B.mro())
# B().m1()



# def fun():
#     print(a)
#     a=100
#
# fun()


# from abc import ABC, abstractmethod

# class A(ABC):
#     @classmethod
#     @abstractmethod
#     def m1(cls):
#         pass
# print(A.__dict__)
# class B(A):
#     pass
# b1 = B()



class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __getattr__(self, item):
        return f"{item} Not found"
    #
    # def __getattribute__(self,name):
    #     print(f"{name} is accessing")
    #     # self.x
    #     return super().__getattribute__(name)
    #     # return object.__getattribute__(self, name)

    def m1(self):
        print(self.x,self.y,sep="@")

# object
# a1 = A(10,25)
# print(a1.z)
# a1.m1()
# A.m1(a1)
# a1.__dict__['z'] = 100
# print(a1.z)


# class Bank:
#     def __init__(self,ac,bal):
#         self.account_holder = ac
#         self.balance = bal
#
#     def deposit(self,amount):
#         if amount >= 0:
#             self.balance += amount
#     def withdraw(self,amount):
#         if 0<= amount <= self.balance:
#             self.balance -= amount
#
#     def __str__(self):
#         return f"{self.account_holder} : {self.balance}"
#
#     def __add__(self, other):
#         return self.balance + other.balance
#
#     def __sub__(self, other):
#         return self.balance - other.balance
#
#     def __eq__(self, other):
#         return self.balance == other.balance
#
#     def __lt__(self, other):
#         return self.balance < other.balance
#
#     def __getattribute__(self, name):
#         print(f"{name} is accessing")
#         return super().__getattribute__(name)
#
#     def __setattr__(self, name, value):
#         if name == "balance":
#             if value >= 0:
#                 super().__setattr__(name,value)
#         else:
#             super().__setattr__(name,value)
class B:
    def __init__(self,x,y):
        self.x = x
        self.y = y

b1 = B(1,2)
# print(b1.)


class A:
    def __init__(self,x,y):
        self._x = x
        self.__y = y

    def get_x(self):
        return self._x
    def set_x(self,x):
        self._x = x

    def get_y(self):
        return self.__y
    def set_y(self,y):
        self.__y = y
# a1 = A(1,2)
# # print(a1._A__y)
# a1.set_x(50)
# print(a1.get_x())




class Hell:
    def __init__(self,name,age):
        self._name = name
        self.__age = age

    @property
    def n(self):
        return self._name
    @property
    def a(self):
        return self.__age
    @a.setter
    def a(self,n):
        self.__age = n
    @n.setter
    def n(self,n):
        self._name = n

# h = Hell("Santosh",0.5)
# print(h.n,h.a)
# h.a = 100
# print(h.a)
# # h.get_a = 75
# # print(h.get_a)


# class Bank:
#     def __init__(self,name,account,pin):
#         self.name = name
#         self._account = account
#         self.__pin = pin
#         self.__balance = 0
#
#     @property
#     def balance(self):
#         pin = int(input("Enter PIN: "))
#         if pin == self.pin:
#             return self.__balance
#         return None
#     @balance.setter
#     def balance(self,b):
#         self.__balance = b
#
#     @property
#     def account(self):
#         return self._account
#     @property
#     def pin(self):
#         return self.__pin
#
# b1 = Bank("Nandhini",3456789,3456)
# b1.balance = 25
# print(b1.balance)


class Employee:
    def __init__(self,sal):
        self.__salary = sal
        self.logs = []

    @property
    def sal(self):
        self.logs.append("Attempted")
        return self.__salary

    @sal.setter
    def sal(self,ns):
        if self.__salary < ns:
            self.__salary = ns

class Product:
    def __init__(self,p,dis):
        self._price = p
        self._discount = dis

    @property
    def cost(self):
        return self._price

    @cost.setter
    def cost(self,nc):
        if nc > 0:
            self._price = nc

    @property
    def offer(self):
        return self._discount

    @offer.setter
    def offer(self,no):
        if 0 <= no <= 0.7:
            self._discount = no

    def __final_cost(self):
        fc = self.cost * (1-self.offer)
        return fc

    @property
    def final_price(self):
        return self.__final_cost()
#
# p1 = Product(1500,0.2)
# print(p1.final_price)

class Character:
    def __init__(self,health):
        self.max_limit = self.__health = health

    @property
    def hp(self):
        return self.__health

    def damage(self,points):
        dm = self.__health - points
        if dm >= 0:
            self.__health -= points
        else:
            self.__health = 0

    def heal(self,points):
        h = self.__health + points
        if h <= self.max_limit:
            self.__health += points
        else:
            self.__health = self.max_limit


# ch = Character(200)
# ch.damage(170)
# ch.heal(50)
# print(ch.hp)
# ch.damage(100)
# print(ch.hp)
# ch.heal(250)
# print(ch.hp)

class Engine:
    def __init__(self):
        self.__temperature = 25.0

    @property
    def temp(self):
        return self.__temperature

    @temp.setter
    def temp(self,nt):
        if 0 <= nt <= 100:
            self.__temperature = nt
        else:
            self.__temperature = 100.0

#
# class Car:
#     def __init__(self):
#         self.__engine = Engine()
#         self.start = False
#
#     def display(self):
#         print(f"car {'start' if self.start else 'off'}")
#         print(f"Engine temperature : {self.__engine.temp} C")
#
#     def start_car(self):
#         if not self.start:
#             self.start = True
#             self.__engine.temp += 50
#         self.display()
#
#     def stop_car(self):
#         if self.start:
#             self.start = False
#             self.__engine.temp -= 20
#         self.display()
#
#     def cool_engine(self):
#         self.__engine.temp -= 30
#         self.display()
#
# c1 = Car()
# c1.start_car()
# c1.cool_engine()
# c1.stop_car()



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def area(self):
        r = int(input("r: "))
        print((22/7)*r*r)

    def perimeter(self):
        r = int(input("r: "))
        print(2*(22/7)*r)

class Rectangle(Shape):
    def area(self):
        l,b = int(input("l: ")), int(input("b: "))
        print(l*b)

    def perimeter(self):
        l, b = int(input("l: ")), int(input("b: "))
        print(2*(l+b))

class Triangle(Shape):
    def area(self):
        b,h = int(input("b: ")), int(input("h: "))
        print((1/2)*b*h)

    def perimeter(self):
        b, h = int(input("b: ")), int(input("h: "))
        print(b*h)

# c1 = Circle()
# r1 = Rectangle()
# t1 = Triangle()


class PaymentGateway(ABC):

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class UPIPayment(PaymentGateway):
    def authenticate(self):
        print("Authentication successful in UPI")

    def pay(self, amount):
        print(f"{amount} paid using UPI")

    def refund(self, amount):
        print(f"{amount} refunded to ur UPI account")

class CardPayment(PaymentGateway):
    def authenticate(self):
        print("Authentication successful in Card")

    def pay(self, amount):
        print(f"{amount} paid using Card")

    def refund(self, amount):
        print(f"{amount} refunded to ur card")

class NetBankingPayment(PaymentGateway):
    def authenticate(self):
        print("Authentication successful from ur Bank")

    def pay(self, amount):
        print(f"{amount} paid to Net account")

    def refund(self, amount):
        print(f"{amount} refunded to ur account")


# l = [UPIPayment(), CardPayment(), NetBankingPayment()]
# for i in l:
#     i.authenticate()
#     i.pay(1000)
#     i.refund(100)

# class A:
#     def __init__(self,n):
#         print("A")
#         self.n = n
#
# class B(A):
#     def __init__(self,n,m):
#         print("B")
#         super().__init__(n)
#         self.m = m
#
# class C(B):
#     def __init__(self,n,m,o):
#         print("C")
#         super().__init__(n,m)
#         self.o = o

# c1 = C(10,20,25)


class A:
    def m1(self):
        print("A")

class B:
    def m1(self):
        print("B")

class C:
    def m1(self):
        print("C")

# l = [A(),B(),C()]
# def run(obj):
#     obj.m1()
# for i in l:
#     run(i)

class Player:
    def __init__(self,name,hp,pin):
        self.name = name
        self.__HP = hp
        self.__pin = pin
        self._items = []

    @property
    def life(self):
        return self.__HP

    @life.setter
    def life(self,n):
        self.__HP = n

    def inventory(self):
        from copy import deepcopy
        pin = input("Pin: ")
        if pin == self.__pin:
            return deepcopy(self._items)
        return None






