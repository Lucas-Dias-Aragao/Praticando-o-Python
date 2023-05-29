#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


data = input("Informe uma data no formato dd/mm/aaaa: ")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

bissexto = False
data_valida = True

if ano % 4 == 0:
    bissexto = True

if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 0:
    data_valida = False

elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia > 31: data_valida = False

elif mes in (4,6,9,11) and dia > 30: data_valida = False

elif mes == 2:
    if bissexto:
        if dia < 1 or dia > 29:
            data_valida = False
    else:
        if dia < 1 or dia > 28:
            data_valida = False

if data_valida:
    print("Data Válida")
else:
    print("Data Inválida")
