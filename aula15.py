# id = identidade 
# v1 = 'b'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

# none = nao valor / is and is not = é ou nao é \ 
# sendo (tipo, valor e identidade)

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('nao faça algo')

if  passou_no_if is None:
    print('passou no if')

else:
    print('nao passou no if')