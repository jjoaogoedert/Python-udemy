login = 'admin'
senha = '123456'

loginUser = str(input('Digite o seu login: '))
senhaUser = str(input('Digite a sua senha: '))

if (loginUser == login) and (senhaUser == senha):
    print("logado com sucesso")
else:
    print("Usuario ou senha invalidos")