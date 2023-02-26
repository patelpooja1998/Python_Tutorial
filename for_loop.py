print("Hello")

i = 5
for i in range(5,10,1):
    print(i)

name = ['Pooja','Nehal']
ages = [24,26]
zip_codes = [1234,3456]

#Zip function in Python
for name,ages,zip_codes in zip(name,ages,zip_codes):
    print(name,ages,zip_codes)