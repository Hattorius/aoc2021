
# get input into list
with open('./input.txt') as f:
    depths = f.read().splitlines()

increasesCount = 0
previousDepth = 99999999999999
for depth in depths:
    if int(depth) > previousDepth:
        increasesCount += 1
    previousDepth = int(depth)

print(increasesCount)
