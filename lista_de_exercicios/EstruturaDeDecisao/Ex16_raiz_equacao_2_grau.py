# #Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
# pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

print("*** Cálculo de raízes ***")

a = int(input("Informe o valor de a: "))

if a != 0:
    b = int(input("Informe o valor de b: "))
    c = int(input("Informe o valor de c: "))
else:
    print("A equação não é do segundo grau")
    exit()

delta = (math.pow(b, 2)) - 4 * a * c

print("Delta:", delta)
if delta < 0:
    print("A equação não possui raízes reais")
    exit()

raiz_1 = (-b + math.sqrt(delta)) / (2 * a)
raiz_2 = (-b - math.sqrt(delta)) / (2 * a)
print("Raízes: ")
print("X':", raiz_1)
print("X\":", raiz_2)
