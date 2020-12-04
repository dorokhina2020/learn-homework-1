"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Ем", "Как погода?": "Солнечно!", 'Чем занимаешься?': 'Программирую'}

def ask_user():
      while True:
        user_say = input('Пользователь: ')
        if user_say == 'Как дела?':
          print(questions_and_answers[user_say])
        elif user_say == "Что делаешь?":
          print(questions_and_answers[user_say])
        elif user_say == 'Как погода?':
          print(questions_and_answers[user_say])
        elif user_say == 'Чем занимаешься?':
          print(questions_and_answers[user_say])        
        else:
          print('Задай другой вопрос')

print(ask_user())
