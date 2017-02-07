#Problem 2

def genfib():
    '''This function returns an interger of the sum of all
    positive fibonacci sequence numbers below 4 000 000
    '''
    last = 1
    curr = 2
    total = 2
    while curr < 4000000:
        bak = curr + last
        last = curr
        curr = bak
        del(bak)
        if curr % 2 == 0:
            total += curr
        else:
            pass

    return(total)
