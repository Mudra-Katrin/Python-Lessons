# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных
# индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
def fib (n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)
list_fib=[]
for e in range(1,9):
    list_fib.append(fib(e))
print(list) 

def otrits_fib(n):
    otrits_list=[0,1]
    for i in range(n-1):
        otrits_list.append(otrits_list[-2]-otrits_list[-1])
    return otrits_list
print(otrits_fib(8))    
print(otrits_fib(8)[::-1]+list_fib)    