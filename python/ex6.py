brand = 'Apple'
exchangeRate = 1.235235245
message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)
print (message)

# x += 1; x -= 1
#  list: mylist.append(df); del mylist[2]
mydict = dict(name= "y2o", age = "NA", sex = "male", profession = "DevOps")
print(mydict)
print(mydict["name"])
mydict["height"] = 100
print(mydict)
mydict["height"] = 1.3
print(mydict)
del mydict["age"]
print(mydict)

myInput = input("Hi, enter 1 or 2: ")

# In-line if 
print("My name is YAKUB" if myInput == "1" else "My alias is Y2O")

# for loop
pets = ['cats', 'dogs', 'rabbits', 'hamsters']
for position, pet in enumerate(pets):
    print(pet, "is at posssition", position)

for key, value in mydict.items():
    print(f"Name = {key}, Value = {value}")