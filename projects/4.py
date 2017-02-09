# This is a very inefficient solution to the problem, but after trying (and
# failing to figure out some less
# Brute force ways to complete it, I ended up with this very ugly solution
# At http://code.jasonbhill.com/c/project-euler-problem-4/, Jason has outlined
# a much more efficient approach. I think I'll come back to this problem when
# I'm a better programmer.

def palindrome(num):
    """Checks whether a given interger is a palindrome
       returns true or false
       """

    numA = map(int, str(num))
    for i in range(int(len(numA) / 2)):
        if numA[i] != numA[-i - 1]:
            return False

    return True

def genNumbers(num):
    """starting from 999 * 999, iterates down to 100 * 100
    returns the highest palindrome"""
    times = []
    highest = 0
    for i in range(num):
        for x in range(num):
            if palindrome(x * i) and x * i > highest:
                highest = x * i
    print highest
    #for i in range(len(numlist)):
    #    if palindrome(numlist[-i]):
    #        print numlist[-i]
    #        return()



genNumbers(999)
