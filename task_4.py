''' Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.'''

user_str = input('введите строку из нескольких слов, разделённых пробелами: ')

new_str = user_str.split()

for el in new_str:
    if len(el) > 10:
        print(el[:10])
    else:
        print(el)