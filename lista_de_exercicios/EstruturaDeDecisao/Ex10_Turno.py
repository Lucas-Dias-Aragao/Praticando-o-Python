# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
# V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.


print("Em qual turno você estuda? ")
print("M - matutino | V - vespertino | N - noturno")
resp = input("-> ").upper()

if resp == 'M':
    print("Bom dia!")
elif resp == 'V':
    print("Boa tarde!")
elif resp == 'N':
    print("Boa noite!")
else:
    print("Turno", resp, "inválido")