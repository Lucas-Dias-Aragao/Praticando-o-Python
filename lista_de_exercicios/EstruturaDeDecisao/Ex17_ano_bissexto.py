# Faça um Programa que peça um número correspondente a 
# um determinado ano e em seguida informe se este ano é ou não bissexto

ano = int(input("Informe um ano"))

if ano % 4 == 0:
    print(ano,"é bissexto")
else:
    print(ano,"não é bissexto")
