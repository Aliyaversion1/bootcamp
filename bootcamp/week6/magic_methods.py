# # 1 
# class Som:
#     currencies = {
#         'USD': 84.5,
#         'EUR': 101.4,
#         'RUB': 1.06,
#         'KZT': 0.2,
#         "SOM": 1
#     }

#     def __init__(self, value, curr):
#         self.value = value
#         self.curr = curr

#     def __add__(self, other):
#         curr1 = Som.currencies.get(self.curr)
#         curr2 = Som.currencies.get(other.curr)
#         print(f'{self.value * curr1} som and {other.value * curr2} som')
#         return self.value * curr1 +other.value * curr2

# a = Som(100, 'USD')
# b = Som(25, 'EUR')
# print(a+b)

# c = Som(15000,"RUB")
# d = Som(40000, "KZT")
# print(c + d)



# #  2 

# class Distance:
#     units_M = {
#         "SM": 0.01, 
#         "DM": 0.1,
#         "M": 1,
#         "KM": 1000, 
#         "MILES": 1600
#     }

#     def __init__(self, value, unit):
#         self.value = value
#         self.unit = unit


#     def __gt__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} M and {other.value * dist2} M')
#         return self.value * dist1 > other.value * dist2

#     def __eq__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} M and {other.value * dist2} M')
#         return self.value * dist1 == other.value * dist2

#     def __lt__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} M and {other.value * dist2} M')
#         return self.value * dist1 < other.value * dist2


# a = Distance(700, 'KM')
# b = Distance(700, "MILES")
# print(a == b)



# 3 

# class PasswordValidationMixin:
#     def validate_password(self, password):
#         if len(password) >= 8 and not password.isdigit() and not password.isalpha() and not password.islower():
#             self.password = password
#             print('Password created')
#             return True
#         else:
#             print('Invalid password')
#             return False


# class Facebook(PasswordValidationMixin):
#     def __init__(self, username, password):
#         if self.validate_password(password):
#             self.username = username
#             print(f'Facebook account created for {username}!')
#         else:
#             print('Facebook account not created!!!')
    
#     def __getattr__(self, attr):
#         print('GETATTR is working!!!')
#         return "You don't have a Facebook account yet!"

#     def __getattribute__(self, name: str):
#         print('GETATTRIBUTE is working!!!')
#         return super().__getattribute__(name)

# user1 = Facebook('jannat', 'qwerTyu1889')
# print(user1.username)
# print(user1.lastname)
# print(user1.__dict__)
# user1.email = 'jannat@gmail.com'
# print(user1.__dict__)

# 4

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __setattr__(self, name, value):
#         if name == "password":
#             print('Cannot create password')
#             return None
#         return super().__setattr__(name, value)

# jannat = Person('Jannat')
# jannat.name = 'Atai'
# jannat.lastname = 'Janatov'
# print(jannat.lastname)
# jannat.password = 'QWERTY'
# print(jannat.password)


# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value
#     def __ __(self):
        
        
# obj_int = MyNumber(5)

# # task 3 magic methods
# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return (f'Это сложение и результат равен: {self.value + other}')
    
#     def __sub__(self, other):
#         return (f'Это вычитание и результат равен: {self.value - other}')

#     def __mul__(self, other):
#         return (f'Это умножение и результат равен: {self.value * other}')

#     def __truediv__(self, other):
#         return (f'Это деление и результат равен: {self.value / other}')
# obj_int = MyNumber(5)  
# print(obj_int + 5)  
# print(obj_int - 5)  
# print(obj_int * 5)  
# print(obj_int / 5) 



# # Task 4 magic methods
# class Student:
    
#     def __init__(self, name, class_name, ball):
#         self.name = name
#         self.class_name = class_name
#         self.ball = dict(ball)
        
#     def __gt__(self, other):
#         return self.ball > other.ball
        
#     def __lt__(self, other):
#         return self.ball < other.ball
        
#     def __ge__(self, other):
#         return self.ball >= other.ball
        
#     def __le__(self, other):
#         return self.ball <= other.ball

# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2)



# 1 instance, cls, static method

# class Product:
#     base_price = 20000
    
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
    
#     def has_garantiya(self, year):
#         if year - self.year > 2:
#             return f'Ваша гарантия истекла'
#         else:
#             return f'Гарантия действительна'
    
#     @classmethod
#     def change_price(cls, rate):
#         cls.base_price = cls.base_price * rate

# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price) 
        

""""
Создайте класс User, объекты которого имеют атрибуты - name, lastname, email.
Создайте статический метод validate_email, который проверяет есть ли в имейле знак собачки @ и возвращает True либо False.
Переопределите метод __str__ так чтобы если у юзера был валидный имейл при использовании print() вам возвращалась строка:
"{Имя юзера}: {имейл}"
где вместо Имя юзера и имейл должны быть соответствующие значения.
В противном случае должна быть строка:
"email в неправильном формате".
Создайте класс метод create_user, который может создавать объекты от класса User из строк, переданных в таком формате - 
"Имя, Фамилия, имейл".
Например:
user1 = User.create_user('John, Snow, john@email.com') 
применив метод create_user получим объект с John в атрибуте name, Snow в атрибуте lastname и john@email.com в атрибуте email.
Создайте 2 экземпляра класса User - user1 и user2, где user2 должен иметь неправильный имейл(без @). Распечатайте эти объекты
Ввод должен быть:
print(user1) 
print(user2) 
"""
# class User:
#     def __init__(self, name, lastname, email):
#         self.name = name
#         self.lastname = lastname
#         self.email = email
    
#     # @staticmethod
#     def validate_email(email):
#         if "@" in email:
#             return True
#         else:
#             return False 
        
#     def __str__(self):
#         return 'str'  

#     # def create_user(cls):
#     #     pass


# user1 = User('John',  'Snow' , 'john@email.com')
# # user2 = User.create_user()


# print(user1) 
# # print(user2)

class Car:
    __speed = 0
    def set_speed(self, new):
        self.__speed = new
    def show_speed(self):
        return self.__speed
car1 = Car() 
print(car1.show_speed()) 
car1.set_speed(20) 
print(car1.show_speed())