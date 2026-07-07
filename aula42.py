# Introduction for functions in Python - Reapplication things
# def impression(a , b, c):
#     print(a, b, c)

# impression(1, 2, 3)
# impression(1, 2, 4, ) # This will raise an error because the function expects exactly 3 arguments

def saudaction(name='None Name'):
    print(f'Hi, {name}!')

saudaction('Alice')
saudaction('Lucas')
saudaction('Joao')
saudaction() # This will use the default value 'None Name'
