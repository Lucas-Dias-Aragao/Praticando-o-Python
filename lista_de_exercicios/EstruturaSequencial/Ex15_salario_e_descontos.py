print("---- Contabilidade do Lucão ----\n")

print("Informe quanto você ganha por hora: ")
valor_da_hora = float(input("-> "))

print("\nTu trampou quantas horas no mês? ")
horas_trabalhadas_no_mes = float(input("-> "))

salario_bruto = valor_da_hora * horas_trabalhadas_no_mes
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
total_descontos = desconto_sindicato + desconto_inss + desconto_ir
salario_liquido = salario_bruto - total_descontos

print("-------------------------------------")
print(f"+ Salário bruto : R${salario_bruto: .2f}")
print(f"- IR (11%) : {desconto_ir: .2f}")
print(f"- INSS (8%) : {desconto_inss: .2f}")
print(f"- Sindicato (5%) : {desconto_sindicato: .2f}")
print(f"= Salário Líquido : R${salario_liquido: .2f}")
print("-------------------------------------")