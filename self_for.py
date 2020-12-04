for x in 1, 2, 3, 4:
    print(x ** 2)

for number in range(3):
    print(f'Привет, мир {number}!')

example_string = 'я изучаю язык python'
for word in example_string.split():
    print(f'Длина слова "{word}": {len(word)}')


students_scores = [1, 21, 19, 6, 5]
#print(f'Средняя оценка: {sum(students_scores) / len(students_scores)}')  
scores_sum = 0
for score in students_scores:
    scores_sum += score
    print(scores_sum)

print(f'Средняя оценка: {scores_sum / len(students_scores)}')  
