from collections import namedtuple

Slide = namedtuple('Slide', 'orientation id tags')

def parse_inputs(input_name):
   with open(input_name) as inp:
       inp.readline()
       lines = inp.read().strip().split('\n')
       ret_vals = list()
       for n, i in enumerate(lines):
           split = i.split(' ')
           ret_vals.append(Slide(split[0], split[1], split[2:]))
       return ret_vals


