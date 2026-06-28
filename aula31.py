# introduction and tuples
# example 1 :
# names = ['Mary', 'Joseph', 'Lucas', 'Joao']
# name1, name2, name3, name4 = names
# print(name3)
# example 2 :
# name1, *resto = ['Mary', 'Joseph', 'Lucas', 'Joao']
# print(name1)
# example 3 :
name, *_ = ['Mary', 'Joseph', 'Lucas', 'Joao']
print(name)