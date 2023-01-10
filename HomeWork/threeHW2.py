# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
list_num=[randint(0,2) for i in range (randint(5,6))]
print (list_num)
multi=[]
length=len(list_num)
middle=length//2+length%2
#середина списка для четной и  нечетной длинны
for i in range(middle):
    multi.append(list_num[i]*list_num[length-1-i])
print(multi)    