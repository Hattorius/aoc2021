
# get input into list
with open('./input.txt') as f:
    input = f.read().splitlines()

gamma = ''
epsilon = ''
position = 0
for _ in input[0]:
    zero = 0
    one = 0
    for line in input:
        if line[position] == '0':
            zero += 1
        else:
            one += 1
    position += 1
    if zero > one:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print("Gamma:",gamma)
print("Epsilon:",epsilon)
print("Power consumption:",(gamma*epsilon))
