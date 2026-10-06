import sys


def adding(x,y):
    return x+y

def multi(x,y):
    return x*y

def sub(x,y):
    return x-y

def div(x,y):
    return x/y

# adding(25,30)

# a = adding
# b = 100

# def calling(gowtham,x,y):
#     print(gowtham(x,y))
# x,y = int(input("x: ")), int(input("y: "))
# calling(adding,x,y)


# l = [adding, multi, sub, div]
# print(l)
# print(l[2](25,20)) # 5

# d = {'add':adding, 'sub':sub, "multi":multi, 'div':div}
# print(d)
# print(d['add'](20,30))
# print("Keys: ",d.keys())
# print("Values: ",d.values())
# print("items(Key, Value) : ",d.items())

# c = 0
# for i in d.keys():
#     c+=1
#     # print(f"{c}.{i}")
#     print(c,".",i)
# user = input("Enter the choice (like 'add'): ")
# print(d[user](int(input("x: ")), int(input("y: "))))

# print(adding.__name__)
# e = {1:adding, 2:sub, 3:multi, 4:div}
# for i,j in e.items():
#     print(i,j.__name__)

# def message():
#     print("Hello Python")
#
# m = message
# for i in range(3):
#     m()
# def cube(x):
#     return x**3
#
# def apply(func,value):
#     print(func(value))
#
# apply(cube,10)
#
# count = len
#
# print(count("Hello"))
# print(count([1,2,3,4]))

# f = open('output.txt','w')
#
# l = [1,2,3,'A','B','C']
# print(*l,sep=" @ ", file=sys.stdout)
#
# f.close()

def calculate_bill(*args,**kwargs):
    print(f"Prices: {args}")
    print(kwargs)
    # discount = kwargs.get("discount",0)
    if 'discount' not in kwargs:
        discount = 0
    else:
        discount = kwargs['discount']
    # delivery = kwargs.get('delivery',0)
    if 'delivery' not in kwargs:
        delivery = 0
    else:
        delivery = kwargs['delivery']
    # tax = kwargs.get('tax',0)
    if 'tax' not in kwargs:
        tax = 0
    else:
        tax = kwargs['tax']

    price = sum(args)
    return price + delivery + tax - (discount * price)

# print(calculate_bill(35,56,78,99,100,57,delivery=20,tax=35,discount=0.2))


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def calculate(a,b,operation):
    print(operation(a,b))

# calculate(10,25,add)
# calculate(10,25,sub)
# calculate(10,25,mul)
# calculate(10,25,div)


def display_customer(**details):
    print(details)
    for i,j in details.items():
        print(f"{i} : {j}")

def process_customer(display_function, **customer_details):
    display_function(**customer_details)

# process_customer(display_customer,name="mani",emoji="🙄",age=21,gender="male",branch="Mechanical")

print(ord("🙄"))
print(chr(128580))



