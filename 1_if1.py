"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
name = input('Введите ваш возраст')
age = int(name)
print(age)

def main(age):
        if age <= 6:
          return 'Ходит в детский сад'
        elif 7 <= age <= 17:
          return 'Учится в школе'
        elif 18 <= age <= 22:
          return 'Учится в ВУЗе'
        else:
          return 'Работает'

print(main(age))
