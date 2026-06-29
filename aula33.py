# enumerate introduction:
list = ['mary', 'joseph', 'lucas', 'taylor']
list.append('joao')

for indice, nome in enumerate(list):
    print(indice, nome, list[indice])

# for tupla_enumerada in enumerate(list):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t(valor)')