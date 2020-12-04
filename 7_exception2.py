"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    try:
      price = abs(float(price))
      discount = abs(float(discount))
      max_discount = abs(int(max_discount))
      if discount >= max_discount:
        return price   
      else: 
        return price - price * discount / 100    
    except  (ValueError, TypeError):
      print('Что-то пошло не так')


print(discounted(100, 100))
print(discounted(100, "3"))
print(discounted("100", "4.5"))
print(discounted("five", 5))
print(discounted("сто", "десять"))
print(discounted(100.0, 5, "10"))


'Вопрос - не могу понять, почему выводится None после сообщения о перехваченной ошибке'