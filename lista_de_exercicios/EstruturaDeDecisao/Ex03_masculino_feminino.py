# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

letra = input('Digite a letra: ').upper()

if letra == 'F':
    print('F - Feminino')
elif letra == 'M':
    print('M - Masculino')
else:
    print('Sexo inválido')