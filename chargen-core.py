#code written by duck_master from 2021-02-16
#all code open source (MIT licensed)
#character-generator core
#inspired by gwern
#(writing at https://www.gwern.net/Statistical-notes#)
#currently only samples from people alive in 2021

#TODO: sample people from across world history
#TODO: sample location more finely from real data
#TODO: sample age from real data
#TODO: sample name from real data
#TODO: sample gender from real data
#TODO: sample poltical/religious/etc. beliefs from real data

import random

#read & preprocess world population distribution data
with open('data/wikipedia_population_clean.txt', 'r') as f:
    popdata_lines = f.readlines()
    f.close()
popdata = [l.split(' ') for l in popdata_lines]
popdata = [[l[0], int(''.join(l[1].strip('\n').split(',')))] for l in popdata]
worldpop = sum([l[1] for l in popdata])

#code credit to StackOverflow user "Boojum"
#https://stackoverflow.com/questions/3655430/selection-based-on-percentage-weighting
def select(values):
    '''Selects randomly from a categorical distribution.
    {any : numeric} -> any'''
    variate = random.random() * sum( values.values() )
    cumulative = 0.0
    for item, weight in values.items():
        cumulative += weight
        if variate < cumulative:
            return item
    return item # Shouldn't get here, but just in case of rounding...

print([select({ "a": 70, "b": 20, "c": 10 }) for i in range(40)])
