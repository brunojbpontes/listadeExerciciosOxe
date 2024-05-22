valor = float(input("Insira um numéro: "))
soma = 0
media = 0
numeros = 0
while valor >= 0 :
    soma += valor
    numeros+=1
    valor = float(input("Insira um número: "))

media = soma/ numeros
print(f"A média é: {media:.2f}")
