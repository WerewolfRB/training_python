# name = ['Таню', 'Диму', 'Руслана']
# print(f'Хочу пригласить на обед {name[0]}, {name[1]}, {name[2]}')
# liv_gost = name.pop(1)
# print (f'Увы гость {liv_gost} прийти не сможет')
# name.insert(1, 'Алена')
# print (f'А вот {name[1]} прийти сможет')
# print(f'Приглашаю на обед {name[0]}, {name[1]}, {name[2]}')
# name.append('Егор')
# name.append('Данил')
# print(f'Я сожалею о том что вы не сможите прийти {name.pop(-1)}')
# print(f'Я сожалею о том что вы не сможите прийти {name.pop(-1)}')
# print(f'Я сожалею о том что вы не сможите прийти {name.pop(-1)}')
# print(f'Предложение остается в силе можите прийти {name.pop(-1)}')
# print(f'Предложение остается в силе можите прийти {name.pop(-1)}')
# print(name)
from symtable import Function
from threading import activeCount
from turtledemo.sorting_animate import enable_keys

#==================================#

# list_cities = ['Samara', 'Maikop', 'Moskva', 'SPB', 'Krim']
# print(list_cities)
# sort_cities = sorted(list_cities)
# print(sort_cities)
# revers_sorted_cities = sorted(list_cities, reverse=True)
# print(revers_sorted_cities)
# list_cities.reverse()
# print(list_cities)
# print(len(list_cities))

# inp = input('Введте значения, если их несколько то через пробел:')
# list_index = inp.split(" ")
# print(list_index)
# choice = input('Ты хочешь посчитать количество значение (ДА/НЕТ)')
# if choice == "ДА":
#     print(f'Количество элиментов в списке: {len(list_index)}')

#==============================================#

# for values in range(1,21):
#     print (values)

# list = []
# for values in range(1, 1000001):
#     list.append(values)
# print(list)
# print(sum(list))
# print(min(list))
# print(max(list))


# list = []
# for values in range(1, 21, 2):
#     list.append(values)
#     print(f'найденно нечетное число списка: {values}')
# print(list)

# list = []
# for values in range(3, 31):
#     if values % 3 == 0:
#         list.append(values)
#         print(values)
#     else:
#         continue
# print(list)

# list = [i for i in range(3,31,3)]
# print(list)

# list = []
# for values in range(1, 11):
#     list.append(values**3)
# print(list)

# list = [values**3 for values in range(1,11)]
# print(list)

#============================================#

# list_kor = ('Yorkshire pudding', 'Roast beef', 'A toad in a hole', 'Christmas pudding', 'Cheddar')
# for dishes in list_kor:
#     print(dishes)
# list_kor = ('Scone', 'Roast beef', 'A toad in a hole', 'Christmas pudding', 'Chicken tikka masala')
# for ferst_dishes in list_kor:
#     print(ferst_dishes)

#===============================================#

# alien_color = 'yellow'
#
# if alien_color == 'green':
#     print('вы только что заработали 5 очков')
# elif alien_color == 'yellow':
#     print('вы только что получили 10 очков')
# elif alien_color == 'red':
#     print('вы только что получили 15 очков')
# else:
#     print('вы ничего не получаете')

# age = int(input('Введите ваш возраст:'))
# if age < 2:
#     print('Вы младенец')
# elif age >= 2 and age < 4:
#     print('Вы малыш')
# elif age >=4 and age < 13:
#     print('Вы ребенок')
# elif age >=13 and age < 20:
#     print('Вы подросток')
# elif age >=20 and age < 65:
#     print('Вы взрослый')
# else: print('Вы пожилой человек')

# list = ['Яблоко', 'Апельсин', 'Ананас']
# favorite_fruit = str(input('Какой у тебя любимый фрукт '))
# if favorite_fruit.title() in list:
#     print(f'You really like {favorite_fruit.title()}')

#=============================================#

# name_list = []
# name = input('What is your name: ')
# name_list.append(name)
#==========

