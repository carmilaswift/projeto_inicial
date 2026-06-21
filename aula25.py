# range function = start ; stop and step 
numeros = range(10)
numeros = range(2, 34 , 4)
for numero in numeros:
    print(numero)

for i in range(10):
    if i == 2:
        print('í é igual a 2, pulando...')
        continue

    if i == 11:
        print('í é 8, your else nao vai executar')
        break

    for j in range(1, 3):
        print(i , j)
else:
    print('for completo com sucesso, congrations !')