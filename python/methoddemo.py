# class methoddemo:
#     a = 1

#     @classmethod
#     def classM(cls):
#         print("Class Method. cls.a= ", cls.a)

#     @staticmethod
#     def staticM():
#         print("Static Method")

class house():
    def __init__(self,  address, owner, price):
        self.address = address
        self.owner = owner
        self.price = price

house1 = house("Ilekun", "Yakub", 25000)
house2 = house("Agbopa", "Hassan", 300000)

print(house1.address)
print(house2.price)