# new_name = ['Yrei', 'Vasia', 'Admin', 'Masha', 'Dima']
# current_user = ['Natasha', 'Tania', 'Dima', 'Ruslan', 'Artem']
#
# for new_names in new_name:
#     for current_users in current_user:
#         if new_names.lower() == current_users.lower():
#             new_name.remove(new_names)
#             print(f'Come up with another name for your ak {new_names}\n')
#
# if new_name:
#     for name_greeting in new_name:
#         if name_greeting == 'Admin':
#             print(f'Hello {name_greeting}, would you like to see a status report?')
#         else: print(f'Hello {name_greeting},thank you for logging in again')
# else: print('We need to find some users!')

#======

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for numbers in list:
#     if numbers == 1:
#         print(str(numbers)+"st")
#     elif numbers == 2:
#         print(str(numbers)+"nd")
#     elif numbers == 3:
#         print(str(numbers) + "rd")
#     else:
#         print(str(numbers)+"th")

#================= Dictionary ====================

# Best_friend = {
#     'name': 'James',
#     'age': 22,
#     'city': 'Samara',
# }
# # print(Best_friend['name'])
#
# for key, values in Best_friend.items():
#     print (key, values)

# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }
#
# programmist = ['Dima','James','Tania','Sarah']
#
# for language in set(favorite_languages.values()):
#     if 'python' in language:
#         print(f'My favorite language is {language}')
#     else:
#         print(f"These languages are not bad either {language}")
#
# for name in programmist:
#     if name.lower() not in favorite_languages.keys():
#         print (f'Какого черта вы не прошли {name}')

# Ali = {
#     'Surname': 'Alinize',
#     'Middle_name': 'Djazov',
#     'City': 'Kanzas',
# }
#
# Djo = {
#     'Surname': 'Djozovich',
#     'Middle_name': 'Diamon',
#     'City': 'Los_Andjeles',
# }
#
# Dio = {
#     'Surname': 'Djozef',
#     'Middle_name': 'Kakoi-to',
#     'City': 'Los_Pingvinis',
# }
#
# people = [Ali, Djo, Dio]
#
# for name in people:
#     print ('\n')
#     for kon,bot in name.items():
#         print(f'{kon}: {bot}')

# Первый словарь: животные и их категории
# animals1 = {
#     "Dog": "Mammal",
#     "Eagle": "Bird",
#     "Shark": "Fish"
# }
#
# Второй словарь: животные и их ареал обитания
# animals2 = {
#     "Dog": "Land",
#     "Eagle": "Air",
#     "Shark": "Water"
# }
#
# # Список: только названия животных
# animal_list = ["Dog", "Eagle", "Shark", "Cat"]
#
# for anivamls, cotegoria in animals1.items():
#     print(f"Собака {anivamls} входит в котегорию {cotegoria}")

# favorite_places = {
#     'Александр': {
#         'Место': 'Горы',
#         'Хобби': 'Рисовать'
#     },
#     'Таня':{
#         'Место':'Море',
#         'Хобби':'Путешествовать'
#     },
#     'Дима':{
#         'Место':'Дом',
#         'Хобби':'Программировать'
#     }
# }
#
# for name, hobb in favorite_places.items():
#     mesto = hobb['Место']
#     hobbs = hobb['Хобби']
#     print(f'Это {name} он любит {mesto} и его любимое хобби {hobbs}')

# ===============================Vvod

# car = input('Какую машину ты взял? ')
# print(f'Ты взял {car}')

# stol = input('Какой номер стола вы бы хотели взять ')
# if int(stol) < 8:
#     print("Отлично, мы забронировали стол номер "+stol)
# else:
#     print("К сожалению стол номер "+stol+" занят")

# chislo = input("Введите число кратное 10 ")
# if int(chislo) % 10 == 0:
#     print('Ваше число кратно 10')
# else:
#     print("Ваше число не кратно 10")

# ==============================While

# prompt = "Введите дополнение к пицце"
# prompt += "Введите 'Выйти' если хотите закончить ввод "
#
# activ = True
# while activ:
#     dop = input(prompt)
#     if dop == "Выйти":
#         activ = False
#     else:
#         print(f"{dop.title()} Добавленно в ваш заказ")

