ROW = 20 #length of rows
highest = 0

f = open('input11.txt')
f = f.read()
f = map(lambda x: int(x), f.split()) #f is now an array consisting of intergers

def product(array, index):
    """takes an index and an array, returns the highest possible product of four
    adjacent numbers"""
    output = 0
    try: #straight line
        output = array[index] * array[index + 1] * array[index + 2] * array[index + 3]
    except:
        pass
    try: #downwards
        down = 1
        for n in xrange(index, index + (ROW * 3), ROW):
            down *= array[n]
        if down > output:
            output = down
    except:
        pass
    try: #right diagonal
        down = 1
        for n in xrange(index, index + (ROW * 3), ROW + 1):
            down *= array[n]
        if down > output:
            output = down
    except:
        pass
    try:
        down = 1
        for n in xrange(index, index + (ROW * 3), ROW + -1):
            down *= array[n]
        if down > output:
                output = down
    except:
            pass
    return output

for i in range(len(f)):
    if product(f, i) > highest:
        highest = product(f, i)

print highest
