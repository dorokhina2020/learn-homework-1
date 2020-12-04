

while True:
    user_say = input('как дела?: ')
    if user_say == 'Хорошо':
        print('Отлично!')
        break
    else:
        print('Прям {}? А может все-таки Хорошо?'.format(user_say))





x = 10
while True:
    x -= 1
    if x < 0:
        break
    print (x)
print('Все!')

'упрощенная конструкция'

x = 9
while x >= 0:
    print(x)
    x -= 1 
print('Все!')

while True:
    user_say = input('Скажи что-нибудь: ')
    if user_say == 'Пока':
        print('Ну пока')
        break
    else:
        print('Сам ты {}'.format(user_say))
