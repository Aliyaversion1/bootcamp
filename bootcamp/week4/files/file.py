# file1 = open('makers.txt', 'r')
# print(file1.read())

# task 1
# with open('platform.txt', 'w+') as f:
#     while True:
#         email = input('Enter your email ')
#         if not email:
#             print('STUDENT ADDED')
#             break
#         f.write(email + '\n')



# task 2
# with open('platform.txt') as f:
#     student = input('Enter your email: ')
#     students = f.read()
#     if student in students:
#         print('You have an acces ')
#     else:
#         print('--')

# KPI.txt


# Atai 50 2 
# Ulan 70 5 
# Janat 90 10
# Bektur 85 7 

# with open('kpi.txt') as f:
#     # print(f.readlines())
#     data = list(map(lambda x : x.replace('\n', ''), f.readlines()))
#     data = [name.split() for name in data]
#     # print(data)
#     max_point = 0
#     max_voice = 0
#     for list in data:
#         if int(list[1]) > max_point:
#             max_point = int(list[1])
#             best_student = list[0]
#         if int(list[-1]) > max_voice:
#             max_voice =  int(list[-1])
#             fire_student = list[0]
#     print(best_student, max_point)
#     print(fire_student, max_voice)



# with open('kpi.txt') as f:
#     data = list (map(lambda x: x.replace('\n', ''), f.readlines()))
#     data = [name.split() for name in data]
#     max_point = 0
#     max_voice = 0
#     for list in data:
#         if int(list[1]) > max_point:
#             max_point = int(list[1])
#             best_student = list[0]
#         if int(list[-1]) > max_voice:
#             max_voice = int(list[-1])
#             fire_student = list[0]
#     print(best_student, max_point)
#     print(fire_student, max_voice)


# task 4
# with open('contacts.txt') as f:
#     contacts = f.readlines()
#     # print(contacts)
#     contacts = [contact.split() for contact in contacts]
#     print(contacts)
#     contacts = {contact[0]: contact[1] for contact in contacts}
#     name = input('Enter name: ').lower().title()
#     print(contacts.get(name, 'No such name in contact book'))

# task pokazyvat datu
# from datetime import datetime
# with open('qrcode.txt', 'a') as f:
#     name =  input('Enter name: ')
#     f.write(f'{name} {datetime.now().strftime("%H:%H:%5 %d-%B-%Y")}\n')
#     print(f)


# with open('task5.txt', 'r') as file:
#     list1 = [int(i.replace('\n','') for i in file.readlines())]
# with open('task6.txt', 'w') as file:
#     file.write(f'{min(list1} - {min(list1)}')



# viselica
import random
words = ["книга","дом", "ручка"]
secret = random.choice(words)
hidden_word = list('*' * len(secret))
attemts = 5

while attemts > 0:
    letter = input(f'Ugadaite slovo {hidden_word}\nKolichestvo poputok {attemts}\nVvedite bukvu: ').lower().strip(' ')
    if letter in secret:
        for index, value in enumerate (secret):
            if letter == value:
                hidden_word[index] = letter
            if '*' not in hidden_word:
                print(f'Vy ugadali slovo {secret}! Pozdravlyau!')
                break
    else:
        attemts -= 1
        if attemts < 5: print('  | ')
        if attemts < 4: print('  0 ')
        if attemts < 3: print(' /|\ ')
        if attemts < 2: print('  | ')
        if attemts < 1: print(' / \ ')
    if attemts == 0:
        print('You lose. Zagadannoe slovo {secret}')
        break


