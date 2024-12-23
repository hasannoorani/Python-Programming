# Write a program to create a dictionary of Hindi words with values as their English translation.
# Provide user with an option to look it up!

words = {
    "namaste": "Hello",
    "kaise ho": "How are you",
    "achchha": "Good",
    "dhanyavaad": "Thank you",
    "svaagat": "Welcome",
    "madad": "Help"
}

word = input("Enter the word you want to meaning of: ")

print(words[word])