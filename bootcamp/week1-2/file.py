# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# operation = input("Выберите операцию из следующих +-*/%**// :")
# if operation == '+':
#     print(num1 + num2)
# elif operation == '-':
#     print(num1 - num2)
# elif operation == '*':
#     print(num1 * num2)
# elif operation == '/':
#     print(num1 / num2)
# elif operation == '%':
#     print(num1 % num2)
# elif operation == '**':
#     print(num1 ** num1)
# elif operation == '//':
#     print(num1 // num2)
# else:
#     print('Данной операции нет в системе')

# task 1 
# monday = {'math', 'literature', 'physics'}
# tuesday = {'russian', 'biology', 'chemistry'}
# wednesday = {'Pe', 'biology', 'chemistry'}
# thursday = {'russian', 'Music', 'math'}
# friday = {'economics', 'chemistry', 'CS', 'math'}

# study_week = (monday, tuesday, wednesday, thursday,friday)

# # 2
# for i in range(len(study_week) - 1):
#     if study_week[i] & study_week[i + 1]:
#         # print(*(study_week))
#         study_week[i + 1].remove(*(study_week[i] & study_week[i + 1])
#         study_week[i + 1].add('politics')
# print(study_week)
#     # print(study_week[i])
    # print(study_week[i + 1])

# 1
# for day in study_week:
#     # print(day)
#     for subject in day:
#         if subject == 'chemistry':
#             day.remove('chemistry')
#             day.add('politics')
# print(study_week)
        
    #     print(subject)
    # print(----------)
# for day in study_week:
#     day.discord('chemistry')
# print(study_week)

# set1 = {20, 78, 33}
# set2 = {90, 20, 40}
# set3 = {33, 90, 100}
# print(set1 - set2 - set3)

# import random
# # print(random.choice(['Atai', 'Sana', 'Dana']))

# # randomizer
# # print(random.randrange(50, 10000))

# # print(random.choices(['Atai', 'Sana', 'Dana', 'Aliya', 'Niki'], k=2))
# print(random.sample(['Atai', 'Sana', 'Dana', 'Aliya', 'Niki'], k=2))
# # print(dir(random))


# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# if robert & kail:
#     print("kail, merri")
# elif robert & merri:
#     print(merri)
# elif robert & kail and robert & merri:
#     print(kail, merri)
# elif 
# else:
#     print("no")
# elif robert & merri:
#     print("merri")
# elif kail & merri:
#     print("kail, merri")


# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# for name in robert & kail:
#     print("kail")
# elif robert & merri:
#     print(merri)
# elif robert & kail and robert & merri:
#     print(kail, merri)


# tilek = {'Dodo', 'ImperiaPizza', 'FreshBox'}
# timur = {'OchakKebab', 'FreshBox'}
# alexander = {'FreshBox', 'KFC'}
# elina = {'Dodo', 'ImperiaPizza', 'FreshBox', 'OcakKebab', 'KFC'}
# print(random.choice([tilek, timur, alexander, elina]))

# ingredients = {"сыр чеддар", "грибы", "соус","шпинат"}
# ingredients.add("помидор")


# ingredients = {"сыр чеддар", "грибы", "соус","шпинат"}
# ingredients.add("помидор")
# ingredients.discard("колбаса")
# ingredients.remove("шпинат")
# ingredients.add("базилик")
# ingredients.discard("сыр чеддар")
# ingredients.add("сыр моцарелла")
# print(ingredients)


# ingredients = {"сыр чеддар", "грибы", "соус","шпинат"}
# ingredients.add("помидор")
# ingredients.discard("колбаса")
# ingredients.remove("шпинат")
# ingredients.add("базилик")
# ingredients.discard("сыр чеддар")
# ingredients.add("сыр моцарелла")
# print(ingredients)

# my_dict = {1 : "Finneas", 2 : "Cooper", 3 : "Aisha"}
# print(my_dict.keys())


