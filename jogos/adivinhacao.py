import random

def jogar():
    print("**********************************")
    print("Bem-vindo ao jogo de adivinhação!!")
    print("**********************************", end='\n\n')

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0
    pontos = 1000

    print("Defina o nível do jogo!")
    print("1 - Fácil  2 - Médio  3 - Difícil", end='\n\n')
    nivel_jogo = int(input("Digite o nível desejado: "))

    if(nivel_jogo == 1):
        total_de_tentativas = 20
    elif(nivel_jogo == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1,total_de_tentativas + 1):
        print("*** Tentativa {} de {} ***".format(rodada, total_de_tentativas))
        palpite = int(input("Digite o seu palpite entre 1 e 100: "))
        print("Você digitou: ", palpite)

        if(palpite < 1 or palpite > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        palpite_certo = palpite == numero_secreto
        palpite_menor = palpite < numero_secreto
        palpite_maior = palpite > numero_secreto

        if(palpite_certo):
            print("Você acertou!!")
            break
        else:
            if(palpite_maior):
                print("Seu palpite é maior que o numero secreto")


            elif(palpite_menor):
                print("Seu palpite é menor que o número secreto")
        pontos_perdidos = abs(numero_secreto - palpite)
        pontos = pontos - pontos_perdidos



    print("Fim de Jogo! Você fez {} pontos".format(pontos))

if(__name__ == "__main__"):
    jogar()
