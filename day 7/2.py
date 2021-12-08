
# YES THIS ANSWER TAKES LONG TO PROGRESS
# YES I KNOW HOW TO DO IT BETTER
# NO I'M NOT GOING TO DO IT BETTER

import sys

# get input into list
with open('./input.txt') as f:
    crab_positions = [int(line) for line in f.read().splitlines()[0].split(',')]

minimum_position = min(crab_positions)
maximum_position = max(crab_positions)
steps = maximum_position - minimum_position

sys.setrecursionlimit(maximum_position + 100)

def calculate_fuel(start, target, cost=1):
    if start == target:
        return 0
    if start > target:
        return cost + calculate_fuel(start-1, target, cost+1)
    return cost + calculate_fuel(start+1, target, cost+1)

print("target:", maximum_position)

lowest = -1
lowest_fuel = 9999999999999999
for i in range(steps + 1):
    position = minimum_position + i
    print(position)
    fuel_cost = 0
    for crab_position in crab_positions: # this should be unnecessary, if I'm going to calculate this anyway at every loop, why not save the results for sped???
        fuel_cost += calculate_fuel(crab_position, position)
        if fuel_cost > lowest_fuel: # give it some extra speed: it needs it
            break
    if fuel_cost < lowest_fuel:
        lowest = position
        lowest_fuel = fuel_cost

print(lowest_fuel)
