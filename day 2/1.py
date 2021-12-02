
# get input into list
with open('./input.txt') as f:
    input = f.read().splitlines()

depth = 0
horizontal = 0

for line in input:
    n = int(line.split()[1])
    command = line.split()[0]
    if command == "forward":
        horizontal += n
    elif command == "down":
        depth += n
    elif command == "up":
        depth -= n

print("End result: "+str(depth*horizontal))
