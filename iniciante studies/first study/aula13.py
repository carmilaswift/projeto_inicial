# compreender funçoes indigt ; e comprrender o tratamento de erros com try e except

numero_str = input('irei dobrar um numero, digite este numero: ')

try:
    print('STR', numero_str.isdigit())
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'o dobro de {numero_float} é {numero_float ** 2:.0f}')
except :
    print('O valor inserido nao esta corretamente, tente novamente')