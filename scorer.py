# Takes two slides and returns the score between them
def calc_transition_score(s1, s2):
    left = s1.tags
    right = s2.tags
    common = 0
    only_l = 0
    only_r = 0

    for tag in left:
        if tag in right:
            common += 1
            right.remove(tag)
        else:
            only_l += 1
    only_r = len(right)

    return min(common, only_l, only_r)
