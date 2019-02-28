import random
from scorer import *

def climb_hill(data, maxtries):
    gooddata = data[:]
    datalen = len(data) - 1
    score = sum(calc_score(gooddata))
    tries = 0
    print(gooddata)
    while tries < maxtries:
        print(tries)
        localdata = gooddata[:]
        tries += 1
        if random.random() > 0.2:
            i1 = random.randint(0,datalen)
            i2 = random.randint(0,datalen)
            (localdata[i1], localdata[i2]) = (localdata[i2], localdata[i1])
        else:
            i1 = random.randint(0,datalen)
            while not isinstance(localdata[i1], list):
                i1 = random.randint(0,datalen)
            i2 = random.randint(0,datalen)
            while not isinstance(localdata[i2], list) or i2 == i1:
                i2 = random.randint(0,datalen)
            index1 = random.randint(0,1)
            index2 = random.randint(0,1)
            elem1 = localdata[i1][index1]
            elem2 = localdata[i2][index2]
            localdata[i1][index1] = elem2
            localdata[i2][index2] = elem1
        if sum(calc_score(localdata)) > score:
            gooddata = localdata
            tries = 0
    return (score, gooddata)
