# class SomeClass:
#     pass

# class A:
#     pass

# a = A()  # экземпляр instance или обьект класса

# print(isinstance(a, A))


# user registration OOP task 1

# class User(object):
#     platform = 'Makers'

#     def __init__(self, age, username, password):
#         self.username = username
#         self.age = age
#         self.password = password
#         self.followers = []
    
#     def follow(self, user):
#         user.followers.append(self.username)

#     def unfollow(self, user):
#         user.followers.remove(self.username)

#     def followers_count(self):
#         print(len(self.followers))
#         return len(self.followers)
 
#     def __str__(self):
#         return f'{self.username}, {self.age}'

# jannat = User(22, 'jannat', 'qwerty')
# atai = User(username='atai', age=18, password='helloworld')
# kani = User(username='kani', age=23, password='hello')
# ulan = User(username='ulan', age=29, password='ugh')


# jannat.follow(atai)
# atai.follow(jannat)
# atai.follow(kani)
# kani.follow(jannat)
# ulan.follow(jannat)
# atai.unfollow(jannat)
# # print(atai.followers)
# print(jannat.followers)
# jannat.followers_count()


# task 2 Footbolists
# class FootballPlayer:
#     status = 'sportsman'

#     def __init__(self, name, last_name, team):
#         self.name = name
#         self.last_name = last_name
#         self.team = team
#         self.salary = 50000
#         self.goals = 0

#     def goal(self):
#         self.goals += 1
#         print('GOOOAAALLL!!!!')

# player1 = FootballPlayer('Cristiano', 'Ronaldo', 'MU')
# player2 = FootballPlayer('Lionel', 'Messi', 'PSG')

# import random
# players = [player1, player2]
# for _ in range(10):
#     random.choice(players).goal()

# player1.team = player2.team
# print(player1.team)
# player1.salary = 10000000
# # player1.goal()
# # player2.goal()
# # player1.goal()
# # player2.goal()
# # player2.goal()
# print(player1.salary)
# print(player1.goals)
# print(player2.goals)



# class Song:
#     def __init__(self,title,author,year):
#         self.title = title
#         self.author = author
#         self.year = year
        
#     def show_author(self):
#         print(f'Автор этой песни {self.author}')
    
#     def show_title(self):
#         print(f'Название этой песни {self.title}')
        
#     def show_year(self):
#         print(f'Эта песня вышла в {self.year} году')
        
# song = Song(author= 'Pharell Williams', title='Happy',year= '2013')

# song.show_author()
# song.show_title()
# song.show_year()


# class Circle:
#     color = 'Blue'
#     Pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius
            
#     def get_area(self):
#         mul = Circle.Pi * self.radius ** 2
#         return mul
# circle1 = Circle(2)
# circle1.color = 'red'
# print(circle1.get_area())

# inheritance nasledovanie

# # Employee
# class Employee:

#     stuff = []

#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#         self.id = self.generate_id()
#         Employee.stuff.append({
#             'id': self.id,
#             'name': self.name,
#             'last_name': self.last_name
#         })
    
#     def __str__(self):
#         return f'{self.name} {self.last_name}'

#     def generate_id(self):
#         import random
#         id_ = random.randint(500, 1000)
#         for worker in Employee.stuff:
#             if worker.get('id') == id_:
#                 return self.generate_id()
        
#         return id_

# class BonusMixin:
#     def bonus(self, hours):
#         if hours > 200:
#             self.salary = self.salary + (self.salary * 5 / 100)
#         else:
#             self.salary = self.salary

# class SalaryEmployee(Employee):
#     def __init__(self, name, last_name, salary):
#         super().__init__(name, last_name)
#         info = {
#             'id': self.id,
#             'name': self.name,
#             'last_name': self.last_name
#         }
#         self.salary = self.salary
#         self.bonus(hours)

#         for worker in Employee.stuff:
#             if info == worker:
#                 worker.update({'salary': self.salary })

# class HourlyEmployee(Employee):
#     def __init__(self, name, last_name, hours, per_hours):
#         super().__init__(name, last_name)
#         self.salary = hours * per_hours


# john = Employee('John', 'Snow')
# emily = Employee('Emily','Snow')
# jannat = SalaryEmployee('Jannat','Jannatov', 5000)
# aykol = HourlyEmployee('Aykol', 'Aykolev',155,10 )

# print(john.stuff)
# print(Employee.stuff)






# ¤๋ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧ͜͡ Эсен, [07.10.21 15:22]
# # Employee
# Esenov task
# class Employee:

#     stuff = []

#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#         self.id = self.generate_id()
#         Employee.stuff.append({
#             'id': self.id,
#             'name': self.name, 
#             'last_name': self.last_name
#         })
#     def __str__(self):
#         return f'{self.name} {self.last_name}'

#     def generate_id(self):
#         import random
#         id_ = random.randint(500, 1000)
#         for worker in Employee.stuff:
#             if worker.get('id') == id_:
#                 return self.generate_id()
#         return id_

# class SalaryEmployee(Employee):
    
#     def __init__(self, name, last_name, salary):
#         super().__init__(name, last_name)
#         info = {
#             'id': self.id, 
#             'name': self.name, 
#             'last_name': self.last_name
#         }
#         self.salary = salary
#         for worker in Employee.stuff:
#             if info == worker:
#                 worker.update({'salary': self.salary})

