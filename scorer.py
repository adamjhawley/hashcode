# Takes a list of slides and returns the score for that slideshow
def calc_score(slides):
    print(len(slides))
    scores = []
    for i in range(1, len(slides)):
        scores.append(calc_transition_score(get_tags(slides[i - 1]),
                                            get_tags(slides[i])))
    return(scores)


# Takes two slides and returns the score between them
def calc_transition_score(left, right):
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

# Gets the tags from a slide, vertical or horizontal
def get_tags(slide):
    if type(slide) is tuple:
        tags_out = slide[0].tags
        for tag in slide[1].tags:
            if tag not in tags_out:
                tags_out.append(tag)
        return tags_out

    else:
        return slide.tags
