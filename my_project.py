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