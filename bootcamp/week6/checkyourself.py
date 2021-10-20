# class Circle:
#   color = 'blue'
#   Pi = 3.14
#   def __init__(self, radius):
#     self.radius = radius

#   def s(self):
#     num = self.Pi * self.radius ** 2
#     return num
# circle1 = Circle(2)
# circle1.color = 'red'
# print(circle1.s())



# 3) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит 
# информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
# Затем объявите экземляр класса и вызовите метод.
# """
# class PhoneNumber:
#     def __init__(self, name, last_name, contact):
#         self.name = name
#         self.last_name = last_name
#         self.contact = contact
    
#     def get_info(self):
#         return f'Контакт : {self.name} {self.last_name}, телефон: {self.contact}'
# num = PhoneNumber(name ='Иван', last_name = 'Петров', contact = '+996770854562')
# print(num.get_info())
"""
5) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
"""
# class Dog:
#     def voice(self):
#         print(f"Гав")
    
# class Cat:
#     def voice(self):
#         print(f'Мяу')

# fluffy = Cat()
# sweety = Dog()

# def to_pet(action):
#     action.voice()

# sweety.to_pet()




"""
4) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом 
человеке.
Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в 
родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет 
выводить данные об этом студенте.
Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f'{self.name} {self.age}')

# class Student(Person):

#     def __init__(self,name, age, course):
#         super().__init__(self, name, age)
#         self.course = course 

#     def display_student(self):
#         print(f'{self.name} {self.age} {self.course}')

# aliya = Student("Aliya", "25", 'IT')
# print(aliya.display())
# print(aliya.display_student())



# class Salary:
#     def __init__(self,pay):
#         self.pay = pay

#     def getTotal(self):
#         return (self.pay*12)

# class Employee:
#     def __init__(self,pay,bonus):
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)

#     def annualSalary(self):
#         return "Total: " + str(self.salary.getTotal() + self.bonus)

# employee = Employee(100,10)
# print(employee.annualSalary())


# class Salary(object):
#     def __init__(self, pay):
#         self.pay = pay

#     def getTotal(self):
#         return (self.pay * 12)

# class Employee(object):
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus

#     def annualSalary(self):
#         return "Total: " + str(self.pay.getTotal() + self.bonus)

# salary = Salary(100)
# employee = Employee(salary, 10)
# print(employee.annualSalary())


# class WinDoor:
#     def __init__(self, x, y):
#         self.square = x * y
# class Room:
#     def __init__(self, x, y, z):
#         self.square = 2 * z * (x + y)
#         self.wd = []
 
#     def add_wd(self, w, h):
#         self.wd.append(WinDoor(w, h))
 
#     def work_surface(self):
#         new_square = self.square
#         for i in self.wd:
#             new_square -= i.square
#         return new_square
# r1 = Room(6, 3, 2.7)
# print(r1.square)  # выведет 48.6
# r1.add_wd(1, 1)
# r1.add_wd(1, 1)
# r1.add_wd(1, 2)
# print(r1.work_surface())  # выведет 44.6    new_square = self.square
#         for i in self.wd:
#             new_square -= i.square
#         return new_square
# r1 = Room(6, 3, 2.7)
# print(r1.square)  # выведет 48.6
# r1.add_wd(1, 1)
# r1.add_wd(1, 1)
# r1.add_wd(1, 2)
# print(r1.work_surface())  # выведет 44.6


# class Heart:
#     def __init__(self, heartValves):
#         self.heartValves = heartValves
#     def display(self):
#         return self.heartValves
# class Person:
#     def __init__(self, fname, lname, address, heartValves):
#         self.fname = fname
#         self.lname = lname
#         self.address = address
#         self.heartValves = heartValves  # Aggregation
#     def display(self):
#         print("First Name: ", self.fname)
#         print("Last Name: ", self.lname)
#         print("Address: ", self.address)
#         print("No of Healthy Valves: ", hv.display())

# hv = Heart(4)
# p = Person("Adam", "Lee", "555 wso blvd", hv)
# p.display()


# class Wall:
#     def __init__(self, height, length):
#         self.height = height
#         self.length = length
#     def get_total_square(self, wall_square):
#         wall_square = (self.height * self.length)
#         return wall_square
# class Window():
#     def __init__(self, winheight, winlength):
#         self.winheight = winheight
#         self.winlength = winlength
#         self.walls = Wall(self.wall_square)
#     def windows(self):
#         return (self.winheight * self.winlength) - self.wall_square
# w1 = Wall(2700, 3500)
# print(w1.get_total_square)








