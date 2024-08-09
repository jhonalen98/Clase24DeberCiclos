# n = 10
# a, b = 0, 1
# contador = 0
# while contador < n:
#     print(a)
#     a, b = b, a + b
#     contador += 1

n = int(input("Ingrese la cantidad de numeros de la serie Fibonacci desea ver: "))
a, b = 0, 1
contador = 0
while contador < n:
    print(a)
    a, b = b, a + b
    contador += 1