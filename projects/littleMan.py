#!/usr/bin/python

"""
My implimentation of a little man computer
"""




def splitter(string):
    """
    splits our input up by whitespace
    """
    commands = string.split()
    print commands
    commands = values(commands)
    return commands


def values(commandList):
    """
    convert our input into a useful mix of values and strings
    input: list of 3 character strings
    output: list consisting of three character strings, followed by 3 digit ints
    """
    newList = []
    for i in xrange(len(commandList)):
        try:
            newList.append(int(commandList[i]))
        except:
            newList.append(commandList[i])

    return newList

def parse(ins):
    """
    This function takes the user input which has been cleaned by our values
    and splitter functions, and passes it to the calculator in pairs of command/value
    """
    c = 0
    acc = 0
    box = [0] * 10 # boxes are numbered 0 to 9

    while c < len(ins):
        if isinstance(ins[c], int): #wait for command
            c += 1
        elif ins[c] == "ACC": #set ACC
            acc = ins[c+1]
            c += 1
        elif ins[c] == "ADD": #addition
            acc += ins[c+1]
            c += 1
        elif ins[c] == "SUB": #subtraction
            acc -= ins[c+1]
            c += 1
        elif ins[c] == "STA": #Store in Mailbox
            box[ins[c+1]] = acc
            c += 1
        elif ins[c] == "BRA": #Branch unconditional
            c += 1
        elif ins[c] == "BRZ": #Branch if zero
            if acc == 0:
                c = ins[c+1]
            else:
                c += 1
        elif ins[c] == "BRP": #Branch if positive
            if acc > 0:
                c = ins[c+1]
        elif ins[c] == "BRN": #Branch if negative
            if acc < 0:
                c = ins[c+1]
            else:
                c += 1
        elif ins[c] == "SWP": #Move data from a given address to ACC
            acc = box[ins[c+1]]
            c += 1
        elif ins[c] == "OUT":
            print acc
            c+=1
        else:
            print "command %r" % ins[c], "is not a valid input"

    print "ACC: %d" % acc, "\n"
    for i in range(len(box)):
        print "BOX %d" % i, ": ", "%d" % box[i]



f = open('test.txt', 'r')
test = f.read()
test = splitter(test)
parse(test)