# task dict
# test = {
#     "Atai": 15,
#     "Bektur": 13,
#     "Jannat": 2,
#     "Kamila":11,
#     "Ulan":10
# }
# scores = test.values()
# print(sum(scores) / len(test))

# users = {
#     "Kani": "kani@gmail.com",
#     "Atai": "elchacha@mail.ru",
#     "Jannat":"Jannat@gnmail.com",
#     "Sezim":"sezim@gmail.com",
#     "Aliya": "aliya@gmail.com",
#     "Dana": "dana@gmail.com",
#     "Fatima": "fatima@mail.ru"
# }
# user_emails = users.values()
# total = len(users)
# gmail_count = 0
# for email in user_emails:
#     if email.endswith("@gmail.com"):
#         gmail_count += 1

# # total - 100

# print(f'Procent polzovateley s gmail sostavlyaet: {round(gmail_count * 100/total,2)}%')


# # task 3
# person = {
#     "name": "Nurbolot",
#     "age": 35,
#     "languages": ['Python', 'JavaScript'],
#     "children": [
#         {
#             "name": "Jannat",
#             "age": 10
#         },
#         {
#             "name":"Aselya",
#             "age": 5
#         }
#     ]
# }
# # person["languages"].append("Python")
# # print(person)
# # person["languages"].append("C#")
# person.setdefault("salary", 4000 )
# # person.update({"salary": 4000})
# # person["wife"] = {
# #     "name": "Karen",
# #     "age": 29
# # }
# # person["children"].append({"name": "New_child", "age": 0})
# # print(len(person["children"]))
# print(person)

# print(person)
    # print(email)
# print(total)

# 4
# TIME = "10:00:00"
# students = {
#     "Kanat": "09:20:34",
#     "Aliya": "09:50:50",
#     "Uluk": "14:00:00",
#     "Kair": "09:59:59",
#     "Emil": "10:00:01"
# }
# late_students = []
# for key,val in students.items():
#     if val > TIME:
#         late_students.append(key)
# print(late_students)


# a = {'x': 1, 'y': 2, 'z': 1}
# a = 
# print(a.keys())

# seasons = {'лето': "жара", "осень": "дождь", "весна": "дождь"}
# seasons.update({"": ""})

# a = {'a':1, 'b': 2, 'c': 1}
# print(a.pop())

# a = {'a':1, 'b': 2, 'c': 1}
# print(a.items())
# for k, v in a.items():
#     print(k, v)
    
# a = {'a': 1, 'b': 2, 'c': 1}
# print(a.items())
# for x, y in a.items():
#     print(x, y)


# a = {'a': 1, 'b': 2, 'c': 3}
# print(a.items())
# for k, v in a.items():
#      print(k, v)

# a = {'a': 1, 'b': 2, 'c': 1}
# for k, v in a.items(): 
#     print(k, v)

# a = {'a': 1, 'b': 6, 'c': 1, 'd': 5, 'e': }
# b = a.copy()
# for value in b.values():
#     if value % 2 == 0:
#         b.update()
# print(b)


# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = a.copy()
# for value in b.values():
#     if value % 2 == 0:
#         b.update()
# print(b)

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = a.copy()
# # print(b)
# for v in b.values():
#     if v % 2 == 0:
#         b.setdefault(2)
# print(b)
    

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = a.copy()
# # list(b.values())
# print(b)
# # # for v in b.values():
# # if  2 == 0:
# #     b.setdefault(0, 2)
# # print(b)

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = a.copy()
# # list(b.values())
# for i in b.values():
#     # if b % 2 == 0:
#     # b.setdefault(0, 2)
#     print(b)


# # comprehension
# string = "Azamat is an amazing actor."
# list_ = []
# for letter in string:
#     if letter.lower() == 'a'
#     list.append('*')
#     else:
#         list.append(letter)
# print('.',join(list_))


# string = "Azamat is an amazing actor."
# list_ = [
# letter if not letter.lower() == 'a' else '*' 
# for letter in string
# ]
# print(''.join(list_))

