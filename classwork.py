# Start with a main function and make each problem a function. Call those functions from your main function.

### Problem 1:
# Create a class Dog. Make sure it has the attributes name, breed, color, gender. Create a function that will print all attributes of the class. Create an object of Dog in your problem1 function and print all of it's attributes.

class Dog:
    def __init__(self, name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender

    def printAll(self):
        print(f'{self.name} is a {self.breed} that is {self.color} and is a {self.gender}')


def prob1():
    dogInfo = Dog('Joshua', 'Yorkie', 'Black', 'Make')
    dogInfo.printAll()


prob1()


# ### Problem 2:
# ##### We will keep having this problem until EVERYONE gets it right without help
# # Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.
# 
# def prob2():
#     userInput = ""
#     while userInput != 'q':
#         userInput = input('Enter info press q to quit')
# prob2()

### Problem 3:
# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
# The class should have several functions:
# a) One function that can change the name of the product.
#     b) Another function that can change the name and price of the product.
#     c) A last function that can change the name, price, and quantity of the product.
#     Create an object of Product and print all of it's attributes.

class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def nameCh(self, newName):
        self.name = newName
        print(f'this is the new product name:{newName}')

    def nameAndPriceCh(self, newName2, newPrice2):
        self.newName2 = newName2
        self.newPrice2 = newPrice2
        print(f'This is the new product {newName2} and the price is {newPrice2}')

    def changeAllAtt(self, newName3, newPrice3, newQty3):
        self.newName3 = newName3
        self.newPrice3 = newPrice3
        self.newQty3 = newQty3
        print(f'This is the new product {newName3} and the price is ${newPrice3} and you have {newQty3} on hand')

def prob3():
    productInfo1 = Product('candy', 10, 25)
    productInfo1.nameCh('chips')
    productInfo1.nameAndPriceCh('soda',0.65)
    productInfo1.changeAllAtt('SNACK CAKE', 2.00, 100)
    


prob3()
