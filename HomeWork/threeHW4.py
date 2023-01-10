# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
n=int(input('Ввведите целое число:'))

def dec_to_bin(num,reslt = ""):
    if num ==0:
        return reslt[::-1]
    reslt=reslt+str(num%2)
    return dec_to_bin(num//2,reslt)
print(dec_to_bin(n))
print (bin(n)[2:])#встроенная функция