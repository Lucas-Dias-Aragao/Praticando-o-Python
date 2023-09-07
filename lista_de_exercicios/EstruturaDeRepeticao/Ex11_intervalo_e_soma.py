# Altere o programa anterior para mostrar no final a soma dos números.

valor_inicial = int(input("Informe o valor inicial"))
valor_final = int(input("Informe o valor final"))
soma = 0

while valor_inicial < valor_final-1:
    soma += valor_inicial+1
    print(valor_inicial + 1, end=" ")
    valor_inicial += 1
    
print("\nA soma dos numeros no intervalo é: {}".format(soma))