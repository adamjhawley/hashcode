import random
from parser import parse_inputs
from hill_climb import climb_hill

def prep_slides(slides):
    output = []
    hs, vs = splitSlides(slides)
    print(random.shuffle(vs))
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
            output.append([verts[n-1], verts[n]])

    return output

def main():
    inputs = parse_inputs("inputs/c_memorable_moments.txt")
    max_score = 0
    best_submission = []
    for _ in range(10):
        prep = prep_slides(inputs[:])
        score, data = climb_hill(prep, 100, True)
        if score > max_score:
            max_score = score
            best_submission = data
    print(max_score)
    return (max_score, best_submission)



if __name__ == "__main__":
    main()

