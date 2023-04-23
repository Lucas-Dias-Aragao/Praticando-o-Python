#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Informe um valor: '))

if valor < 0:
    print(valor, 'é um número negativo')
else:
    print(valor, 'é um número positivo')