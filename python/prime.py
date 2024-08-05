# def checkIfPrime (numberToCheck):
# 	for x in range(2, numberToCheck):
# 		if (numberToCheck%x == 0):
# 			return False
# 	return True

# import sys

# instance_type = sys.argv[1]

# if instance_type == "t2.micro":
# 	print("This type will cost you $2 per day")

# elif instance_type == "t2.medium":
# 	print("This type will cost you $4 per day")

# elif instance_type == "t2.xlarge":
# 	print("This type will cost you $8 per day")

# else:
# 	print("Enter a valid instance type")


type = ["t2.micro", "t2.medium", 1, 2.89, "t2.large", 7, "t2.xlarge"]
print(type)

# new_list = type[:3]
# print(new_list)

# type.append(True)
# print(type)

# type.insert(1, "log.file")
# print(type)

# print(type.index("log.file"))

# type.remove("t2.medium")
# print(type)

# print(len(type))

# print(type[0], "--", type[1])

# my_tuple = type = ("t2.micro", "t2.medium", 1, 2.89, 7, "t2.large", "t2.xlarge")

for x in type:
#    print(x)
    if x == 7:
        continue
    print(x)