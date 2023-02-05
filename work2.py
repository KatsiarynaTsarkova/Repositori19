import random
#Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите, 
# сумма элементов каких строк превосходит сумму главной диагонали матрицы.
rows = 5
columns = 5
numbers = [0] * rows
for index in range(len(numbers)):
    numbers[index] = [random.randint(1, 9) for _ in range(columns)]
 
for el in numbers:
    print(el)

sum_s = []
for i in range(rows):
    sum_s.append(sum(numbers [i]))
print(f' {sum_s} ')            

 
s_d = []    
for i in range(rows):
    for j in range(columns):
        if [i] == [j]:
            s_d.append(numbers [i] [j])
print(s_d)             
sum_d = 0            
for i in range(len(s_d)):   
    sum_d += s_d [i]        
print(sum_d) 

sum_i = []
for i in range(len(sum_s)):
    if sum_s [i] > sum_d:
      sum_i.append(i + 1)
print(sum_i)       
           