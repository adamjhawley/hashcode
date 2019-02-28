from parser import *
from scorer import calc_score

inputs = [Slide('H', 1, ['a', 'b', 'c']), Slide('H', 2, ['b', 'c', 'd']),
          [Slide('V', 3, ['a','b','c']), Slide('V', 4, ['b','c','d'])]]
print(inputs)
print(calc_score(inputs))
