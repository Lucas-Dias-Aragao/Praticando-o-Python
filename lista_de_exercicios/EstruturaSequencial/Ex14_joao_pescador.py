# faça um programa que leia a variável peso (peso de peixes) e calcule
# o excesso (acima de 50kg). Gravar na variável excesso a quantidade de
# quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.


print("------- CALCULADORA DE MULTA -------\n")
print("# Peso máx. permitido: 50 Kg\n")

qtd_pescada = float(input("Quanto tu pescou, irmão? "))
excesso = qtd_pescada - 50
valor_a_pagar_por_kg = 4.00
multa = 0

if excesso > 0:
    multa = valor_a_pagar_por_kg * excesso
    print(f"Você pescou {excesso} kg a mais, vai ter que pagar R${multa: .2f} reais de multa. Fica ligeiro, pô")
else:
    print("Boaa, sem multa hoje!!")