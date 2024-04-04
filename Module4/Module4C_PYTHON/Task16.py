elements = {
    "elementOne": "Hydrogen",
    "elementTwo": "Helium",
    "elementThree": "Lithium",
    "elementFour":  "Beryllium",

}

# Print the dictionary in console
print(elements)

# Update the dictionary with two different key-value pair items
elements.update({"elementFive": "Boron", "elementSix": "carbon"})
print("Update:", elements)

# Other List Functions
# Keys
elements_keys = elements.keys()
print("Keys:", elements_keys)

# Values
elements_values = elements.values()
print("Values:", elements_values)

# popitem
elements.popitem()
print("Pop Item:", elements)

#copy
elements_copy = elements.copy()
print(elements_copy)

#clear
elements_copy.clear()
print("Clear:", elements_copy )

#Print the first original elements
print(elements)