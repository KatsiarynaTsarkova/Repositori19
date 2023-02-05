import random

#Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все 
# оценки заносятся в таблицу. Каждой группе отведена своя строка. 
# Определите группу с наилучшим средним баллом.

group = 5
count = 20
numbers = [0] * group
for index in range(len(numbers)):
    numbers[index] = [random.randint(1, 5) for _ in range(count)]
 
 
for el in numbers:
    print(el)
    
    
numbers_in_group = []
for i in range(group):
    numbers_in_group.append(sum(numbers[i]) / count)
print(numbers_in_group)  

max = 0
max_i = 0
for i in range(len(numbers_in_group)):
    if numbers_in_group[i] > max:
        max = numbers_in_group[i]
        max_i = i + 1
print(f' группа с максимальным средним баллом: {max_i} - {max}')