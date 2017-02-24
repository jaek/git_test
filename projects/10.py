from math import sqrt

rval = 0

def is_prime(number):
    for i in xrange(2, int(sqrt(number)+1)):
        if number % i == 0:
            return False
    return True

for i in range(2, 2000000):
    if is_prime(i):
        rval += i

print rval
