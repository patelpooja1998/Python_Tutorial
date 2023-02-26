age = 10
name = 'Pooja'

if age < 12 and name == 'Nehal':  # should be both conditions true
    print(f"{name} is less than {age}")

if age == 10 or name == 'Nehal':
    print(f"{name} is less than {age}")  #should be one of them to be true

if (age < 12 and age == 10) and name == 'Pooja':
    print(f"{name} is less than {age} and eequal to 10")