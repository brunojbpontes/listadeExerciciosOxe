n = int((input("Digite um número n: ")))

fatorial = 1

while n!=0 :
    fatorial=fatorial*n
    n=n-1

print(f"O fatorial de n é {fatorial}")