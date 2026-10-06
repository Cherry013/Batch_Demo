# x = 75
#
# if x%2:
#     print("Odd")
# else:
#     print("Even")
#
# t = (1,2,[1,2,3])
# print(t)
# t[2].append(90)

# d = {}
# d['name'] = "Srilatha"
# print(d) # {'name': 'Srilatha'}
# d.update({'a':30,'b':50,'c':90})
# print(d) # {'name': 'Srilatha', 'a': 30, 'b': 50, 'c': 90}
# print(d.keys()) # dict_keys(['name', 'a', 'b', 'c'])
# print(d.values()) # dict_values(['Srilatha', 30, 50, 90])
# print(d.items()) # dict_items([('name', 'Srilatha'), ('a', 30), ('b', 50), ('c', 90)])

# l = {'a':70,'b':90,101:300}
# l['a'] = 700
# print(l) # {'a': 700, 'b': 90, 101: 300}
# l.update({'a':60,'b':99,'n':50})
# print(l) # {'a': 60, 'b': 99, 101: 300, 'n': 50}
# x = l.pop(101)
# print(l) # {'a': 60, 'b': 99, 'n': 50}
# print(x) # 300
# print(l.popitem()) # ('n', 50)
# print(l) # {'a': 60, 'b': 99}


# def even_odd(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")
#     print("hello")
# x = int(input("Enter a number: "))
# even_odd(x)


def fun(b, c, d, *a, e="hii"):
    print(a)  # (10, 20, 30, 78, 99)
    print(type(a))  # <class 'tuple'>
    print(*a)  # 10 20 30 78 99
    # print(10,20,30,78,99) # 10 20 30 78 99


# fun(10,20,30,78,99)
# fun("Hello",'Byee',1,2,3,[2,3])
# print(type(fun)) # <class 'function'>


def find_sum(*args):
    s = 0
    for i in args:
        s += i
    return s
    # return sum(args)


# l = [1,3,4,78,9,10]
# print(find_sum(1,2,3,4,4))
# print(find_sum(3,44,6,7,8))
# print(find_sum(*l))
# print(find_sum(30,49,50,args=90))

# def display(name, age, section, course, batch):
#     print(name, age, section, course, batch)
#
#
# def details(**det):
#     print(det)
#     print(type(det))
#     display(**det)
# details(name="Nithin", age=122, section="4", course="ECE", batch="Py29")


def fun(*args,**kwargs):
    print(args) # (10, 67, 'hjk')
    print(kwargs) # {'a': 30, 'b': 90, 'st': 'Hello'}

# fun(10,67,"hjk",a=30,b=90,st="Hello")
# fun(90,99,a=90,7,b=45,c=100,89) # Error


from random import randint

print(randint(1,27))

# 3. Passing a Value
#
# Create an outer function called calculate() that accepts a number.
#
# Inside it, define a function square() that calculates and prints the square of that number.

# 3rd
# def calculate(x):
#     def square():
#         print(x*x)
#     square()
# calculate(5)

#1st
# def outer():
#     def inner():
#         print("inner function is started")
#     inner()
#     print("outer funtion is executed")
# outer()

#2nd question
# def greeting():
#     def say_hello():
#         print("Hello,Student!")
#     print("Welcome!")
#     say_hello()
# greeting()


#4th
# def operations(a,b):
#     def add():
#         print(a+b)
#     add()
# operations(10,20)

#5th
# def message():
#     def display(name):
#         print(f"Hello {name}")
#     display("Bhagyam")
# message()


#6th
# def calculator(a,b):
#     def add():
#         print(a+b)
#     def multi():
#         print(a*b)
#
#     add()
#     multi()
# calculator(int(input("a: ")), int(input("b: ")))

#7th
# def outer():
#     message = "Python"
#     def display():
#         print(message)
#     display()
# outer()

#8th
# def calculate():
#     def add(a,b):
#         return a+b
#
#     x = add(int(input("a: ")), int(input("b: ")))
#     print(f"Added Value: {x}")
#
# calculate()

#9th
# def check_number(x):
#     def check():
#         print(f"{x} Odd" if x%2!=0 else f"{x} Even")
#     check()
# check_number(36)


#10th
# def student_details(name):
#     def display():
#         print(f"Student Name: {name}")
#
#     display()
# student_details("Akshay")


l = (1,2,3,4)

# a = *l, 1,2,3
# print(a)
b = (*l,1,2,3)
print(b)
