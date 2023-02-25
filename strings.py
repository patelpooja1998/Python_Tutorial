# Strings in Python

hello_world = 'Hello world'
print(hello_world)

#Concatenate the strings
hello = 'hello'
world = 'world'
another_hello_world = hello +" "+ world
print(another_hello_world)

# Slicing the string

print(another_hello_world[0:5])
print(another_hello_world[6:])

# Get the index of the characters

print(another_hello_world.index('w'))

# Upper Case and Lower case
hello_world_upper = another_hello_world.upper()
print(hello_world_upper)
hello_world_lower = another_hello_world.lower()
print(hello_world_lower)