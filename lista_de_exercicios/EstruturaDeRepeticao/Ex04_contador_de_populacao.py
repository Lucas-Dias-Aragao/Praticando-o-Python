# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
# taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
# com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a 
# população do país A ultrapasse ou iguale a população do país B, 
# mantidas as taxas de crescimento.

qtd_a = 80000
qtd_b = 200000
cont_anos = 0

while qtd_b > qtd_a:
    qtd_a += ((qtd_a * 3) /100)
    qtd_b += ((qtd_b * 1.5) /100)
    cont_anos += 1
    
print("A ultrapassa ou iguala B em {} anos".format(cont_anos))