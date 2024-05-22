n = int(input("Digite um Número: "))

Start = int (0)

while Start <= n :

    if Start % 2 == 0 :
        print(f"{Start}")
        Start = Start+1
    else :
        Start = Start+1

print (f"Esses são todos os números pares entre 0 e {n}")