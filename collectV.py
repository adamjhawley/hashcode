import random
from parser import parse_inputs

def main(slides):
    output = []
    hs, vs = splitSlides(slides) 
    random.shuffle(vs)
    vs = joinVs(vs)
    output = hs + vs
    random.shuffle(output)
    return output

def findNextVertical(slides, index):
    for i in range(index, len(slides)-1):
        if slides[i].orientation == "V":
            return i

def splitSlides(slides):
    hs = []
    vs = []
    for i in slides:
        if i.orientation == "H":
            hs += i
        else:
            vs += i
    return (hs,vs)

def joinVs(verts):
    output = []
    for i in range((len(verts)-1)/2):
        output += (verts[i], verts[i*2])

    return output

print(main(parse_inputs("inputs/a_example.txt")))
