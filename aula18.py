# operados de atribuição
# operador ; =+ adicao =- subtracao *= multiplicacao
# /= divisao ; //= divisao inteira ou exata ; **= exponencial ; %= modulo
# operador = 1
# operador **= 5
# print(operador)
qntd_coluna = 5
qntd_linhas = 5

linha = 1
while linha <= qntd_linhas:
    coluna = 1
    print(linha)

    while coluna <= qntd_coluna:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('acabou')