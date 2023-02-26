age = 10
name = 'Pooja'

if age < 12 and name == 'Nehal':  # should be both conditions true
    print("This is if block")
    print(f"{name} is less than {age}")

elif age == 10:   #else if in python
    print("Age is equal to 10")

elif name > 'Pooja':
    print("name is equal to Pooja")

else:
    print("This is else block")
    print(f"{name} is less than {age}")