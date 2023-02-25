example_list = [1,2,3,4,5]

print(example_list, type(example_list))

#length of the list
print(len(example_list))

#Append values in the list
example_list.append(6)
example_list.append('test')
example_list.append(1.2)
print(example_list)

print(example_list[-1])

#slicing lists
example_list_two = example_list[0:5]
print(example_list_two)

#Merge two lists
example_list += example_list_two
print(example_list)

#Remove elements
example_list.pop() # Remove last element from the list by default
print(example_list)
example_list.pop(2)
print(example_list)

#Assigning values

example_list[0] = 11
print(example_list)
example_list[-1] = ['H','E','y']
print(example_list)