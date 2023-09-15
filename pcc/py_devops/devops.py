# testing if/elif/else

i = 50
if i == 40:
    print ("i = 50")
elif i == 45:
    print ("i = 45")
elif i < 50:
    print ("i < 50")
else:
    print("I don't know much about i...")

# for loop
for x in range(5):
    i = x * 2
    if i == 4:
        continue
    print(i)

# while loop

count = 0
while True:
    print(f"The count is {count}")
    if count > 5:
        break
    count += 1

# List

name = "YAKUB Yusuf O"
print (list(name))

# print(dict(name))

name_list = ['cherry', 'cream', 'apple', 'rhubarb']
name_list.pop(0)
print (name_list)

sent = "  I pray God help us very soon  "
print(sent)
print(sent.strip())
print(sent.lstrip())
print(sent.rstrip())

a = " and ".join(name_list)
print(a)

# Changing the case of text
name = "YAKUB Yusuf O."
print(name.capitalize())
print(name.title())
print(name.lower())
print(name.upper())

# dict
map = {'key-1': 'value-1','key-2': 'value-2', 'key-3': 'value-3', 'key-4': 'value-4', 'key-5': 'value-5'}

for x, y in map.items():
    print(f"{x} : {y}")

if "key-7" in map:
    print(map["key-7"])
elif "key-6" in map:
    print(map["key-6"])
elif "key-5" in map:
    print(map["key-5"])
    print(map.values())
else:
    print("I don't know anything about map dictionary")