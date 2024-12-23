car = {
    "name": "Tom",
    "age": 25,
    "city": "New York"
}
print(car.items())

print(car.keys())

print(car.values())

car.update({"name": "John", "skill": "Python"})  # Update the carionary and carionary is mutable
print(car)

print(car.get("name"))
print(car["name"])

# print(car.get("name2")) #Prints None
# print(car["name2"])  #Returns an error

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
 
car.pop("model")  # Removes the element with the specified key
print(car)

car.popitem()    # Removes the last inserted key-value pair
print(car)

car.clear()  # Clears the carionary
print(car)


