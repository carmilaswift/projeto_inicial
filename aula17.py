string = 'joao lucas'
variavel_2 = f'{string[:3]}ABC{string[4:]}'
print (string.capitalize())
print (variavel_2)
print (string.zfill(20))

while - loop infinito

condicao = True
while condicao:
    nome = input('Qual é o seu nome?: ')
    print(f'seu nome é {nome}')
    if nome == 'sair':
        print('saindo do programa...')
        condicao = False
        break

contador = 0

while contador <=10:
    contador = contador + 1 
    print(contador)

print('ended')


