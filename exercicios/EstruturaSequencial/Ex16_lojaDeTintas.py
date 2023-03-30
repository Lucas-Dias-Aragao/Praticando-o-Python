import math

print("-- Lucão Tintas ---\n")

area_em_metros = float(input("Área do local (m²): "))

tinta_necessaria = area_em_metros / 3
latas_necessarias = tinta_necessaria / 18
qtd_de_latas = math.ceil(latas_necessarias)

valor_total = qtd_de_latas * 80

print("======================================")
print(f"Área total do local (m²) :{area_em_metros: .1f}")
print("Valor un. lata de 18 litros : R$ 80.00")
print("---------------------------------------")
print("- Quantidade de latas: {}".format(qtd_de_latas))
print(f"= Valor total da compra: R${valor_total: .2f}")
print("======================================")
print("Obrigado e volte sempre!!")
