# class Human:
#     golova = 'Голова'
#     def __init__(self, name, age = 0):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return str(self.age)
    
#     # def __add__(self, a, b):
#     #     return f'{len(self.name)}{len(self.age)}'

# class Planet:
#     people = []

#     def __init__(self, name, life):
#         self.name = name
#         self.life = life

#     def add_human(self, human):
#         self.people.append(human)
#         print(f'Welcome {self.name}, {human.name}')

# earth = Planet('Earth', True)
# Naiza = Human('Naiza', age = 20)
# Naiza = Human('Naiza', age = 20)
# # test = Human
# earth.add_human(Naiza)
# print(earth.people)



# from abc import ABC, abstractclassmethod, abstractmethod
# class Animal(ABC):
#     instinct = ('eat', 'razmnozhenie')

#     def __init__(self, name, age, poroda):
#         self.name = name
#         self.age = age
#         self.poroda = poroda

#     @abstractclassmethod
#     def hunting(self):
#         print('It can hunt')

#     @abstractclassmethod
#     def eat(self):
#         print('I can eat')

# class Hobby:
#     game = {
#         'cat': 'Tsarapat',
#         'dog': 'Return ball'
#     } 

# class Dog(Animal, Hobby):

#     def __init__(self, name, age, poroda):
#         super().__init__(name, age, poroda)

#     def eat(self):
#         return super().eat()
    
#     def hunting(self):
#         return super().hunting()

#     def __str__(self):
#         return self.name

# faramir = Dog('Faramir', 3, 'pudel')
# print(faramir.instinct)
# print(faramir.hunting)

# class Cat(Animal, Hobby):

#     def __str__(self):
#         return self.name
#     def __init__(self, name, age, poroda, owner):
#         super().__init__(name, age, poroda)
#         self.owner = owner
#     def __str__(self):
#         return self.name
    
#     @property
#     def hunting(self):
#         print('It can not hunt. It is domestic')

#     def eat(self):
#         print('It can eat')
        
        

    
#     def play(self, classs):
#         try:
#             return Hobby.game[classs]
#         except KeyError:
#             return 'takogo net'

#     @property
#     def info(self):
#         return f'{self.name} {self.age} {self.poroda} {self.owner}'

# cat = Cat('Beef Stroganoff', 4, 'Siamtwin', 'Aliya')
# print(cat.play('cat'))

# bobik = Dog('bobik', 20, 'kandek')
# print(bobik.hunting)

# print(Dog.__mro__)

from abc import ABC, abstractmethod

class Initil(ABC):

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class DataBase():
    dict_ = {}

    def db(self):
        DataBase.dict_.update({str(self.name) : (self.password)})

    def __init__(self, name, email, password):
        # super().__init__(name, email, password)
        self.name = name
        self.email = email
        self.password = password
           
    @property
    def db(email, password):
        DataBase.dict_[email] = password
        
        
class Registration(DataBase, Initil):

    def __init__(self, name, email, password, password_confirm):
        super().__init__(name, email, password)
        self.password_confirm = password_confirm

    def registration(self):    
        if not self.email.endswith('@mail.ru'):
            raise ValueError ('Email doljen zakanChivatsya')
        if len(str(self.password)) < 5:
            raise ValueError ('Parol doljen byt > 5')
        else:
            self.password = self.password 
        if self.password != self.password_confirm:
            raise ValueError('Email ne sovpadaet')

class Authorization():
    pass


user = Registration('Sezim', 'Sezim@mail.ru', 123456, 123456)
user.registration()
print(DataBase.dict_)








