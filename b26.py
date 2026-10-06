# def multi(*a):
#     m = 1
#     for i in a:
#         m *= i
#     return m
#
# def avg(*a):
#     s = 0
#     c = 0
#     for i in a:
#         c +=1
#         s += i
#     print(f"Avg : {s/c}")
#
# def display(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i}: {j}")
#
# # display(name="Vamsi",age=21,gender="male",Course="CSE")
# def delivery(price,quantity):
#     total = price * quantity
#     if total < 200:
#         total +=40
#     print(f"Total Bill : {total}")
#
# def main(l):
#     for i,j in enumerate(l):
#         print(f"{i}: {j.__name__}")
#
# li = [multi, avg, display, delivery]
# main(li)

#
#
# import sys
#
# a = [1,2,4]
# b = a
# c = a
# d = a
#
# print(sys.getrefcount(a))
l = lambda x,y: (x+y)*(x-y)
k = lambda z,a: z*a
li = [lambda x,y:x+y,k,l]
def fun(l,x,y):
    print(l(x,y))


def fun2(s,x,y):
    for i in s:
        print(i(x,y))
# fun2(li,7,6)
# l = [1,2,3,4,5,6]
# n = lambda x: x*x
# def mapping(sq,li):
#     el = []
#     for i in li:
#         s = sq(i)
#         el.append(s)
#     return el
# sq = mapping(n,l)
# print(sq)
def is_even(*n):
    l = []
    for i in n:
        if i%2 == 0:
            l.append(i)
    return l

# print(is_even(1,2,4,5,7,8,9))

k = 90
def is_prime(k):
    c = 0
    for i in range(2,k//2):
        if k%i==0:
            return False
    if c == 0:
        print("Prime")
    else:
        print("Not Prime")

# is_prime(23)

# l = (1,2,3,4,5)
# print(l)
# print(*l)

def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # print(**kwargs)

# fun(a=30,b=90,c=100)

# def student_details(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i}:{j}")
#
# # student_details(name="phani",age=101,gender=None,course="Java")
#
#
# class A:
#     def __init__(self,x):
#         self.__x = x
#
#
#     @property
#     def getter(self):
#         # return self.__x
#         pass
#     # @getter.setter
#     # def getter(self,n):
#     #     self.__x = n
#
#
# a1 = A(25)
# print(a1.getter)
# # a1.getter = 400
# # print(a1.getter)
# print(a1.__dict__)
# print(A.__dict__)




# def outter(x):
#     def inner():
#         print(x*200)
#     return inner
#
# l = outter(25)
# m = outter(5)
#
# m() # 1000
# l() # 5000

#
# def multiply(x):
#     def inner(y,a=None):
#         if a:
#             nonlocal x
#             x = a
#         return x*y
#     return inner
#
# double = multiply(2)
# triple = multiply(3)
#
# print(double(75, 5))
# print(triple(30))

# def outter(func):
#     def inner(n):
#         print("hii")
#         func(n)
#     return inner
#
# def greet(name):
#     print(f"Hello {name}")
#
# l = outter(greet)
# l("Pujitha")

def Dec(func):
    def inner(*args,**kwargs):
        us = input("Username: ")
        psd = input("Password: ")
        if us == "Sai" and psd == "Sai1432":
            print("Authentication Successfully Passed")
            func(*args,**kwargs)
        else:
            print("Authentication Successfully Failed")
            print("Invalid Credentials")
    return inner
# @Dec
# def total(a,c,b,d):
#     print(a+b+c+d)
# total(100,200,b=30,d=79)



# Create a password_validator decorator
# Validation rules:
# len(password) > 8
# must and should contain at least 1 special character,
# 1 small letter, 1 capital letter, 1 number.

#
# from random import randint
#
# print(randint(1,45))



