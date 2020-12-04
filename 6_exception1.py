"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
      while True:
        try:
          user_say = input('как дела?: ')
          if user_say == 'Хорошо':
            print('Отлично!')
          else:
            print('Прям {}? Давай еще раз попробуем'.format(user_say))
        except KeyboardInterrupt:
          print('Пока!')
          break

print(hello_user())
    