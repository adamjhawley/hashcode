from parser import parse_inputs
from scorer import calc_score

inputs = parse_inputs("inputs/a_example.txt")
print(inputs)
print(calc_score(inputs))
