# Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
# senha igual ao nome do usuário, mostrando uma mensagem de 
# erro e voltando a pedir as informações.

nome = input("Informe o nome de usuário: ")
senha = input("informe a senha: ")

while nome == senha:
    print("Usuario e senha não podem ser iguais")
    senha = input("informe a senha: ")
print("Acesso permitido")

