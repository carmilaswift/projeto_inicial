import random
import time

materias = [
    "Matemática",
    "Português",
    "Biologia",
    "Química",
    "Física",
    "História",
    "Geografia",
    "Filosofia",
    "Sociologia",
    "Inglês"
]


def gerar_estudo():
    materia = random.choice(materias)
    tempo = random.randint(30, 90)

    print("\n===== PLANO DE ESTUDO =====")
    print(f"Matéria sorteada: {materia}")
    print(f"Tempo recomendado: {tempo} minutos")
    print("===========================\n")


while True:
    print("=== GERADOR DE ESTUDOS ===")
    print("[1] Sortear estudo")
    print("[2] Adicionar matéria")
    print("[3] Listar matérias")
    print("[4] Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        gerar_estudo()
        time.sleep(1)

    elif opcao == "2":
        nova = input("Digite o nome da nova matéria: ").strip()

        if nova:
            materias.append(nova)
            print(f'"{nova}" adicionada com sucesso!')
        else:
            print("Nome inválido.")

    elif opcao == "3":
        print("\nMatérias cadastradas:")
        for indice, materia in enumerate(materias, start=1):
            print(f"{indice}. {materia}")

    elif opcao == "4":
        print("Até a próxima! Bons estudos!")
        break

    else:
        print("Opção inválida.")