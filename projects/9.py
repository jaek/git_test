"""


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2h

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

# generate a list of 3 numbers which add to form 1000
# a < b < c

from math import sqrt

for a in range (1000):
    for b in range(a, 1000):
        c = sqrt(a ** 2 + b ** 2)
        if c + b + a == 1000:
            print a, b, c
            print a * b * c
        else:
            pass
