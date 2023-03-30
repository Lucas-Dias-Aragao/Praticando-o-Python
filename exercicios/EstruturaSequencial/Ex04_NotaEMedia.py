
notas = []
notas_necessarias = 4


for nota in range (0, notas_necessarias):
    nota = int(input("Informe a {}ª nota: ".format(nota+1)))
    notas.append(nota)

soma = sum(notas)
media = soma / len(notas)

print("A média do aluno é: {}".format(media))

if media >= 6:
    print("*** APROVADO ***")
else:
    print("** REPROVADO :( **")


