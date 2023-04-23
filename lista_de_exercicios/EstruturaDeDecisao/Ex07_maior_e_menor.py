# Faça um Programa que leia três números e mostre o maior e o menor deles.

primeiro_valor = int(input('Informe o primeiro valor: '))
segundo_valor = int(input('Informe o segundo valor: '))
terceiro_valor = int(input('Informe o terceiro valor: '))

if primeiro_valor == segundo_valor and primeiro_valor == terceiro_valor:
    print('Os tres valores são iguais a',primeiro_valor)
else:
    if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
       print('O maior valor é:', primeiro_valor)
    elif segundo_valor > terceiro_valor:
        print('O maior valor é:',segundo_valor)
    else:
        print('Maior valor é:', terceiro_valor)

    if primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
        print('O menor valor é:', primeiro_valor)
    elif segundo_valor < terceiro_valor:
        print('O menor valor é:',segundo_valor)
    else:
        print('Menor valor é:', terceiro_valor)