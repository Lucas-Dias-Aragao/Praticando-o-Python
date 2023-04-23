#Faça um Programa que peça dois números e imprima o maior deles.

primeiro_numero = int(input('Informe o primeiro número: '))
segundo_numero = int(input('Informe o segundo número: '))

if primeiro_numero > segundo_numero:
    print('Maior número:', primeiro_numero)
else:
    print('Maior número:', segundo_numero)