# def hello_makers():
#     print('Hello, Makers!')

# print(type(hello_makers))

# def outer_func():
#     def inner_func():
#         print('Life is so annoying')
#     inner_func()

# outer_func()


# def main_func(func):
#     print(f'I take func {func} like argument')
#     func()
#     return func

# def hello_makers():
#     print('Hello, Makers!')

# print(main_func(hello_makers))


# decorator

# 1
# slug --> gheloveko chitaemoe id

# def slugify(func):
#     def wrapper(title):
#         return title.replace(' ', '-').lower()
#     return wrapper

# @slugify
# def get_title(word):
#     return word

# print(get_title('Nike Airforce 2021'))



# def on_sale(func):
#     def wrapper(sale, old_price):
#         func(sale,old_price)
#         new_price = old_price - (sale * old_price / 100)
#         # old_price = 100%
#         # discount = sale%
#         # discount = sale * old_price / 100
#         print(f'New price is {new_price}$')
#         return new_price
#     return wrapper
# @on_sale
# def buy_product(sale, price):
#     print(f'I have a coupon {sale}%. Old price is {price}$')

# buy_product(int(input('Enter sale: ')), int(input('Enter prices: ')))

# print(buy_product(30,100))


# login
# users = {
#     'jannat': "qwerty",
#     'atai':'elchacha',
#     'ulan': 'ulik'
# }


# def login_required(func):
#     def wrapper(**kwargs):
#         username = kwargs.get('username')
#         password = kwargs.get('password')
#         if username in users and password == users.get(username):
#             print("post created")
#             func(kwargs.get('title'), kwargs.get('image'))
#         elif not username or not password:
#             print('You should login')
#         else:
#             print('Not valid')
     
#     return wrapper

# @login_required
# def create_post(title, image):
#     print(f'{title} - {image}')

# create_post(title= 'post 1', image='post1.jpeg', username= 'jannat', password='qwerty')

# import datetime
# def func_start_time(func):
#     def wrapper():
#         a = datetime.datetime.today().strftime("%d.%m.%Y")
#         b = datetime.datetime.today().strftime("%H:%M:%S")
#         print(a)
#         print(b)
#     return wrapper 

# @func_start_time
# def func():
#     print('Hello world')

# func()



# datenow
# import datetime
# def func_start_time(func):
#     def wrapper():
#         a = datetime.datetime.today().strftime("%d.%m.%Y")
#         b = datetime.datetime.today().strftime("%H:%M")
#         print(f'Функция запущена {a} {b}')
#         func()
#     return wrapper 
# @func_start_time
# def func():
#     print('Hello world')
# func()




from typing import Text


def make_bold(func):
    def wrapper(text):
        <b>text</b>
    return wrapper()
def make_italic(func):
    def wrapper():
        <i>...</i>
def make_underline(func):
    def wrapper():
        <u>...</u>
@make bold
@make italic
@make underline
def hello():
    def wrapper():
        print('Hello world')
    return wrapper
print(hello())





