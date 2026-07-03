# list of list and your indices
room = [
    # zero ...... one 
    ["Mary", "Alice", ], #zero
    #zero
    ['Elaine', ], #one
    # zero....one....two
    ['Jonh', 'Lucas', 'João', (0, 10,20,30,40)], #two
]
print(room[2][3][2])
# By means of the list i can acess the elements of the list with the indices 
# In the tuple, he must add more one index to acess the number in tuple

for rooms in room:
    print(f'the classrom is {room}')
    for aluno in room:
        print(aluno)