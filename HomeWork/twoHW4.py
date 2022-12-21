# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.""
n=int(input("d:"))
list_num=[i for i in range (-n, n+1)]
print (list_num)
file=open("File.txt, "r"")
a=file.readlines()
print (a)
multi=1
for i in range (len(a)):
    multi+=list_num[a[i]]
print(multi)
list_num=list (map(str.strip,a))    
print(list_num)
