# usuario sair :
while True:
    sair = input('quer [s]air: ?').lower().startswith('s')
    print(sair)

    if sair is True:
        break