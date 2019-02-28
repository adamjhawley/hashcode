import random
from solver import *

def climb_hill(data, maxtries):
    gooddata = data[:]
    datalen = len(data)
    score = sum(calc_score(gooddata))
    tries = 0
    while tries < 100:
        localdata = gooddata[:]
        tries += 1
        if random.random() > 0.2:
            i1 = random.randint(0,datalen)
            i2 = random.randint(0,datalen)
            (localdata[i1], localdata[i2]) = (localdata[i2], localdata[i1])
        else:
            i1 = random.randint(0,datalen)
            while not isinstance(localdata[i1], tuple):
                i1 = random.randint(0,datalen)
            i2 = random.randint(0,datalen)
            while not isinstance(localdata[i2], tuple) and i2 == i1:
                i2 = random.randint(0,datalen)
            index1 = random.randint(0,1)
            index2 = random.randint(0,1)
            localdata[i2][index2], localdata[i1][index1] = localdata[i1][index1], localdata[i2][index2] 
        if sum(calc_score(localdata)) > score:
            gooddata = localdata
            tries = 0
    return (score, gooddata)

