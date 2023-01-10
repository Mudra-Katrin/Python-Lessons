#Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.
import os
os.system('cls')# это очистка экрана
import datetime
n = int(input("введите число: "))
rand = datetime.datetime.now().microsecond%(n+1)
print(rand)

# import datetime
# n = int(input())
# rand = datetime.datetime.now().microsecond%(n+1)
# print(rand)