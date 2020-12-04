def cut_cake(people):
    try:
        part = 1 / people
        print(f'Каждый человек получит {part} пирога')
    except (TypeError, ZeroDivisionError):
        print('Проверь ввод! Я умею делить только на число отличное от 0')

cut_cake(0)