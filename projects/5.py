

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Another incredibly sub-optimal solution!
# Will have to revise and optimise to get this running in a reasonable period
# of time.

from timeit import default_timer

start = default_timer()

def divideby(num, ran):
    """ divides a given interger by all numbers in a given range,
    returns if num is divisible by all values between 0 and range
    """

    for i in range(ran):
        if num % (i + 1) != 0:
            return False
    return True

start = 2520

while divideby(start, 20) != True:
    start += 2520




print start

duration = default_timer() - start

print duration
