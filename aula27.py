# exercicio usuario descobrirá a senha secreta 
palavra_secreta = 'verde'
letras_com_acertos = ''
tentativas = 0
# while 'verde' in '':
#     if len(letra_digitada) == 1 and palavra_secreta in letra_digitada:
#         print('A letra {letra} esta contida em {palavra_secreta}')
    
while True:
    letra_digitada = input('Digite um valor: ').lower()
    tentativas += 1
    if len(letra_digitada) != 1:
        print('Digite apenas um valor !')
        continue

    if letra_digitada in palavra_secreta:
        letras_com_acertos += letra_digitada

        letra_formado = ''
        
        for letra in palavra_secreta:
            if letra in letras_com_acertos:
                letra_formado += letra
            else:
                letra_formado += '*'

        print(letra_formado)

        if letra_formado == palavra_secreta:
            print(f'VOCE ACERTOU ! e seu numero de tentativas foi {tentativas}')
            break