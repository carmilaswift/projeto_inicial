# programa usuario retornando valor impar ou par
numero = int(input('digite um numero; '))
if numero % 2 == 0:
    print('este numero é par')
else:
    print ('este numero é impar')

# programa usuario saudacao de horario digitado e retorna a saudacao correta mais valor do horario digitado
horario = int(input('digite o  horario: '))
horario_formatado = horario%24
if horario < 11:
    saudacao = 'bom dia as horas sao : '
elif horario >=12 and horario < 18 :
    saudacao = 'boa tarde as horas sao : '
else:
    saudacao = 'boa noite as horas sao : '
mensagem = f'{saudacao} {horario_formatado}'
print(mensagem)

## solicitado nome do usuario  é dado se é curto, extenso ou normal
nome = input(f'digite seu nome: ')
if len(nome) < 4:
    name = 'seu nome é curto'
elif len(nome) >= 5 and len(nome) <= 6:
    name = 'seu nome é normal'
else:
    name = 'seu nome é muito grande'
namme =  'seu nome é '

your_name = f'{namme} e {name} e tem {len(nome)} letras'
print(your_name)