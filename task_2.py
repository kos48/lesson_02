'''Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().'''

user_list = []

while True:
    x = input('добавим эл-нт в список? Если нет, введите "no":')
    if x == 'no':
        break
    else:
        user_list.append(input('Введите эл-нт: '))

print(f' это ваш список {user_list}')

new_list = user_list

for i in range(1, len(new_list), 2):
    """можете объяснить на сл уроке эту конструкцию!"""
    new_list[i - 1], new_list[i] = new_list[i], new_list[i - 1]#!!!не понял эту конструкцию!!!

print(f'измененный список {new_list}')

#2
