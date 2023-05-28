# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))
status = 'Aprovado'

media = (nota_1 + nota_2) / 2

if media < 6:
    status = 'Reprovado'

print("Sua Média de aproveitamento é:", media)
    
if 9 <= media == 10:
    print("Conceito: 'A'-", status)
if 7.5 <= media < 9:
    print("Conceito: 'B'-",status)
if 6 <= media < 7.5:
    print("Conceito: 'C'-",status)
if 4 <= media < 6:
    print("Conceito: 'D'-",status)
if 0 <= media < 4:
    print("Conceito: 'E'-",status)
    
