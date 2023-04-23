# Faça um Programa que leia três números e mostre-os em ordem decrescente.

primeiro_valor = int(input('Informe o primeiro valor: '))
segundo_valor = int(input('Informe o segundo valor: '))
terceiro_valor = int(input('Informe o terceiro valor: '))

if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
    if segundo_valor > terceiro_valor:
        print(primeiro_valor, segundo_valor, terceiro_valor)
    else:
        print(primeiro_valor,terceiro_valor,segundo_valor)
elif segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    if primeiro_valor > terceiro_valor:
        print(segundo_valor, primeiro_valor, terceiro_valor)
    else:
        print(segundo_valor,terceiro_valor,primeiro_valor)
elif terceiro_valor > primeiro_valor and terceiro_valor > segundo_valor:
    if primeiro_valor > segundo_valor:
        print(terceiro_valor, primeiro_valor, segundo_valor)
    else:
        print(terceiro_valor,segundo_valor,primeiro_valor)