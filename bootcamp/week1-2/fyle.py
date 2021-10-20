# numbers1 = []
# numbers2 = list()

# numbers1 = [7, 7, 7, 7, 7, 7]
# numbers2 = [7] * 9 
# print(numbers1)
# print(numbers2)


"""range()"""
# range(end)
# numbers = list(range(8))
# print(numbers)

# range(start, end)
# numbers = list(range(1, 6))
# print(numbers)

#range(start, end, step)
# numbers = list(range(1, 28, 2))
# print(numbers)
# for i in range (1, 11):
#     print(i ** 2)


# '''sravnenie spiskov'''

# users = ['Nick', 'Rob', 'Jack', 'Niki']
# for user in users:
#     print(f'Hello, {user}')



# 1 

# list_len = int(input("Enter list length: "))
# list_ = []
# for i in range(list_len):
#     element = input("Enter element: ")
#     print(element)
#     list_.append(element)
# print(list_)




# list_len = int(input("Enter list length: "))
# for i in range(list_len):
#     list_ = []
#     element = input("Enter element: ")
#     print(element)
#     list_.append(element)
# print(list_)     # kajdyi raz novaya inf vykidyvaet staroe


# 2 data
# data = [
#     ['Uluk777', 'qwerty'],
#     ['timurrr', '12345'],
#     ['aliya', 'helloworld']
# ]

# users = []
# for user in data:
#     username = user[0]
#     users.append(username)
# print(users)
# a = 3
# while a > 0:
#     chel = input("Enter user name: ")
# if chel in users:
#     print("This user is already exists ")
# else:
#     password = input("Set your password: ")
#     data.append([chel, password])
# a -= 1
#     print(data)


# new_list

# name_of_list = ["bootcamp"]
# new_list = []
# if (len(name_of_list[0])) % 2 != 0:
#     mean_index = len(name_of_list[0]) // 2
#     new_list.append(name_of_list[0][(mean_index + 1):])
#     new_list.append(name_of_list[0][:(mean_index + 1)])
#     print(new_list)
# else:
#     mean_index = len(name_of_list[0]) // 2
#     new_list.append(name_of_list[0][mean_index:])
#     new_list.append(name_of_list[0][:mean_index])
#     print(new_list)

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# operation = input("Выберите операцию из следующих +-*/%**// :")
# dict_ = (
#     '+': num1 + num2,
#     '-': num1 + num2,
#     '*': num1 + num2,
#     '/': num1 + num2,
#     '//': num1 + num2,
#     '%': num1 + num2,)
#     print(dict_.get(choice))
# except_zerodivisionError



# calc > input('Vvedite operation: ')
# print("Otvet ")



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



# name_of_list = ["bootcamp"]
# new_list = []
# if (len(name_of_list[0])) % 2 != 0:
#     mean_index = len(name_of_list[0]) // 2
#     new_list.append(name_of_list[0][(mean_index + 1):])
#     new_list.append(name_of_list[0][:(mean_index + 1)])
#     print(new_list)
# else:
#     mean_index = len(name_of_list[0]) // 2
#     new_list.append(name_of_list[0][mean_index:])
#     new_list.append(name_of_list[0][:mean_index])
#     print(new_list)







# name_of_list = ["bootcamp"]
# new_list = []
# if (len(name_of_list[0])) % 2 != 0:
#     index = len(name_of_list[0]) // 2
#     new_list.append(name_of_list[0][(index + 1)/2])
#     new_list.append(name_of_list[0][:index + 1/2])
#     print(new_list)
# else:
#     index = len(name_of_list[0]) // 2
#     new_list.append(name_of_list[0][index:])
#     new_list.append(name_of_list[0][:index])
#     print(new_list)


# list_ = ["hello", "world"]
# list_.reverse()
# print(list_)

list_ = ["hello", "world"]
list_.reverse()
new_list(list_.reverse())
print(new_list)

