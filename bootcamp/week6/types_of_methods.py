# class Category:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name

# iphone = Category('Iphone')
# samsung = Category('Samsung')
# nokia = Category('Nokia')
# xiaomi = Category('Xiaomi')


# class Condition:
#     def __init__(self, condition):
#         self.condition = condition
#     def __str__(self):
#         return f'Condition: {self.condition}'

# new = Condition('Новый')
# used = Condition('Использованный')
# repaired = Condition('Отремонтированный') 

# class Phone:
#     def __init__(self, category, model, price, condition):
#         self.category = category
#         self.model = model
#         self.price = price
#         self.condition = condition

#     def __repr__(self):
#         return f'{self.category} {self.model} {self.price} {self.condition}'

#     @classmethod
#     def create_iphone(cls, model, price, condition):
#         return cls(
#             category=iphone,
#             model = model,
#             price = price,
#             condition = condition
#         )
        
#     @classmethod
#     def create_samsung(cls, model, price, condition):
#         return cls(
#             category=samsung,
#             model = model,
#             price = price,
#             condition = condition
#         )

#     @classmethod
#     def create_nokia(cls, model, price, condition):
#         return cls(
#             category=nokia,
#             model = model,
#             price = price,
#             condition = condition
#         )

#     @classmethod
#     def create_xiaomi(cls, model, price, condition):
#         return cls(
#             category=xiaomi,
#             model = model,
#             price = price,
#             condition = condition
#         )


# # iphones_SE_NEW = []

# # for _ in range(10):
# #     iphones_SE_NEW.append(Phone.create_iphone("SE", 80000, new))

# # print(iphones_SE_NEW)

#     @property
#     def title(self):
#         return f'{self.category} {self.model} {self.price} {self.condition}'

#     @staticmethod
#     def sale(percent, price):
#         x = price * percent / 100
#         return x

#     # def sale_price(self, percent):
#     #     sale = self.sale(percent, self.price)
#     #     return self.price - sale

#     def sale_price(self, percent, code):
#         sale = self.sale(percent, self.price)
#         if code.lower() == 'makers':
#             self.price -= sale

#     def __repr__(self) -> str:
#         return self.title

# p1 = Phone.create_iphone('SE', 78000, new)
# p2 = Phone.create_iphone('X', 56000, used)
# print(p2.sale_price(30, 'makers'))
# print(p2.price)
    


# # iphones_samsungs = []
# # import random
# # for _ in range(15):
# #     choice = random.choice([Phone.create_iphone('SE', 78000, new),
# #                             Phone.create_nokia('3310', 25000, repaired, 
# #                             Phone.create_samsung('S10', 50000, new)])

# # p1 = Phone.create_iphone('SE', 78000, new)
# # p2 = Phone.create_iphone('X', 56000, used)
# # p3 = Phone.create_nokia('3310', 25000, repaired)
# # p4 = Phone.create_samsung('S10', 50000, new)
# # p5 = Phone.create_xiaomi('Note9', 25000, used)
# # print(p2.category, p2.condition)
# # print(p3.category, p3.condition)
# # print(p4.category, p4.condition)
# # print(p1.category, p1.condition)
# # print(p5.category, p5.condition)

# # phone1 = Phone(iphone, 'SE', 45000, 'NEW')
# # phone2 = Phone(sam
# # sung, 'Galaxy 9', 23000, 'USED')
