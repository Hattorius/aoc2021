
# get input into list
with open('./input.txt') as f:
    fishes = [int(line) for line in f.read().splitlines()[0].split(',')]

days = 80
for _ in range(days):
    temp_fishes = []
    new = 0
    for fish in fishes:
        if fish > 0:
            temp_fishes.append(fish - 1)
            continue
        temp_fishes.append(6)
        new += 1
    for _ in range(new):
        temp_fishes.append(8)
    fishes = temp_fishes

print(len(fishes))
