#code written by duck_master from 2021-02-16
#open source (MIT licensed)
#character-generator core

import random

with f as open('data/wikipedia_population_clean.txt', 'r'):
    popdata_lines = f.readlines()

popdata = [l.split(' ') for l in popdata_lines]
