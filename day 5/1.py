
# get input into list
with open('./input.txt') as f:
    input = f.read().splitlines()

coords = []
seen = []
dupli = 0
for line in input:
    start, end = [list(map(int, a.split(','))) for a in line.split(' -> ')]
    if start[0] == end[0]:
        x = start[0]
        length = end[1] - start[1] 
        s = start[1]
        if length < 1:
            length*=-1
            s = end[1]
        length += 1
        for y in range(length):
            y += s
            coords.append([x, y])
            seen.append(str(x)+"."+str(y))
            if seen.count(str(x)+"."+str(y)) == 2:
                dupli += 1
    elif start[1] == end[1]:
        y = start[1]
        length = end[0] - start[0]
        s = start[0]
        if length < 1:
            length*=-1
            s = end[0]
        length += 1
        for x in range(length):
            x += s
            coords.append([x, y])
            seen.append(str(x)+"."+str(y))
            if seen.count(str(x)+"."+str(y)) == 2:
                dupli += 1

print(dupli)
