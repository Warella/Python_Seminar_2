"""
Задача 10: На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""
print('Введите количество монет: ')
n = int(input())
score = 0
for i in range(n):
    coin = int(input())
    if coin == 1:
        score += 1
print(score if score < n/2 else n-score)
