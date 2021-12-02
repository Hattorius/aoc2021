
# get input into list
with open('./input.txt') as f:
    input = f.read().splitlines()

depth = 0
horizontal = 0
aim = 0

for line in input:
    n = int(line.split()[1])
    command = line.split()[0]
    if command == "forward":
        horizontal += n
        depth += aim*n
    elif command == "down":
        aim += n
    elif command == "up":
        aim -= n

print("End result: "+str(depth*horizontal))
