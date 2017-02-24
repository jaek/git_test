from math import sqrt

# generate a list of primes less than NUM
NUM = 600851475143
highest = 0

def is_prime(number):
    for i in xrange(2, int(sqrt(number)+1)):
        if number % i == 0:
            return False
    return True

def factors(number):
    highestPrime = 0
    for i in xrange(1, int(sqrt(number)+1)):
        if not number % i:
            if is_prime(i) or is_prime(int(number / i)):
                highestPrime = i
    return highestPrime

print factors(NUM)
