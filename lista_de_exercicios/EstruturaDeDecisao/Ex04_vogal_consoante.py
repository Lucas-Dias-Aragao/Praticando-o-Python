# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Informe uma letra: ').upper()

if 'AEIOU'.find(letra) >= 0:
    print(letra,'é uma vogal')
else:
    print(letra,'é uma consoante')
