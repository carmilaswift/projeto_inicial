# split and join with list and string
# split - divides a the string
# join - combines a list of strings into a single string
# function strip() - cut the spaces in both sides of the string
# function rstrip() - cut the spaces in the right side of the string
pharse = "look at this example, this is interesting"
list_of_words = pharse.split(',')
for i, frase in enumerate(list_of_words):
    print(list_of_words[i].rstrip())
print(list_of_words)
# the combined with join() function:
pharses_united = '-'.join('list_of_words')
print(pharses_united)
