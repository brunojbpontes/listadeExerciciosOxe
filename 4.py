texto = input("Digite uma string: ")
vogais = "aeiouAEIOU"
contador = sum(1 for char in texto if char in vogais)
print(f"A string possui {contador} vogais.")