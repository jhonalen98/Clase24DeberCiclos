# numero = 5
# factorial = 1
# for i in range(1, numero + 1):
#     factorial *= i
# print(f"El factorial de {numero} es:", factorial)

numero = int(input("Ingrese el numero para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es:", factorial)