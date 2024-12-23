# Write a program to detect double space in a string.

name = "Ali is a good boy and"

print(name.find("  "))  #output is -1 means not double space present


name = "Ali is a good boy and  intelligent"

print(name.find("  "))  #output is 21 means double space present
