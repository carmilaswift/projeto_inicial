# Exercise - CPF Generator
import random

def gerar_cpf(formatado=True):
    def calcula_digito(cpf, peso_inicial):
        soma = sum(int(d) * peso for d, peso in zip(cpf, range(peso_inicial, 1, -1)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    cpf = [random.randint(0, 9) for _ in range(9)]
    cpf.append(calcula_digito(cpf, 10))
    cpf.append(calcula_digito(cpf, 11))

    cpf_str = ''.join(map(str, cpf))

    if formatado:
        return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"
    return cpf_str

# Exemplo de uso
if __name__ == "__main__":
    print(gerar_cpf())          # ex: 123.456.789-09
    print(gerar_cpf(False))     # ex: 12345678909