# print(list_)

# string = "Azamat is an amazing actor."
# list_ = [letter*5 for letter in string]
# print(list_)


# string = "Azamat is an amazing actor."
# list_ = [
#     f'Eto bukva {letter}' if not letter.lower() == 'a' else '*$' 
#     for letter in string
#     ]
# print(list_)

# 2 
# users = {
#     'post1': ['Emil', 'Bektur', 'Jannat', 'Sezim', 'Atai','Jannet', 'Ruslan'],
#     'post2': ['Atai', 'Nurbek', 'Bektur', 'Bektur', 'Emil'],
#     'post3': ['Jannat', 'Atai', 'Bektur', 'Aykol', 'Aliya', 'Emil', 'Fatima']
# }
# # 2 sposob
# list_users = [set(list_) for list_ in users.values()]
# candidates = list_users[0]
# for set in list_users:
#     candidates &= set 
# print(candidates)

# print(list_users)
# print(list_users[0] & list_users[1] & list_users[-1])
# print(users.values())
# 1 sposob
# candidates = [
#     name for name in users['post1']
#     if name in users['post2'] and 
#     name in users['post3']
# ]
# import random 
# winner = random.choice(candidates)
# print(winner)



# likes = {key:len(val) for key,val in users.items()}
# most_liked_post = None
# most_likes = 0
# for post, like in likes.items():
#     if like > most_likes:
#         most_likes = like
#         most_liked_post = post


# print(most_liked_post)


# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude']
# new_list = ["shorter" if len(name) > 4 else "longer" for name in list_name]
# print(new_list)


# dict_ = {i: i**2 for i in range(1, 11)}
# print(dict_)

# # dict_ = {**2 for k,val in range(1,11)}
# # print(dict_)


# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: val for k, val in a.items()}
# print(dict_)


# dict_ = {'first': 1, 'second': 2, 'third': 3}
# a = {key:'even' if val % 2 == 0 else 'odd' for val in dict_.items()}
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [i for i in string_ if i.isdigit()]
# print(list_)

# exceptions
# 1
# products = {
#     'milk': 2,
#     'bread': 1,
#     'eggs': 20,
#     'potato': 35
# }
# while products:
#     product = input('Enter product: ')
#     try:
#         products.pop(product)
#         print(products)
#     except KeyError:
#         print('There is no such product!!!')
#     finally:
#         print(products)
    
# else:
#     print('Products is empty')



# 2

# gallery = []
# try:
#     memory = int(input('Choose memory size: '))
# # except ValueError:
# #     print('Enter number not a symbol')
# # except Exception as e:
# #     print((type(e)._name_)) # tip isklucheniya
# while memory:
#     photo = input('Make photo: ')
#     gallery.append(photo)
#     memory -= 1
# else:
#     print(gallery)
#     raise MemoryError('Your gallery is full!!!! ')


# 3

# kurs = {
#     'buy': {
#         'dollar': 84.50,
#         'euro': 101.25,
#         'rub': 1.10
#     },
#     'sell':{
#         'dollar': 84.90,
#         'euro': 102.10,
#         'rub': 1.30
#     }
# }

# while True:
#     try:
#         operation = input('Choose operation (sell, buy): ').lower()
#         data = kurs[operation]
#         print(data)
#     except KeyError:
#         print('Enter correct operation')
#         continue
#     else:
#         valuta = input('Choose (dollar, euro, rub): ')
#         try:
#             exchange = data[valuta]
#             summa = int(input('How much money do you want to convert? '))
#             if operation == 'buy':
#                 result = summa * exchange
#                 print(f'Your exchange {result} soms')
#             else:
#                 result = summa / exchange
#                 print(f'Your exchange {round(result, 2)} {valuta}s')
#             if summa <= 0:
#                 raise ValueError
#         except ValueError:
#             print('Enter correct amount')
#         except KeyError:
#             print('Enter correct currency')
#         else:
#             end = input('Do you want to continue? ').lower()
#             if end == 'y' or end == 'yes':
#                 continue
#             else:
#                 break





# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# a = {key: innerkey for key, val in dict_.items()
# for innerkey, innerval in val.items() if innerval == max(val.values())}
# print(a)

# my_dict = {k: v for k, v in dict_.items() if v }
# my_max_val = None
# {k: v for k, v in dict_.items() if val + 1 == }
    #     my_max_val=val
    #     my_max_key=k
    #     print(k, val)
    # elif val > my_max_val:
    #     my_max_val=val
    #     my_max_key=k
    #     print( my_max_val)

# my_dict = {key: val for key: val in dict_ if val }
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {key:val1 for key,val in my_dict.items() for key1,val1 in my_dict[key].items()}
# print(dict_)
                
# try:
#     b = 10
#     c = 11
# except ValueError:

# print(a)

# num1 = int(input())
# num2 = int(input())
# try:
#     num1 = int(input())
#     num2 = int(input())
#     num = num1 + num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(num)
# finally:
#     print("Ok")

# num1 = int(input('Введите число: '))
# num2 = int(input("Введите число: "))
# try:
#     num1 = int(input('Введите число: '))
#     num2 = int(input("Введите число: "))
#     s = num1 + num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(s)
# finally: 
#     "ok"



# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     result = num1 + num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(result)
# finally: 
#     "Программа завершена "


#     dict_ = {'key1': 'value1', 'key2': 'value2'}
# dict_ = {i: val for i, val in dict_.items()}
# try:
#     print('key')
# except KeyError:
#     print('Нет такого ключа!')


# try:
#     age = int(input())
#     a = {i for i in age if age > 18}
#     print(a)
# except ValueError:
#     print('Доступ запрещён')
# except :
#     print('Введен некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')



# try:
#     cash = int(input())
#     if cash <= 0:
# except ValueError:
#     print('Сумма не может быть отрицательной!')
# else:
#     print(cash)



# functions

# def get_product_cost(item, qty, price_per_one):
#     # item, qty, price_per_one
#     result = qty * price_per_one
#     print(f'{item} - {result} dollars')


# get_product_cost(price_per_one=3, item='banana', qty= 5)

# # print('hello', 'world', sep= '\n')

# *args **kwargs

# best_friends = []

# def add_to_best_friends(name):

#     best_friends.append(name)
#     print(f'New friend {name} added to best friends')


# add_to_best_friends('Aidai')

# add_to_best_friends('Bektur')
# print(best_friends)



# def get_sum(a, b):
#     return f'Return is: {a + b}'

# result = get_sum(3, 7)
# result2 = get_sum(10, 9)
# print(result)
# print(result2)


# def spargalka(param1, param2, *args, **kwargs):
#     if- else
#     for 
#     while 
#     def 
#     print()
#     input()
#     try- except 
#     return 'hello'
# spargalka(arg1, arg2, ars1,kwargs1)


# cash = int(input())
# if cash <= 0:
#     raise ValueError ('Сумма не может быть отрицательной!')
# else:
#     print(cash)

# def get_add(num1, num2):
#     result = num1 + num2
#     num
#     return(result)

# num = 6
# def check(num1):
#     if num1 % 2 != 0:
#         print('It is odd number')
#     else:
#         print('It is even number')
# check(num)
# print(check(num))


# num = 6
# def check(a):
#     if a % 2 != 0:
#         print('It is odd number')
#     else:
#         print('It is even number')
#         return num
# print(check(num))


# def is_palindrome(word):
#     return word == word[::-1]
# print(is_palindrome('довод'))



# def is_palindrome():
#     for i in is_palindrome() if len(i) < i or len(i) > i:
#         print(False)
#     i != i[::-1]
# print(is_palindrome('довод'))

# dict_ = {'apple': 75, 'banana': 110, 'lemon': 125 }
# print(list(dict_.items()))
# for i,v in list(dict_.items()):
#     if v % 2 == 0:
#         del dict_[i]
# print(dict_)


