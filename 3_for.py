"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
total_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '5б', 'scores': [2,2,5,5,3]},
    {'school_class': '7б', 'scores': [4,4,3,5,5]},
    {'school_class': '9а', 'scores': [3,3,5,5,4]},
]

for clas in total_scores:
  clas['avr_score'] = sum(clas['scores']) / len(clas['scores'])
  print(clas)
  
score_sum = 0
for clas in total_scores:
  score_sum += clas['avr_score']

print(f'Средний балл по всей школе: {score_sum / len(total_scores)}')

for clas in total_scores:
  clas_no = clas['school_class']
  avr_score = clas['avr_score']
  print(f'Средний балл по классу {clas_no}: {avr_score}')