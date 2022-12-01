print("Qual seu nivel de usuario?")
print ("Adm, User, ou Guest")
acesso_pessoa = input ("Digite o nivel de acesso: ").upper()
if acesso_pessoa=="ADM" or acesso_pessoa=="USER":
    genero = input("Digite seu sexo: ").upper()
    if acesso_pessoa=="ADM":
        if genero=="FEMININO":
            print("Olá, Administradora.")
        else:
            print("Olá, Administrador.")
    else:
        if genero=="FEMININO":
            print("Olá, Usuária")
        else:
            print("Olá, Usuário")
elif acesso_pessoa=="GUEST":
    print("Olá, visitante.")
else:
    print("Olá, Desconhecido.")