# built- in, global, local

# a = 9 
# def func():
#     global a
#     a += 1
#     return a

# print(func())


# nonlocal

# def func1():
#     a = 9
#     def func2():
#         nonlocal a 
#         a = 10
#         a += 1
#         return a
#     print(func2())



# def func1():
#     a = 9
#     def func2():
#         # a = 10
#         def func3():
#             # a = 0
#             nonlocal a
#             a += 1
#             return a 
#         return(func3())
#     return(func2())
# print(func1())


# instagram = {}
# post_number = 0

# def generate_id():
#     # import random
#     global post_number
#     post_number += 1
#     return post_number
#     # id_ = random.randint(1, 3)
#     # if id_ in instagram.keys():
#     #     return generate_id()
#     # else:
#     #     return id_

# def create_post(title, author):
#     post_id = generate_id()
#     print(post_id)
#     post = {
#         post_id: {
#         'title': title,
#         'author': author
#         }
#     }
#     instagram.update(post)
#     return post_id

# def delete_post(post_id):
#     confirm = input('Do you really want to delete this post? (y/n): ').lower()
#     if confirm == 'y':
#         instagram.pop(post_id)
#         print('SUCCESSFULLY DELETED')
#     else:
#         pass


# post1 = create_post('hello world', 'kani')
# post2 = create_post('Python14', 'aikol')
# post3 = create_post('JavaScript','Jannat')

# print(instagram)
# delete_post(post2)
# print(instagram)

# name = input('Whats your name? ')
# import random
# number = random.randint(1, 15)
# wish = input('You want to play? ')

# lives = 0
# while True:
#     lives += 1 
#     if lives > 6:
#         print('Game over =(')
#         wish = input('Want to play again?: ')
#         number = random.randint(1, 15)
#         lives = 0
#         continue
#     if wish.lower().strip() == 'yes':
#         try:
#             guess_number = int(input(f'Загадано число от 1 до 15. У вас есть 6 попыток. Угадайте чсисло. Попытка № {lives}: '))
#         except ValueError:
#             print('Vvedite chislo, a ne stroki')
#             continue
#         if guess_number == number:
#             print(f' Vy vyigrali! ')
#             wish = input('Hotite sygrat snova? ')
#             lives = 0
#     elif wish.lower().strip() == 'no':
#         print(f'Do svidaniya, {name} ')
#         break
#     else:
#         print('Vvedite "yes" ili "no"')
#         lives = 0
#         break



# def sum_digits(num:int):
#     num = str(num)
#     res = 0
#     for i in num:
#         res += int(i)
#     return res

# print(sum_digits(456))



# def foo():
#     global var
#     var = 'переменная foo'
#     def bar():
#         print('переменная в foo: переменная bar')
#         return 
#     bar()
 
# print(f'переменная в foo:' var)
# foo()



# def foo():
#     var = 'переменная foo'
#     def bar():
#         global var
#         var = 'переменная bar'
#     bar()
#     return var
# print("переменная в foo: ", foo())
# print("переменная в foo: ", var)



# num = 3
# def mul(int):
#     global num
#     int**2
#     # import math
# mul(num)
# print(num)



# num = 3 
# def mul(x):
#     global num
#     return pow(x, 2)
# mul(num)
# print()


# num = 3
# def mul(num):
#     a = num ** 2
#     b = a ** 2
#     c = b ** 2
#     num = c
#     return num
# print(mul(num))


# num = 3
# def mul():
#     global num
#     num = num ** 2
#     return num

# mul()
# mul()
# mul()
# print(num)

# mul(num)
# print(num)

# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount
# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')
# def get_balance():
#     global balance
#     n = balance
#     print(f' У вас на счету "{n}" сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()


# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()
# # get_salary(1000)
# print(balance)   


# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     global balance
#     n = balance
#     print(f' У вас на счету {n} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()


# map

# numbers = [-2, -1, -0, 1, 2]
# # abs 
# abs_values = list(map(abs, numbers))
# print(abs_values)

