# Faça um programa que receba dois números inteiros e
# gere os números inteiros que estão no intervalo compreendido por eles.

valor_inicial = int(input("Informe o valor inicial"))
valor_final = int(input("Informe o valor final"))

while valor_inicial < valor_final-1:
    print(valor_inicial + 1, end=" ")
    valor_inicial += 1
