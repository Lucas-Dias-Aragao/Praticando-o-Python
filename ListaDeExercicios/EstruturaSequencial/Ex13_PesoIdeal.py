
sexo = input("Se for mulher digite 'm', se for homem digite 'h': ")
altura_recebida = input("Informe sua altura: ")
altura = float(altura_recebida.replace(",","."))


peso_ideal = 0

if sexo == 'm':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = (72.7 * altura) - 58

print(f"Seu peso ideal é {peso_ideal: .3f} Kg")