# 2 
# words = ['welcome', 'to', 'Python', '14']
# len_words = list(map(len, words))
# print(len_words)

# 3
# first_it = [1, 2, 3]
# second_it = [4, 5, 6]
# third_it = [1, 1, 1]
# # pow(a, b, c) -> a ** b % c

# new_list = list(map(pow, first_it, second_it, third_it))
# print(new_list)

# 4
# def starts_with_A(word):
#     return word[0] == 'A'

# fruits = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# A_fruits = list(filter(starts_with_A, fruits))
# print(A_fruits)

# 4.2

# fruits = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# new_fruits= list(filter(lambda x: not x.startswith('A'), fruits))
# print(new_fruits)

# 5 
# strings = ['john', 'emily', 'atai', 'ulan', 'jannat']
# strings = [(lambda x: f'${name}!') (name) for name in strings]
# print(strings)


# filter 5 
# students = [
#     ('Adilet', 89),
#     ('Gulya', 78),
#     ('Beks', 50),
#     ('Nurs', 49),
#     ('Aibek', 69)
# ]
# pass_students = [name[0] for name in students if name[-1] >= 61] # comprehension
# # pass_students = list(filter(lambda x: x[-1] >= 61, students))
# print(pass_students)


# reduce
# from functools import reduce
# def add(x, y):
#     return x + y

# numbers = [6, 7, 1, 90, 33, 45]
# print(reduce(add, numbers, 20))


# zip
# students = ['Atai', 'Jannat', 'Ulan']
# groups = ['Python 14', 'JS 13', 'Python Ev. 13']
# room = [9, 11, 5]
# result = list(zip(students, groups, room))
# print(result)


# code = 'print("Hello World")'
# eval(code)

# code = 'for i in range(11):\n\tprint(i)'
# exec(code)


# list_ = [5, 8, 4, 6, 7]
# result = list(filter(lambda x: x > 3, list_))
# print(result)


# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni']
# result = list(filter(lambda x: len(x) > 7, list_))
# print(result)


# filter

# names = ['John', 'alice', 'amber', 'raychel', 'sam', 'arnold']
# filtered_names = list(filter(lambda name: name.startswith('a'), names))
# print(filtered_names)

# numbers = [1, 2, 3, 6, 4, 5, 8, 12, 34]
# filtered_numbers = list(filter(lambda number: number % 3 == 0, numbers))
# print(filtered_numbers)


# dict1 = [{'subject': 'python', 'point': 89}, 
#         {'subject': 'Javascript', 'point': 92}]

# dict_new = list(filter(lambda x: x['subject'] == 'python', dict1))
# print(dict_new)

# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
#     }
# dict1_ = [key: innerkey for key, value in dict_.items() for key: val   if max(key: val)]
# print(dict1_)


# matrix = [
#     [x for x in range(1, 4)]
#     for y in range(1, 4)
# ]
# print(matrix)

# counter = int(bool(0))
# def registration(name, *args, **kwargs):
#     name = name 
#     email = args[0]
#     password = kwargs.get('password')
#     password_confirm = kwargs['password_confirm']

#     def is_email(*args, **kwargs):
#         email = kwargs.get('email')
#         if email.endswith('@gmail.com'):
#             return 'Email proshel'
#         else:
#             raise ValueError('Email ne proshel')
#     is_email(email = email)

#     def is_valid(*args, **kwargs):
#         password = kwargs.get('password')
#         password_confirm = kwargs.get('password_confirm')
#         if password != password_confirm:
#             raise ValueError('paroli ne sovpadayut')
#         else:
#             return 'vi zaregistrirovany'

#     def counter_users():
#         global counter
#         counter = counter + 1
#         return f' kol- vo zaregannyh: {counter}'
#     print(counter_users())
    
#     return is_valid(password = password, password_confirm = password_confirm)

# print(registration("python 14", 
# 'python14@gmail.com', 
# password = '123', 
# password_confirm = '123'))