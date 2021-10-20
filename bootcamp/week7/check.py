"""
1) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, 
с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник.
"""
from datetime import datetime

class Clock:
    def time_now(self):
        now = datetime.now().strftime('%H:%M:%S')
        return now
class Alarm:
    def on(self):
        print('Будильник включен')
    def off(self):
        print('Будильник выключен')
class AlarmClock(Clock, Alarm):
    def alarm(self):
        return f'Будильник включен'
obj = AlarmClock()
print(obj.time_now())
print(obj.alarm())



"""
2) Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, 
класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента 
по предметам.
"""
# class Student:
#     def __init__(self, name, last_name, group, grade):
#         self.name = name
#         self.last_name = last_name
#         self.group = group
#         self.grade = grade

#     def kpi(self):
#         num = 



"""
3) Напишите класс учеников Makers, который будет содержать 4 атрибута: 

- атрибут экземпляра name (имя студента)
- атрибут класса students_count (количество учеников)
- атрибут экземпляра класса language (язык, которому обучается студент)
- атрибут экземпляра класса kpi (оценка студента)

Также класс должен содержать следующие методы:

- метод, который будет создавать нового ученика, и при этом увеличивать количество студентов на 1.
- метод который будет выводит имя и язык, выбранный учеником.
- а также метод, который будет устанавливать оценку ученику.
"""
# class Makers:
#     students = dict()
#     students_count = 0

#     def __init__(self, name, language, kpi):
#         self.name = name
#         self.language = language
#         self.kpi = kpi

#     def new_student(self, name, students_count, language ):
#         students_count += 1
#         dict.update(self, name, language)
        
    
#     def info(self, name, language):
#         print(f' Name: {self.name}, language: {self.language}')
    
    # def kpi(self, kpi):
    #     students = students.(self.kpi)

# obj = Makers('John','Snow', 'Python')
# obj.new_student('Loui', 'Kim','JS')
# obj.info()


    





