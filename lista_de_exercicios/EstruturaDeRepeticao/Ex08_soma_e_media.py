# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
cont = 0

while cont < 5:
    num = int(input("Informe um numero inteiro"))
    soma += num
    cont += 1
media = soma / cont

print("A soma dos numeros é: {}".format(soma))
print("A média dos numeros é: {}".format(media))