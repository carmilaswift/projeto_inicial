# exercicio:
# pedir ao usuario para digitar nome e retornar exibido nome
# nome invertido, quantidade de letras, quantidade de espaços
# primeira letra e ultima letra do nome    


if __name__ == '__main__':
    print(input(f'digite seu nome: '))
else:
    print('DESCULPE, VOCE DEIXOU CAMPOS VAZIO !')
if inverso := input('digite seu nome novamente: '):
    print(f'Nome invertido: {inverso[::-1]}')
else:
    print('DESCULPE, VOCE DEIXOU CAMPOS VAZIO !')
if quantidade_de_espaços := input('digite seu nome mais uma vez: '):
    print(f'Quantidade de espaços: {quantidade_de_espaços.count(" ")}')
else:
    print('DESCULPE, VOCE DEIXOU CAMPOS VAZIO !')
if quantidade_de_letras := input('digite seu nome mais uma vez: '):
    print(f'Quantidade de letras: {len(quantidade_de_letras)}')
else:
    print('DESCULPE, VOCE DEIXOU CAMPOS VAZIO !')
if first_letter := input('digite seu nome : '):
    print(f'Primeira letra: {first_letter[0]}')
else:
    print('DESCULPE, VOCE DEIXOU CAMPOS VAZIO !')
if last_letter := input('digite seu nome: '):
    print(f'Última letra: {last_letter[-1]}'   )
else:
    print('DESCULPE, VOCE DEIXOU CAMPOS VAZIO !')
