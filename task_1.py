'''Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.'''

my_list = [123, 'abc', True, 123.456, {'asd': 123, 'fgh': 'qwerty'}, ['sdf', 45], ('zxc', 123)]

for el in my_list:
    print(type(el))

