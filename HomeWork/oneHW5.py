# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# AB = √(xb - xa)2 + (yb - ya)2
Ax = int(input('Введите значения х точки А:')) 
Ay = int(input('Введите значения y точки А:')) 
Bx = int(input('Введите значения х точки B:')) 
By = int(input('Введите значения y точки B:'))
print (((Bx-Ax)**2+(By-Ay)**2)**0.5)