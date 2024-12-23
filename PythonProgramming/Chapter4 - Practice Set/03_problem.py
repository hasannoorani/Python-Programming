# Check that a tupple cannot be changed in python.

tup = (1, 2, 3)

tup[1] = 4

print(tup)  #TypeError: 'tuple' object does not support item assignment