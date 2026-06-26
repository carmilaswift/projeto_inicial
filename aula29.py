# Learning lists on python 
# del - delete / clear() limpa a lista inteira
# insert = adiciona ao indice escolhido
# list = [10,40,80]
# number = list[2] = 3000000
# del list[-1]
# print(list)
# list.append(89)
# last_number = list.pop()
# print(list, 'removido,', last_number)

list_c =[ 1, 3 , 9]
list_d = [3, 9, 13]
list_a = list_c + list_d
list_a.extend(list_c)
print(list_a)