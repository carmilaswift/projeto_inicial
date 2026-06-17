frase = 'aoooooo'

# print(frase.count(''))
i = 0
qtd_letra_mais_apareceu = 0
letra_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quant_letra_apararecer_atual = frase.count(letra_atual)

    if qtd_letra_mais_apareceu < quant_letra_apararecer_atual:
        qtd_letra_mais_apareceu = quant_letra_apararecer_atual
        letra_mais = letra_atual

    i += 1

print('a letra o qual aapreceu mais vezes foi '
f'{letra_mais} que apareceu '
f'{qtd_letra_mais_apareceu}x')