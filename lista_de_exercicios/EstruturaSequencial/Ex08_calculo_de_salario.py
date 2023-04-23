valor_por_hora = input("Informe quanto você ganhar por hora: ")
horas_trabalhadas = int(input("Informe quantas horas trabalhou no mês: "))

valor = float(valor_por_hora.replace(",",".")) #Tratativa realizada em caso de números com vírgula e não ponto

salario = horas_trabalhadas * valor

print(f"Seu salário do mês é: R${salario: .2f} reais")


