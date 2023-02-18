"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str_one, str_two):
    if isinstance(str_one, str) != True or isinstance(str_two, str) != True:
        return '0'
    elif str_one == str_two:
        return '1'
    elif str_one > str_two:
        return '2'
    elif str_two == 'learn':
        return '3'
    else:
        return 'Не подходят'
  
    
if __name__ == "__main__":
    str_one = input('Введите первую строку: ',)
    str_two = input('Введите вторую строку: ',) 
    print(main(str_one, str_two))
    print(main(11, 11))
    print(main(11, '11'))
    print(main('11', 11))
    print(main('11', '11'))

