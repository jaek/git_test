from math import sqrt

def isPrime(num):
    for i in range(2, num):
        if not num % i:
            return False
    return True

c = 6   #counter
t = 13   #number to test
LIMIT = 10001

while c < LIMIT:
    t += 2
    if isPrime(t):
        c += 1
        print t

print t
