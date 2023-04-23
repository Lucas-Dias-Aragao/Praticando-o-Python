# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

capacidade_lata = 18
capacidade_galao = 3.6
valor_lata = 80.00
valor_galao = 25.00

print("-- Lucão Tintas ---\n")
area = float(input("Área do local (m²): "))

tinta_necessaria = (area / 6) * 1.1    # 10% de folga
qtd_lata = math.ceil(tinta_necessaria / capacidade_lata)
qtd_galao = math.ceil(tinta_necessaria / capacidade_galao)

#latas e galoes
lata = int(tinta_necessaria/capacidade_lata)
galao = int((tinta_necessaria - (lata * capacidade_lata)) / 3.6)
if (tinta_necessaria - (lata * capacidade_lata) % 3.6 != 0):
    galao += 1


print('- Quantidade necessária de latas: {}'.format(qtd_lata))
print(f'- Valor de latas: R${qtd_lata * valor_lata: .2f}')
print('-------------------------------------------------')
print('- Quantidade necessária de galoes: {}'.format(qtd_galao))
print(f'- Valor total de galões: R${qtd_galao * valor_galao: .2f}')
print('-------------------------------------------------')
print('- Lata + galão: {} lata(s) e {} galões'.format(lata, galao))
print(f'- Valor total de galões: R${(lata * valor_lata) + (galao * valor_galao): .2f}\n')

