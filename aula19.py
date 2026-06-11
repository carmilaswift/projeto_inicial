# itenando string com while:
nome = 'joao lucas'

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])
novo_nome = ''
indice = 0
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)