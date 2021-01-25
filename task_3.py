'''Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.'''

mounth_list = ['зима', 'весна', 'лето', 'осень']
mounth_dict = {
    'зиме': [1, 2, 12],
    'весне': [3, 4, 5],
    'лету': [6, 7, 8],
    'осени': [9, 10 ,11]
}

user_month = int(input('введите месяц в виде целого числа от 1 до 12: '))

#через list
if user_month == 1 or user_month == 2 or user_month == 12:
    print(f'время года: {mounth_list[0]}')
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(f'время года: {mounth_list[1]}')
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(f'время года: {mounth_list[2]}')
elif user_month == 9 or user_month == 10 or user_month == 11:
    print(f'время года: {mounth_list[3]}')
else:
    print('вы ввели неправильное значение')

#через dict
for key, value in mounth_dict.items():
    for el in value:
        if user_month == el:
            print(f'этот месяц относится к {key}')

#3
