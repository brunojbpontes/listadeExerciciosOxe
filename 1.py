n1 = int(input("Digite um Número Inicial: "))
n2 = int(input("Digite um Número Final: "))
n1Inicial = n1
while n1<n2 :
    if n1%2==1 :
        print(n1)

    n1+=1

print(f"Esses são todos os números ímpares entre {n1Inicial} e {n2}.")
