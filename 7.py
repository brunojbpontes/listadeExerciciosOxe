
num = input("Digite um número: ")

soma_digitos = 0

for digito in num:
    soma_digitos += int(digito)

print(f"A soma de todos os dígitos é: {soma_digitos}")
