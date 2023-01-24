# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.
# print('Введите последовательность натуральных чисел через пробел')
# data = list(map(int,input().split()))
# for i in range(len(data)-1,-1,-1):
#     if i > 0:
#         number = data[i]
#         n = data[i-1]
#         if number - 1 != n:
#             x = number-1
#             data.append(x)
# print(f'Нужное нам чило = {x}')
# 2ВАРИАНТ
# list1 = [1, 2, 3, 4, 6, 7]

# def find(list):
#     for i in list:
#         if list[i] -1 != list[i-1]:
#             return list[i] -1
# print(find(list1))
# это первая задача


# 36. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# data = [1, 5, 2, 3, 4, 6, 1, 7]
# list = []
# m = 0
# for i in range(len(data)):
#     if data[i] > m:
#         list.append(data[i])
#         m = data[i]
# print(list)

# 37. Напишите программу, удаляющую из текста все слова, содержащие "абв".
line = 'фывабвйцу кенабвджэ, ячсабвнгш, йцукенгвба'
while ',' in line or '.' in line or ';' in line or ',' in line:
    line = line.replace(',', '')
print(line)

arr = line.split()
print(arr)

i = 0
for word in arr:
    if 'абв' in word:
        arr.pop(i)
    i += 1
print(arr)
#   ВАРИАНТ2
# line = 'фывабвйцу кенабkвджэ, ячсабвнгш, йцукенгвба'
# while ',' in line or '.' in line or ';' in line or ',' in line:
#     line = line.replace(',', '')
# print(line)

# arr = line.split()
# print(arr)

# arr2 = []
# for word in arr:
#     if 'абв' not in word:
#         arr2.append(word)
# print(arr2)


