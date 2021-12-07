
# Fuck part 1 was inefficient

# get input into list
with open('./input.txt') as f:
    fishes = [int(line) for line in f.read().splitlines()[0].split(',')]

fishes_data = {}
for fish in fishes:
    try:
        fishes_data[str(fish)] += 1
    except:
        fishes_data[str(fish)] = 1

days = 256
for _ in range(days):
    temp_fishes_data = {}
    new = 0
    for fishes in fishes_data:
        if int(fishes) > 0:
            try:
                temp_fishes_data[str(int(fishes)-1)] += fishes_data[fishes]
            except:
                temp_fishes_data[str(int(fishes)-1)] = fishes_data[fishes]
            continue
        try:
            temp_fishes_data['6'] += fishes_data[fishes]
        except:
            temp_fishes_data['6'] = fishes_data[fishes]
        new += fishes_data[fishes]
    if new > 0:
        try:
            temp_fishes_data['8'] += new
        except:
            temp_fishes_data['8'] = new
    fishes_data = temp_fishes_data

total = 0
for fish in fishes_data:
    total += fishes_data[fish]
print(total)
