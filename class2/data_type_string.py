FRUIT = "apple"
# Shows the value of the FRUIT key
print(FRUIT)
# Shows the location on the string in the memory
print(id(FRUIT))
# Shows the data type
print(type(FRUIT))
# #Shows the methods of the string
# print(dir(FRUIT))
# Capitalize the first letter
print(FRUIT.capitalize())
#Find how many times p is repeated
print(FRUIT.count("p"))
#Find out if the string starts with something
print(FRUIT.startswith("app"))
#Find out if the string end with something
print(FRUIT.endswith("pple"))
# Change to uppercases
print(FRUIT.upper())
# Create new variable
INCORRECT_STRING ="  spaced_string   "
# Print value
print(INCORRECT_STRING)
# Remove spaces on the left side
print(INCORRECT_STRING.lstrip())
# Remove spaces on the right  side
print(INCORRECT_STRING.rstrip())
# Remove spaces from both side
print(INCORRECT_STRING.strip())
