# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# A - o produto do dobro do primeiro com metade do segundo .
# B - a soma do triplo do primeiro com o terceiro.
# C - o terceiro elevado ao cubo.

primeiro_numero = int(input("Informe o primeiro valor: "))
segundo_numero = int(input("Informe o segundo valor: "))
numero_real = float(input("Informe um número real: "))

dobro_do_primeiro = primeiro_numero * 2
metade_do_segundo = segundo_numero / 2
produto_a = dobro_do_primeiro * metade_do_segundo
print("O produto do dobro do primeiro com metade do segundo é {}".format(produto_a))

triplo_do_primeiro = primeiro_numero * 3
soma_b = triplo_do_primeiro + numero_real
print("A soma do triplo do primeiro com o terceiro é {}".format(soma_b))

terceiro_ao_cubo = numero_real ** 3
print("O terceiro elevado ao cubo é {}".format(terceiro_ao_cubo))

