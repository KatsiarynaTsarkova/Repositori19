import random

#Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по 
# сентябрь за прошлый год. Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца.
# Выведите их даты.
def period_month(temp_month, period, month ):
    max_temp = 0
    min_temp = 40
    day_maxtemp = 1
    day_mintamp = 1
    
    for i in range(len(temp_month)- period + 1):
        temp_in_period = temp_month [i:i + period]
        print(f'{i + 1} - {i + period}. {temp_in_period}')
        sum_temp = sum(temp_in_period)
        if sum_temp > max_temp:
           max_temp =  sum_temp
           day_maxtemp = i
        else:
           sum_temp < min_temp
           min_temp =  sum_temp
           day_mintamp = i
    print(f'максимальная температура с {day_maxtemp + 1} по {day_maxtemp + period} {month}')
    print(f'минимальная температура с {day_mintamp + 1} по {day_mintamp + period} {month}')  


rows = 5
temp_month = [0] * rows
for index in range(len(temp_month)):
    temp_month[index] = [random.randint(16, 30) for _ in range(31)]
    
n = int(input('Введите номер соответствующий  номеру месяца с мая по сентябрь:'))

for i in range(len(temp_month)): 
    if n == 1:  
        period_month(temp_month[0], 7, 'май')
    elif  n == 2:  
        period_month(temp_month[1], 7, 'июнь') 
    elif  n == 3:  
        period_month(temp_month[2], 7, 'июль') 
    elif  n == 4:  
        period_month(temp_month[3], 7, 'август') 
    elif  n == 5:  
        period_month(temp_month[4], 7, 'сентябрь')            
        
 
        
        
print(f'все температуры {temp_month}')