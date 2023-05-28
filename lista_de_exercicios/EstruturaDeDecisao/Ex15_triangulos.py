# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;


lado_a = int(input("Informe a medida do primeiro lado"))
lado_b = int(input("Informe a medida do segundo lado"))
lado_c = int(input("Informe a medida do terceiro lado"))

if (lado_a + lado_b) > lado_c or (lado_c + lado_b) > lado_a or (lado_a + lado_c) > lado_b:
    if lado_a == lado_b == lado_c:
        print("Triangulo equilatero")
    elif lado_a == lado_b or lado_c == lado_b or lado_a == lado_c:
        print("Triangulo Isósceles")
    else:
        print("Triangulo Escaleno")
else:
    print("As medidas informadas não formam um triângulo")
