
# get input into list
with open('./input.txt') as f:
    depths = f.read().splitlines()
depths = list(map(int, depths))

increasesCount = 0
previousDepth = 99999999999999999
for i in range(len(depths)):
    try:
        depths[i+2]
    except:
        break

    currentDepth = depths[i] + depths[i+1] + depths[i+2]
    if currentDepth > previousDepth:
        increasesCount += 1
    previousDepth = currentDepth

print(increasesCount)
