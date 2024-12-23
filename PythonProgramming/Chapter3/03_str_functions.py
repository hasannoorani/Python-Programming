name = "Hasan"

print(len(name))
print(name.endswith("san"))
print(name.startswith("Ha"))


# 1. len()
# Description: Returns the length of the string.
text = "Hello, World!"
print(len(text))  # Output: 13

# 2. lower()
# Description: Converts all characters in the string to lowercase.
text = "Hello, World!"
print(text.lower())  # Output: "hello, world!"

# 3. upper()
# Description: Converts all characters in the string to uppercase.
text = "Hello, World!"
print(text.upper())  # Output: "HELLO, WORLD!"

# 4. strip()
# Description: Removes leading and trailing whitespace (or specified characters) from the string.
text = "   Hello, World!   "
print(text.strip())  # Output: "Hello, World!"

# 5. replace(old, new)
# Description: Replaces occurrences of old with new in the string.
text = "Hello, World!"
print(text.replace("World", "Python"))  # Output: "Hello, Python!"

# 6. split(separator)
# Description: Splits the string into a list of substrings using the specified separator.
text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']

# 7. join(iterable)
# Description: Joins elements of an iterable (like a list) into a single string, using the string as a separator.
fruits = ['apple', 'banana', 'cherry']
print(", ".join(fruits))  # Output: "apple, banana, cherry"

# 8. find(substring)
# Description: Returns the index of the first occurrence of substring. Returns -1 if not found.
text = "Hello, World!"
print(text.find("World"))  # Output: 7

# 9. index(substring)
# Description: Similar to find(), but raises a ValueError if substring is not found.
text = "Hello, World!"
print(text.index("World"))  # Output: 7

# 10. startswith(prefix) and endswith(suffix)
# Description: Checks if a string starts or ends with the specified prefix or suffix.
text = "Hello, World!"
print(text.startswith("Hello"))  # Output: True
print(text.endswith("!"))        # Output: True

# 11. count(substring)
# Description: Counts the number of non-overlapping occurrences of substring in the string. 
text = "banana"
print(text.count("a"))  # Output: 3

# 12. capitalize()
# Description: Capitalizes the first character of the string and makes all other characters lowercase.
text = "hello, world!"
print(text.capitalize())  # Output: "Hello, world!"

# 13. title()
# Description: Capitalizes the first letter of each word in the string.
text = "hello world"
print(text.title())  # Output: "Hello World"

# 14. isalnum()
# Description: Returns True if all characters in the string are alphanumeric (letters and numbers).
text = "Hello123"
print(text.isalnum())  # Output: True

# 15. isalpha()
# Description: Returns True if all characters in the string are alphabetic (no numbers or special characters).
text = "Hello"
print(text.isalpha())  # Output: True

# 16. isdigit()
# Description: Returns True if all characters in the string are numeric.
text = "12345"
print(text.isdigit())  # Output: True

# 17. isspace()
# Description: Returns True if all characters in the string are whitespace.
text = "   "
print(text.isspace())  # Output: True

# 18. zfill(width)
# Description: Pads the string with zeros on the left to make it the specified width.
text = "42"
print(text.zfill(5))  # Output: "00042"

# 19. ljust(width, fillchar) and rjust(width, fillchar)
# Description: Left-justifies (ljust()) or right-justifies (rjust()) the string, padding it with fillchar to the given width.
text = "Hello"
print(text.ljust(10, '-'))  # Output: "Hello-----"
print(text.rjust(10, '-'))  # Output: "-----Hello"

# 20. center(width, fillchar)
# Description: Centers the string, padding it with fillchar to the given width.
text = "Hello"
print(text.center(11, '-'))  # Output: "---Hello---"