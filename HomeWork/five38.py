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