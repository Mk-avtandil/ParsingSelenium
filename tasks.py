# # 1
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.

# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.

# class Soldier():
#     def __init__(self):
#         self.gun = "AK-47"

#     def shot(self):
#         print('тиги-тигитиш')

#     class Guns:
#         def __init__(self):
#             self.barage_of_bullets = 30
#             self.total_bullets = 150
#         def reload(self):
#             if self.total_bullets > 0:
#                 if self.total_bullets >= 30:
#                     self.total_bullets -= 30
#                     self.barage_of_bullets = 30
#                     print(f"You have succesfully reloaded, apart from the bullets at ur barage u have {self.total_bullets} bullets left")
#                 else:
#                     self.barage_of_bullets = self.total_bullets
#                     self.total_bullets = 0
#                     print(f"WARNING!, these {self.barage_of_bullets} bullets are your last ones")
#             else:
#                 print("U have wasted all ur bullets")
#         def shot(self,shots):
#             alert = f"U have shot {shots} times" if self.barage_of_bullets >= shots else "U dont have this much bullets at ur barage, u have to reload"
#             self.barage_of_bullets -= shots if self.barage_of_bullets >= shots else self.barage_of_bullets
#             print(alert)
           

# class Act_of_Shooting(Soldier.Guns):
#     def __init__(self):
#         super().__init__()

# ob1 = Act_of_Shooting()
# ob1.shot(30)
# ob1.reload()

# ==================================================================

# # 2 
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.

# from random import shuffle

# fornitures = [{'name' : 'bed','area' : 4 },{'name' :'living room' , 'area' : 2},{'name': 'table' , 'area' : 1.5} ]

# class Home:
#     def __init__(self, home_type, total_area):
#         self.home_type = home_type
#         self.total_area = total_area
#         self.list_of_fornitures = []

#     def __str__(self):
#         occupied_area = sum([x['area'] for x in self.list_of_fornitures])
#         return f"The home type is {self.home_type}, the total area is {self.total_area}, the free area is {self.total_area-occupied_area}"

# home1 = Home('futuristic',50)

# [home1.list_of_fornitures.append(i) for i in fornitures]
# print(home1.list_of_fornitures)

# ==================================================================

# # 3 
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

# class Student:
#     def __init__(self, name, age, major):
#         self.name = name
#         self.age = age
#         self.major = major

#     def __str__(self):
#         return str(self.__dict__)

# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# print(Johnny)

# ==================================================================

# # 4 
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567) 
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3


# def dollarize(n):
#     return '${:,.2f}'.format(n)

# print(dollarize(-123456.7801))

# import moneyfmt

# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash)
# cash.update(100000.4567)
# print(cash)
# cash.update(-0.3)
# print(cash)
# print(cash.repr())
