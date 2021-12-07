
# get input into list
with open('./input.txt') as f:
    crab_positions = [int(line) for line in f.read().splitlines()[0].split(',')]


