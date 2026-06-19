# funçao for and while
texto = 'python'

novo_texto = ''
for letra in texto:
    novo_texto += f'.{letra}'
print(novo_texto + '.')


senha = '1234'  # 1. Definida como string para coincidir com o input
senha_digitada = ''
repeticoes = 0

while senha != senha_digitada:
   
    senha_digitada = input(f'digite a senha ({repeticoes}ª tentativa): ')
    
    repeticoes += 1

    if senha_digitada == senha:  
        print('senha esta correta')
    else:                        #
        print('senha invalida')
   
print(f'Total de tentativas: {repeticoes}')
