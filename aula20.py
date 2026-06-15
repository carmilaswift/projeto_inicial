# usuario sair :
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    numero_3 = input('Digite um operador (ex: +-/*)') 

    nu_1_float  = 0
    nu_2_float = 0
    numero_valido = None
    try:
        nu_1_float = float(numero_1)
        nu_2_float = float(numero_2)
        numero_valido = True
    except:
        numero_valido = None
    if numero_valido is None:
        print('Um dos numeros estão invalidos')
        continue
    operadores_permitidos = '+-/*'
    print('Um dos operadores estão invalidos')
    
    print('realizando o calculo : ')
    if len(numero_3) > 1:
        continue

    print('Digite apenas um operador')
    if numero_3 == '+':
        print(f'{nu_1_float}+{nu_2_float}=', nu_1_float + nu_2_float)
    elif numero_3 == '-':
        print(f'{nu_1_float}-{nu_2_float}=', nu_1_float - nu_2_float)
    elif numero_3 == '/':
        print(f'{nu_1_float}/{nu_2_float}=', nu_1_float / nu_2_float)
    elif numero_3 == '*':
        print(f'{nu_1_float}*{nu_2_float}=', nu_1_float * nu_2_float)
    else:
        print('houve um erro, lucas é so meu')
        

    sair = input('quer [s]air: ?').lower().startswith('s')
    print(sair)

    if sair is True:
        break