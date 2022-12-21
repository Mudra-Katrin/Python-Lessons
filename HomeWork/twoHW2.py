# Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# n=int(input('Введите целое число: '))

# list_num=[]
# factorial = 1
# for i in range (2, n+2):
#     list_num.append(factorial)
#     factorial*=i
# print (list_num)

n=int(input('Введите целое число: '))

def Factorial(n:int):
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)
    # for num in range(2,n+1):
    #     listRes.append(factorial)
    #     factorial *= num
    # listRes.append(factorial)
    # return listRes
    
listRes = []
for i in range(1,n+1):
    listRes.append(Factorial(i))
print(listRes)