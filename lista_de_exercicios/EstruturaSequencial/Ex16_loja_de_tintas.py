# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

print("-- Lucão Tintas ---\n")

area = float(input("Área do local (m²): "))

tinta_necessaria = area / 3
latas_necessarias = tinta_necessaria / 18
qtd_de_latas = math.ceil(latas_necessarias)

valor_total = qtd_de_latas * 80

print("======================================")
print(f"Área total do local (m²) :{area: .1f}")
print("Valor un. lata de 18 litros : R$ 80.00")
print("---------------------------------------")
print("- Quantidade de latas: {}".format(qtd_de_latas))
print(f"= Valor total da compra: R${valor_total: .2f}")
print("======================================")
print("Obrigado e volte sempre!!")