# class HourlyEmployee(Employee):
#     def __init__(self, name, last_name, hours, per_hour):
#         super().__init__(name, last_name)
#         self.salary = hours * per_hour

# esen = Employee('Kiko', 'Koko')
# john = Employee('John', 'Snow')
# janna = SalaryEmployee('Janna', 'Jenna', 20000)
# aykol = HourlyEmployee('Aykol', 'Aykolev', 100, 15)
# print(esen.stuff)
# print(janna)
# print(Employee.stuff)



# users = {'Kayir': 123, 'Eldiar': 123}
# def validate_password(func):
#     def wrapper(username, password):
#         user = kwargs.get('username')
#         pas = kwargs.get('password')
#         if not username in users:
#             raise KeyError('Username is not defined')
#         elif pas != users.get(user):
#             raise Exception ('Password is invalid')
#         else:
#             func(username, password)
#     return wrapper
# @validate_password
# def login(username, password):
#         print(f'Welcome, {username}')
        
# login("Eldiar", 123)



# Task 2 OOP
# class Circle:
#     color = 'blue'
#     Pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         mul = Circle.Pi * self.radius ** 2
#         return mul
# circle1 = Circle(2)
# circle1.color = 'red'
# print(circle1.get_area())

#  Task 3 OOP
# class BankAccount:
#     balance = 0
    
#     def withdraw(amount):
#         BankAccount.balance -= amount
#         return f'Ваш баланс: {BankAccount.balance} сом'
#     def deposit(amount):
#         BankAccount.balance += amount
#         return f'Ваш баланс: {BankAccount.balance} сом'        
# account1 = BankAccount
# account1.balance = 5000
# print(account1.withdraw())
# print(account1.deposit())


# task 4 OOP
# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
#     def get_total_cost(self, km):
#         summa = self.cost + self.cost_km * km
#         return f'Такси {self.name} стоимость поездки: {summa}'
# taxi1 = Taxi('Namba', 45, 25)
# taxi2 = Taxi('Yandex', 50, 15)
# taxi3 = Taxi('Jorgo', 53, 22)
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))  

# Task 5 OOP
# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'
# contact = Phone("John", "Snow", "+9967582566")
# print(contact.get_info())




# Polymorphism OOP

# from abc import ABC, abstractmethod

# class Pizza(ABC):
#     def __init__(self, pizza, cost):
#         self.pizza = pizza
#         self.cost = cost

#     @abstractmethod
#     def add_extra(self, *ingredient):
#         self.ingredient = ingredient
#         print(f'{self.pizza} with extra {self.ingredient} costs {self.cost}')
# class DodoPizza(Pizza):
#     def add_extra(self, *ingredient):
#         self.cost += 50 * len(ingredient)
#         return super().add_extra(ingredient)

#     def late(self, time):
#         if time >= 5:
#             print(f'You get free pizza card!!!')

# class PapaJohns(Pizza):
#     def add_extra(self, *ingredient):
#         self.cost += 70 * len(ingredient)
#         return super().add_extra(ingredient)

#     def late(self, time):
#         if time >= 100:
#             print(f'This pizza is free')
#             self.cost = 0
#         else:
#             self.cost = self.cost - (self.cost * time / 100)

# pizza1 = DodoPizza('Pepperoni', 500)
# pizza1.add_extra('cheese', 'sauce', 'pepperoni')
# pizza1.late(5)
# pizza2 = PapaJohns('Margarita', 400)
# pizza2.add_extra('tomatoes', 'bazil')
# pizza2.late(30)
# print(pizza2.cost)

# for pizza in [pizza1, pizza2]:
#     pizza.late(10)


#  2 

# class King:
#     @staticmethod
#     def some_static_method():
#         print(f"I'm staticmethod")
#     @staticmethod
#     def move():
#         print('Я хожу на 1 клетку в любую сторону')

# class Queen:
#     @staticmethod
#     def move():
#         print('Я хожу как королева')

# class Horse:
#     @staticmethod
#     def move():
#         print('Я хожу буквой Г')

# figure1 = King()
# figure1.some_static_method()
# figure2 = Queen()
# figure3 = Horse()
# for figure in [figure1, figure2, figure3]:
#     figure.move()



# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name},'
# class Employee(Person):
#     def __init__(self, work, status):
#         super().__init__()
#         self.work = work
#         self.status = status
#     def get_info(self):
#         super().__init__(self.name, self.last_name)
#         return f'я работаю в компании {self.work} на должности {self.status}'
# class Student(Person):
#     def __init__(self, university, course):
#         super().__init__()
#         self.university = university
#         self.course = course
#     def get_info(self):
#         super().__init__(self.name, self.last_name)
#         return f'я учусь в {self.university}  на {self.course} курсе”'
# def get_human_info(self):
#     self.get_info()
    
# person = Person(name = "Иван", last_name = "Петров")
# employee = Employee(work = "Рога и копыта" ,status = "директор")
# student = Student(university = "КГТУ", course = "3")
    
# get_human_info(person) 
# get_human_info(employee) 
# get_human_info(student) 


    










