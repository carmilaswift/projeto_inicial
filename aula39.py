# unpacking in call ; for method and functions
the_string = 'ABCD'
list = ['mary', 'helena', 'eduarda']
tuple = 'Python', 'is', 'cool'
room = [
    # zero ...... one 
    ["Mary", "Alice", ], #zero
    #zero
    ['Elaine', ], #one
    # zero....one....two
    ['Jonh', 'Lucas', 'João', (0, 10,20,30,40)], #two
]
# a, b, c = list
# print(a, c)

# for name in list:
#     print(name, end=' ')
    # second option
print(*list)
print(*room, sep='\n')