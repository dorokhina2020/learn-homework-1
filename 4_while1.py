"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""



def hello_user():
      while True:
        user_say = input('как дела?: ')
        if user_say == 'Хорошо':
          print('Отлично!')
          break
        else:
          print('Прям {}? Давай еще раз попробуем'.format(user_say))

print(hello_user())

