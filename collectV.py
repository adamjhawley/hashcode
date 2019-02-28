import random
from parser import parse_inputs

def main(slides):
    output = []
    hs, vs = splitSlides(slides)
    random.shuffle(vs)
    vs = joinVs(vs)
    hs.extend(vs)
    random.shuffle(hs)
    return hs

def findNextVertical(slides, index):
    for i in range(index, len(slides)-1):
        if slides[i].orientation == "V":
            return i

def splitSlides(slides):
    hs = []
    vs = []
    for i in slides:
        if i.orientation == "H":
            hs.append(i)
        else:
            vs.append(i)
    return (hs,vs)

def joinVs(verts):
    output = []
    for n, i in enumerate(verts):
        if n%2:
            output.append((verts[n-1], verts[n]))

    return output

print(main(parse_inputs("inputs/a_example.txt")))
