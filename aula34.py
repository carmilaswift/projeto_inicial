# exercise list to buy in list
import os

lista = []

while True:
    print('Escolha uma opção:')
    opcao = input('[i] Inserir [a] Apagar [l] Listar [s] Sair: ').lower()

    if opcao == 'i':
        os.system('clear')  # Windows: cls
        valor = input('Digite um item: ')
        lista.append(valor)

    elif opcao == 'a':
        os.system('clear')
        indice_str = input('Digite o índice para remover: ')

        try:
            indice = int(indice_str)
            del lista[indice]
            print('Item removido com sucesso!')
        except ValueError:
            print('Digite apenas números.')
        except IndexError:
            print('Índice inexistente.')

    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar.')
        else:
            print('Lista de compras:')
            for indice, valor in enumerate(lista):
                print(indice, '-', valor)

    elif opcao == 's':
        print('Programa encerrado.')
        break

    else:
        print('Escolha apenas i, a, l ou s.')