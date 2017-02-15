"""


Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


"""
upto = 100
c = 0
num = 0

def sumOfSquares(ran):
    sumOf = 0
    for i in range(ran + 1):
        sumOf += i ** 2
    return sumOf

while c < 100:
    c += 1
    num += c

print sumOfSquares(upto), "sum of squares\n"
print num, "    " , num ** 2, " sum of first 100, that squared"

print (num ** 2) - sumOfSquares(upto)
