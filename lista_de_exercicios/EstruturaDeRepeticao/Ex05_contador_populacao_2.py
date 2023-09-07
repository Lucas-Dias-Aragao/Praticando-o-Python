# Altere o programa anterior permitindo ao usuário informar as populações e as taxas 
# de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

qtd_a = int(input("Informe o numero de habitantes do país A"))
tx_cresc_a = float(input("Informe a taxa de crescimento do país A"))
qtd_b = int(input("Informe o numero de habitantes do país B"))
tx_cresc_b = float(input("Informe a taxa de crescimento do país B"))
cont_anos = 0

while qtd_b > qtd_a:
    qtd_a += ((qtd_a * tx_cresc_a) /100)
    qtd_b += ((qtd_b * tx_cresc_b) /100)
    cont_anos += 1
    
print("A ultrapassa ou iguala B em {} anos".format(cont_anos))