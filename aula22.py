#while / else
string = 'joaolucas'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('nao houve espaços')
print('fora do while por enquanto')