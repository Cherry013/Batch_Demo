# class Watertank:
#     def __init__(self,tn:str,wl:int):
#         self.tank_name = tn
#         self.water_level = wl
#
#     def __add__(self, o2:int):
#         self.water_level += o2
#         return self
#     def __sub__(self, o2:int):
#         self.water_level -= o2
#         return self
#
#     def __truediv__(self, o2:int):
#         l = self.water_level / o2
#         print(f"water level divided by {o2} tanks : ",end="")
#         return l
#     def __str__(self):
#         return f"Tank Name : {self.tank_name}\nWater Level: {self.water_level}"
#
#     def __repr__(self):
#         return str(self.water_level)
#
#
# tank1 = Watertank("tank1",30)
# print(tank1+20)
# print(tank1/5)
# print([tank1])



# l = ['song1','song2','song3','song4','song5','song6']
# l = "How are (123,'u?')?"
# it = iter(l)
# it2 = l.__iter__()
# print(it,it2,sep='\n')
# print(next(it))
# print(next(it2))
# print(it.__next__())
# print(it.__next__())
# print(it2.__next__())



class Playlist:
    def __init__(self,l):
        self.lst = l
        self.index = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.lst):
            song = self.lst[self.index]
            self.index+=1
            return song
        # else:
        #     raise StopIteration

# p1 = Playlist(['Irumudi','Fear','Sayara','Sunflower','Aya Shear'])
# p2 = Playlist(['Souraa','Hukum','Return of OG','Vikram OST','Oorum Blood'])
# p = iter(p1)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# for i in p2:
#     if i is None:
#         break
#     print(i)

class Attendance:
    def __init__(self,st):
        self.students = st
        self.roll_no = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.roll_no < len(self.students):
            name = self.students[self.roll_no]
            self.roll_no +=1
            return name
        else:
            raise StopIteration

# st1 = Attendance(["Adi","Shiva","Sai Ganesh","Balu","Teja"])
# st2 = Attendance(["Raj","Navya","Meghana","chaitrika","Sravani","Ashritha"])
# for i in st1:
#     print(f"{i} : Present")
# for i in st2:
#     print(f"{i} : Present")

class Even:
    def __init__(self,l):
        self.l = l
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.l):
            n = self.l[self.index]
            self.index+=1
            if n%2 == 0:
                return n
            # else:
            #     return next(self)
        else:
            raise StopIteration
# e = Even([1,4,67,66,68,35,57,54])
# for i in e:
#     print(i)


# def fun(x):
#     for i in range(x):
#         yield i
#
# l = fun(30)
# print(l)
# print(next(l))
# print(next(l))
# print(next(l))


def fun2():
    yield 10
    yield 20
    yield 30

# f = fun2()
# print(f)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

def infinite():
    x = 0
    while True:
        yield x
        x+=1

# l = infinite()
# k = infinite()
# print(next(l))
# print(next(l))
# print("for loop")
# for i in l:
#     if i > 10:
#         break
#     print(i)
# for i in k:
#     print(i)
#     if i > 5:
#         break

def even(l):
    for i in l:
        if i%2 == 0:
            yield i
# k = even([1,2,3,3,7,8,2,10])
# print(next(k))
# print(next(k))
# for i in k:
#     print(i)

class User:
    def __init__(self,n,a,g,dob):
        self.name = n
        self.age = a
        self.gender = g
        self.Dob = dob

    def login(self):
        print("Login Successful")

    def logout(self):
        print("Logout Successful")

class Instagram(User):
    def post(self):
        print(f"{self.name} post")
        print("Got 1L likes")

# i1 = Instagram("vidhya",21,"Female","26 Jan 2005")
# print(Instagram.mro())
# i1.post()
# i1.login()
# i1.logout()

class Restaurants:
    def __init__(self,name,rating,address):
        self.name = name
        self.rating = rating
        self.address = address

    def display_menu(self):
        print("All dishes are non-veg only")
class Dish:
    pass
class Swiggy(User, Restaurants, Dish):
    def display(self):
        print("User details")
# print(Swiggy.mro())
class Zomato(User, Restaurants):
    def display(self):
        print("Zomato")

class Customer(Swiggy, Zomato):
    def order(self):
        print("Just Ordering")
# print(Customer.mro())
# s1 = Swiggy("Raj",21,"Male","1 Jan 2004")
# s1.login()
# s1.display_menu()
# s1.logout()
# s1.display()

class Bank(User):
    Name = "RBI"
    def guidelines(self):
        print("Beware of Scammer and call xxx")

class BhimUPI(Bank):
    def Payments(self,amount):
        print(f"{amount} has be paid through UPI")

# b1 = BhimUPI("Nikhil",21,"Male","2 Feb 2004")
# b2 = Bank("Adi",21,"Male","3 Mar 2004")
# print(BhimUPI.mro())
# class B:
#     def m2(self):
#         print("Hello")
#
# class A(B):
#     def m1(self):
#         super().m2()
#         print("A class")

#
# a = A()
# a.m1()


class A:
    def m1(self):
        print("A class")
        super().m1()
class B(A):
    def m1(self):
        print("B class")
        super().m1()
class C(A):
    def m1(self):
        print("C class")
        super().m1()
class E:
    def m1(self):
        print("E class")
class F(E):
    def m1(self):
        print("F class")
        super().m1()
class D(B,C,F):
    def m1(self):
        print("D class")
        super().m1()
# print(D.mro()) # D B C A F E Object
# d1 = D()
# d1.m1()
# class A:
#     def m1(self):
#         print("A class")
#         super().m1()
# class B:
#     def m1(self):
#         print("B class")
# class C(A,B):
#     def m1(self):
#         print("C class")
#         super(C,self).m1()
# a1 = A()
# a1.m1() # Error
# print(C.mro())
# print(B.mro())
# print(A.mro())
# c1 = C()
# c1.m1()

# class A:
#     @classmethod
#     def m2(cls):
#         print("Helllo")
#
#     def m3(self):
#         print("Byee")
#
#     def m4(self):
#         print("Just Demo")
# class B:
#     @classmethod
#     def m2(cls):
#         # super().m2()
#         print("World")
#         a1 = A()
#         a1.m4()
#
#
# b1 = B()
# b1.m2()



