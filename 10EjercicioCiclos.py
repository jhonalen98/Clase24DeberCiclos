# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
    
n = int(input("Ingrese la cantidad de pisos que desea ver en la piramide: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))