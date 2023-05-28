# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%


print("**** Folha de Pagamento **** ")

valor_hora = float(input("Informe o valor da sua hora: ").replace(",","."))
percentual_ir = 0
salario_bruto = valor_hora * 220

if 900 < salario_bruto <= 1500:
    percentual_ir = 0.05
elif 1500 < salario_bruto <= 2500:
    percentual_ir = 0.10
elif salario_bruto > 2500:
    percentual_ir = 0.20
    
percentual_inss = 0.10
ir = salario_bruto * percentual_ir
inss = salario_bruto * percentual_inss
    
print(f"\nO salário bruto é: R$ {salario_bruto :.2f}")
print(f"(-) IR ({percentual_ir :.2f}%) :   R$ {ir :.2f}")
print(f"(-) INSS (10%):    R$ {inss :.2f}")
print(f"FGTS (11%):        R$ {salario_bruto * 0.11 :.2f}")
print(f"Total descontos:   R$ {ir + inss :.2f}")
print(f"Salario líquido:   R$ {salario_bruto - (ir + inss) :.2f}")
