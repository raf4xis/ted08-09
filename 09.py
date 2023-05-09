numeros = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("Números na ordem inversa:")
for i in range(19, -1, -1):
    print(numeros[i])


#Questão 1