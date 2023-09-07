# Faça um programa que leia 5 números e informe o maior número.

maior = 0
num = 0
cont = 1

maior = num
while cont <= 5:
    num = int(input("Informe um numero inteiro"))
    if num > maior:
        maior = num
    cont += 1
print("O maior numero é: {}".format(maior))