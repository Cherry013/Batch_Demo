# class Employee:
#     bonus_rate = 0.1
#     def __init__(self,name,salary):
#         self.name = name
#         self.base_salary = salary
#
#     def final_salary(self):
#         return self.base_salary+(self.base_salary*Employee.bonus_rate)
#
#     @classmethod
#     def update_bonus(cls,nb):
#         cls.bonus_rate = nb
#
#     @staticmethod
#     def valid(sal):
#         return sal > 0

# e1 = Employee("Amarnath", 5000000)
# e2 = Employee("Shiva", 5000001)
#
# print(e1.final_salary())
# print(e2.final_salary())
# e1.update_bonus(0.2)
# print(e1.final_salary())
# print(e2.final_salary())

class Book:
    total_books = 0
    def __init__(self,title,author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        t,a = book_str.split("-")
        if cls.is_valid(t):
            return cls(t,a)
        else:
            return "Invalid book string"

    @staticmethod
    def is_valid(t):
        return len(t) >= 3


# bts = "Harry Potter - J.K.Rowling"
# b1 = Book.from_string(bts)
# b2 = Book("The song of Ice and Fire","R.R.Martin")


class Inventory:
    total = 0
    threshold = 20
    def __init__(self):
        self.stock = {}

    def display(self):
        print(f"Inventory: {self.stock}")
        print(f"Total Stock: {self.total}")
        print(f"Minimum Stock: {self.threshold}")

    def add_item(self,item,quantity):
        if self.valid(quantity):
            self.stock[item] = quantity
            Inventory.total += 1
        else:
            print(f"quantity should be greater")
        self.display()

    def remove_item(self,item):
        if item in self.stock.keys():
            self.stock.pop(item)
            Inventory.total -= 1
            print(f"Removed {item} from inventory.")
        else:
            print(f"{item} not in inventory.")
        self.display()

    @classmethod
    def update(cls,nt):
        cls.threshold = nt

    @staticmethod
    def valid(qn):
        return qn >= Inventory.threshold
#
# i1 = Inventory()
# i2 = Inventory()
# i3 = Inventory()
# i1.add_item("'marker",90)
# i2.add_item("mobile",25)
# i3.add_item("laptop",15)
# Inventory.update(10)
# i3.add_item("laptop",15)
# i1.remove_item('laptop')
# i2.remove_item('mobile')



class Employee:
    minimum_exp = 5
    def __init__(self,name,exp,dept):
        if self.valid(dept):
            self.name = name
            self.exp = exp
            self.dept = dept
        else:
            print("Employee is not in the right Department")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Exp: {self.exp}")
        print(f"Department: {self.dept}")
        print('\n')

    def promotion(self):
        self.display()
        if self.exp >= Employee.minimum_exp:
            print("Eligible for promotion")
        else:
            print("Not Eligible for promotion")

    @classmethod
    def change(cls,mp):
        cls.minimum_exp = mp

    @staticmethod
    def valid(dep):
        l = ['HR','Tech','Admin','Non-Tech','Sales','Customer Service']
        return dep in l
#
# e1 = Employee("Shiva",0,'Tech')
# e2 = Employee("Pranitha",10,'HR')
# e3 = Employee("Bhrammi",40,'Customer Service')
# e4 = Employee('Pooja',20,'Admin')
#
# e1.display()
# e2.display()
# e3.display()
# e4.display()
#
# e2.promotion()
# e3.change(20)
# e2.promotion()




class Member:
    limit = 28
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    def BMI_calc(self):
        cal = self.weight / (self.height/100)**2
        print(cal)
        if cal > Member.limit:
            print("Un-fit")
        elif cal< (Member.limit-7):
            print("Underweight")
        else:
            print("Fit")

    @classmethod
    def update_bmi(cls,new):
        cls.limit = new

    @staticmethod
    def valid(h,w):
        return 60 <= h <= 300 and 20 <= w <= 200

# m1 = Member("Chiranjeevi",165,48)
# m2 = Member("Yashwanth",170,60)
# m3 = Member("Amarnath",150,73)
#
# m1.BMI_calc()
# m2.BMI_calc()
# m3.BMI_calc()
#
# Member.update_bmi(35)
# m3.BMI_calc()

class LibraryMember:
    total_members = 0
    borrow_limit = 5
    def __init__(self,name):
        self.name = name
        self.books_list = []
        self.books_borrowed = 0

    # def borrow(self,bk_count):
    #     if LibraryMember.borrow_limit-self.books_borrowed >= bk_count:
    #         self.books_borrowed += bk_count
    #         print(f"{bk_count} Books has been borrowed")
    #     else:
    #         print("limit exceeded")
    #         print(f"Your limit is {LibraryMember.borrow_limit-self.books_borrowed}")

    def borrow(self,title):
        if self.valid(title):
            if self.books_borrowed<LibraryMember.borrow_limit:
                if title not in self.books_list:
                    self.books_borrowed+=1
                    self.books_list.append(title)
                    print(f"{title} book borrowed")
                else:
                    print(f"{title} book already borrowed")
            else:
                print("Your limit to borrow books has reached")

    # def return_books(self,bk_count):
    #     if bk_count <= self.books_borrowed:
    #         self.books_borrowed -= bk_count
    #         print("Books returned")
    #     else:
    #         print("Books not returned")

    def return_book(self,title):
        if self.valid(title):
            if title in self.books_list and self.books_borrowed>0:
                self.books_borrowed-=1
                self.books_list.remove(title)
                print(f"{title} book returned")
            else:
                print(f"{title} book not found")
        else:
            print("give a valid title")

    @classmethod
    def update_borrow(cls,bk_count):
        cls.borrow_limit = bk_count

    @staticmethod
    def valid(title):
        return len(title) >= 5


# l1 = LibraryMember("Kishore")
# l2 = LibraryMember("Ganesh")
# l3 = LibraryMember("Priya")
# l4 = LibraryMember("Sohail")
# l5 = LibraryMember("Harshitha")
# l6 = LibraryMember("Raju")
#
# l1.borrow("English communications")
# l2.borrow("Social Media(GK)")
# l3.borrow("How to kill a men???")
# l4.borrow("Ways to avoid something")
# l5.borrow("The palace of illusion")
# l6.borrow("30days of love")
#
# l3.return_book("How to kill a men???")
# l2.return_book("Social Media")
#


from abc import ABC,abstractmethod

class Account(ABC):
    interest = None
    def __init__(self,bal):
        self.__balance = bal

    @property
    def get_balance(self):
        return self.__balance

    @get_balance.setter
    def get_balance(self,new_balance):
        self.__balance = new_balance

    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def calculate_intrest(self):
        pass

    @classmethod
    def change(cls,n):
        cls.interest = n

    @staticmethod
    def valid(amount):
        return amount >= 0

class SavingAccount(Account):
    interest = 1
    def deposit(self,amount):
        if self.valid(amount):
            self.get_balance += amount
        else:
            print("Your balance cannot be deposited")

    def withdraw(self,amount):
        if self.valid(amount):
            if amount <= self.get_balance:
                self.get_balance -= amount
            else:
                print("Your balance cannot be withdrawn")
        else:
            print("Your balance cannot be withdrawn")

    def calculate_intrest(self):
        print("Interest will be 1%")

class FixedDepositeAccount(Account):
    interest = 5

    def deposit(self, amount):
        if self.valid(amount):
            self.get_balance += amount
        else:
            print("Your balance cannot be deposited")

    def withdraw(self, amount):
        if self.valid(amount):
            if amount <= self.get_balance:
                self.get_balance -= amount
            else:
                print("Your balance cannot be withdrawn")
        else:
            print("Your balance cannot be withdrawn")


    def calculate_intrest(self):
        print("Interest will be 5%")

class CurrentAccount(Account):
    interest = 0.5

    def deposit(self, amount):
        if self.valid(amount):
            self.get_balance += amount
        else:
            print("Your balance cannot be deposited")

    def withdraw(self, amount):
        if self.valid(amount):
            if amount <= self.get_balance:
                self.get_balance -= amount
            else:
                print("Your balance cannot be withdrawn")
        else:
            print("Your balance cannot be withdrawn")


    def calculate_intrest(self):
        print("Interest will be 0.5%")

# acc = [SavingAccount(20000),FixedDepositeAccount(10000),CurrentAccount(100000)]
# for i in acc:
#     print(i.get_balance)




class PaymentMethod(ABC):
    def __init__(self,balance):
        self.__balance = balance

    @property
    def get_balance(self):
        return self.__balance

    @get_balance.setter
    def get_balance(self,new_balance):
        self.__balance = new_balance

    @abstractmethod
    def pay(self,amount):
        pass

    @abstractmethod
    def validate(self,amount):
        pass

    def __add__(self,other):
        return "Split Payment"


class CardPayment(PaymentMethod):
    def __init__(self,pin,balance):
        self._pin = pin
        super().__init__(balance)

    def pay(self,amount):
        pin = input("Enter your PIN: ")
        if pin == self._pin:
            if 0<= amount <= self.get_balance:

                self.get_balance -= amount
                print(f"{amount} has been paid using Card")
            else:
                print("Card Declined Proverty")
        else:
            print("Your PIN is not valid")

    def validate(self,amount):
        return amount >= 0

class WalltetPayment(PaymentMethod):
    def pay(self, amount):
        if 0 <= amount <= self.get_balance:
            self.get_balance -= amount
            print(f"{amount} has been paid using Wallet")
    def validate(self,amount):
        return amount >= 0

class UPIPayment(PaymentMethod):
    def __init__(self,pin,balance):
        self.pin = pin
        super().__init__(balance)
    def pay(self, amount):
        pin = input("Enter your PIN: ")
        if pin == self.pin:
            if 0 <= amount <= self.get_balance:
                self.get_balance -= amount
                print(f"{amount} has been paid using UPI")
            else:
                print("InSufficient Balance")
        else:
            print("Your PIN is not valid")

    def validate(self,amount):
        return amount >= 0

# l = [CardPayment('1234',50000),WalltetPayment(20000),UPIPayment('4321',100000)]
# for i in l:
#     i.pay(2000)

#
# class A:
#     def __call__(self,x):
#         print("Hii, Hello")
#
#
# obj = A()
# obj(20)



# def fun(a):
#     print("Hello",a)
#
# fun(10)
# fun.__call__(10)


class StatementFormatter(ABC):
    def __call__(self):
        print(f"{self.__class__.__name__} is executing")

    def __repr__(self):
        return f"{self.__class__.__name__}"

class PDFFormatter(StatementFormatter):
    pass

class JSONFormatter(StatementFormatter):
    pass

class TEXTFormatter(StatementFormatter):
    pass

k = [PDFFormatter(),JSONFormatter(),TEXTFormatter()]
print(k)
for i in k:
    i()