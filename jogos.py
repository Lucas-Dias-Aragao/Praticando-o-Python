import forca
import adivinhacao

def escolhe_jogo():
    print("**********************************")
    print("*******Escolha o seu jogo!********")
    print("**********************************", end='\n\n')

    print("(1) - Forca (2) - Adivinhação", end='\n\n')

    selecione_jogo = int(input("O que deseja jogar? "))

    if(selecione_jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(selecione_jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()