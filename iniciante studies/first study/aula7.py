entrada = input('[E]ntrada [S]air')
print(entrada)

senha_digitado = input('Senha: ')

senha_permitida = '1234567'

if (entrada == 'E' or entrada == 'e') and senha_digitado == senha_permitida:
    print('Entrada')
else:
    print('Sair')