# print(f"Количество используемых потоков {activeCount()}")
# print(activeCount())

# prompt = input("Введите ваш возраст: ")
# if int(prompt) <= 3:
#     print("Для вас билет бесплатный")
# elif int(prompt) > 3 and int(prompt) < 12:
#     print("Для вас билет будет стоить 10$")
# else:
#     print("Для вас билет будет стоить 15$")


# while True:
#     prompt = input('Введите возраст каждого кто пойдет в кино (если хотите просто выйти напишите "выход"): ')
#
#     if prompt.lower() == "выход":
#         print('Спасибо что воспользовались нашими услугами')
#         break
#
#     if not prompt.isdigit():
#         print('Введите пожалуйста коректное число')
#         continue
#
#     if int(prompt) <= 3:
#         print("Для вас билет бесплатный")
#     elif int(prompt) > 3 and int(prompt) < 12:
#         print("Для вас билет будет стоить 10$")
#     else:
#         print("Для вас билет будет стоить 15$")

# active = True
# while active:
#     prompt = input('Введите возраст каждого кто пойдет в кино (если хотите просто выйти напишите "выход"): ')
#
#     if prompt.lower() == "выход":
#         print('Спасибо что воспользовались нашими услугами')
#         active = False
#         break
#
#     if not prompt.isdigit():
#         print('Введите пожалуйста коректное число')
#         continue
#
#     if int(prompt) <= 3:
#         print("Для вас билет бесплатный")
#     elif int(prompt) > 3 and int(prompt) < 12:
#         print("Для вас билет будет стоить 10$")
#     else:
#         print("Для вас билет будет стоить 15$")

# ==================================Function

# def favorite_book(favorite):
#     print (f'Моя любимая книга {favorite.title()}')
#
# favorite_book("ведьмак")


# def city_country(city, strana):
#     """Возвращает город и страну"""
#     per = f"{strana} {city}"
#     return per.title()
#
# mesto = city_country("Майкоп", "Россия")
# print(mesto)

# def make_album(nazvanie, ispolnitel, dorohki=''):
#     slov = {'nazvanie': nazvanie, 'ispolnitel': ispolnitel}
#     if dorohki:
#         slov['dorohki'] = dorohki
#     return slov
#
#
#
# while True:
#     print("Добрый день, ввеите своб любимую групппу и испольнителя, можите по желанию ввести кол-во джорожек:")
#     print("Чтобы выйти из процесса заполнения, нажмите 'q'")
#     nazvanie = input("Песня> ")
#     if nazvanie == 'q':
#         break
#     ispolnitel = input("Испольнитель> ")
#     if ispolnitel == 'q':
#         break
#     dorohki = input("Дорошки> ")
#     if dorohki == 'q':
#         break
#
#     pesenki = make_album(nazvanie, ispolnitel, dorohki)
#     print(pesenki)

# def build_person(first_name, last_name, ):
#     """Возвращает словарь с информацией о человеке."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# def show_messages(letmi):
#     """Обычное сообщение"""
#     for letmies in letmi:
#         print (f"Привет фрик {letmies}")
#
# spisochek=["Krutoi", "Echo kriche"]
# show_messages(spisochek)




# def show_massages(redact_masseges, no_redact_masseges):
#     while redact_masseges:
#         masseges = redact_masseges.pop()
#         print(f"Перенесли {masseges}")
#         no_redact_masseges.append(masseges)
#     print(no_redact_masseges)
#     print(redact_masseges)
#
# corentli = ['Какой то мужик', 'Пубертатная язва']
# corentli_one = []
# show_massages(redact_masseges=corentli, no_redact_masseges=corentli_one)



def show_messages (corentli_spisok):
    for spisok in corentli_spisok:
        print(f"Прикольная штука {spisok}")

def sent_messages (redact, no_redact):
    while redact:
        messages = redact.pop()
        print(f'Перенесли элимент: {messages}')
        no_redact.append(messages)
    show_messages(no_redact)
    print(no_redact)
    print(redact)

spiis = ['Крутой', 'Еще круче']
spiisok = []

sent_messages(redact=spiis, no_redact=spiisok)