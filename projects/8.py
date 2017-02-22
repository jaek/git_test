"""
Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""
f = open('test.txt', 'r')
inputs = f.read()
highest = 0
ADJACENT = 13


def getGreatestProduct(numberOf, startPoint, listName):
    """
    takes the number of adjacent digits to test, the indext to start from and the
    name of the list, returns the product of the adjacent digits
    """
    output = int(listName[startPoint]) #e.g input[0]
    for i in range(startPoint + 1, startPoint + 13):
        output = output * int(listName[i])
    return output

for index in range((len(inputs) - ADJACENT)):
    if getGreatestProduct(ADJACENT, index, inputs) > highest:
        highest = getGreatestProduct(ADJACENT, index, inputs)

print highest
