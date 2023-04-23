# Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.


produto_um = float(input('Informe o primeiro valor: '))
produto_dois = float(input('Informe o segundo valor: '))
produto_tres = float(input('Informe o terceiro valor: '))

if produto_um == produto_dois and produto_um == produto_tres:
    print('Tanto faz, os tres tem o mesmo valor')
elif produto_um < produto_dois and produto_um < produto_tres:
    print('O produto um é mais barato')
elif produto_dois < produto_tres:
    print('O produto 2 é mais barato')
else:
    print('O produto 3 é mais barato')

