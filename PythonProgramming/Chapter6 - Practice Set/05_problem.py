# Write a program which finds out whether a given name is present in a list or not.

l = ["Hasan", "Rahat", "Rakib", "Rahim", "Karim"]

name = input("Enter your name: ")

if(name in l):
    print("Your name is in the list")
else:
    print("Your name is not in the list")