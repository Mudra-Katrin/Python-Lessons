# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.""
n=int(input("d:"))
list_num=[i for i in range (-n, n+1)]
print (list_num) #создает список от -N до N
file=open("File.txt" , "r")
a=file.readlines()
# for a in file:
# print (int(a))-вывести значения из file в формате int,потом перевести в список

print (a)
for i in range (len(a)):
    a[i]=int(a[i].strip())
print(a)
multi = 1    
for i in range (len(a)):
    multi*=list_num[a[i]]
print(multi)
# 
# в 4 вы получили в "a" список со строками, к этому списку сначала нужно
# использовать strip ко всем элементам, чтобы убрать \n, потом int чтобы
# перевести элементы в числа.
# Тогда в "a" у вас будут индексы, и по ним брать элементы из list_num