VET = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    VET.append(num)

repetidos = set([x for x in VET if VET.count(x) > 1])

if repetidos:
    print("Números repetidos encontrados nas posições:")
    for num in repetidos:
        posicoes = [i for i, x in enumerate(VET) if x == num]
        print(f"{num}: {posicoes}")
else:
    print("Não há números repetidos no vetor.")


#Questão 2