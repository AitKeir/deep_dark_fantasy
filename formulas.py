import math

def list_lvlExp():
    allLVL = []
    for a in range(100):
        x = (((a*a)-a)*3)/2
        allLVL.append('{0}:{1}'.format(a,math.floor(x)))
    return allLVL

def lvl_exp(a):
    x = (((a*a)-a)*3)/2
    return math.floor(x)

def what_lvl(allLVL,b):
    for c in allLVL:
        f = int(c.split(':')[1])
        if b < f:
            return int(c.split(':')[0])-1

def plus_exp(lastExp,inpExp,learning):
    newExp = lastExp + inpExp+learning
    return newExp
