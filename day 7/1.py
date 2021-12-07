
# get input into list
with open('./input.txt') as f:
    crab_positions = [int(line) for line in f.read().splitlines()[0].split(',')]

minimum_position = min(crab_positions)
maximum_position = max(crab_positions)
steps = maximum_position - minimum_position

lowest = -1
lowest_fuel = 9999999999999999
for i in range(steps + 1):
    position = minimum_position + i
    fuel_cost = 0
    for crab_position in crab_positions:
        if crab_position >= position:
            fuel_cost += crab_position - position
        else:
            fuel_cost += position - crab_position
    if fuel_cost < lowest_fuel:
        lowest = position
        lowest_fuel = fuel_cost

print(lowest_fuel)
