
# get input into list
with open('./input.txt') as f:
    input = f.read().splitlines()

coords = []
seen = []
dupli = 0
c = 0
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
    else:
        if start[0] > end[0]:
            x = -1
        elif start[0] < end[0]:
            x = 1
        if start[1] > end[1]:
            y = -1
        elif start[1] < end[1]:
            y = 1
        start[0] -= x
        start[1] -= y
        while True:
            start[0] += x
            start[1] += y
            coords.append([start[0], start[1]])
            seen.append(str(start[0])+"."+str(start[1]))
            if seen.count(str(start[0])+"."+str(start[1])) == 2:
                dupli += 1
            if start[0] == end[0] and start[1] == end[1]:
                break
    c += 1
    print(c)

print(dupli)
