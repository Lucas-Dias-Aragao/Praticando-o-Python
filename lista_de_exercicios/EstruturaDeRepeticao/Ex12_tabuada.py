# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. 


mult = int(input("Deseja saber qual tabuada?: "))
cont = 1

while mult > 0 or mult < 11:
    if mult == 0:
        print("Programa encerrado")
        break
    elif mult < 1 or mult > 10:
        print("Informe um número entre 1 e 10")
    else:
        while cont <= 10:
            print("{} X {} = {}".format(mult, cont, mult*cont))
            cont += 1
    print("Tecle 0 para sair")
    mult = int(input("Deseja saber qual tabuada?: "))
