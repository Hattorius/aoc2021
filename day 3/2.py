
# get input into list
with open('./input.txt') as f:
    input = f.read().splitlines()

gen_input = input
scrub_input = input

for i in range(len(input[0])):
    zero = 0
    one = 0
    for line in gen_input:
        if line[i] == "0":
            zero += 1
            continue
        one += 1
    if zero <= one:
        temp = []
        for line in gen_input:
            if line[i] == '1' or len(gen_input) == 1:
                temp.append(line)
        gen_input = temp
    else:
        temp = []
        for line in gen_input:
            if line[i] == '0' or len(gen_input) == 1:
                temp.append(line)
        gen_input = temp
    pass

for i in range(len(input[0])):
    zero = 0
    one = 0
    for line in scrub_input:
        if line[i] == "0":
            zero += 1
            continue
        one += 1
    if zero <= one:
        temp = []
        for line in scrub_input:
            if line[i] == '0' or len(scrub_input) == 1:
                temp.append(line)
        scrub_input = temp
    else:
        temp = []
        for line in scrub_input:
            if line[i] == '1' or len(scrub_input) == 1:
                temp.append(line)
        scrub_input = temp
    pass

generator = int(gen_input[0],2)
scrubber = int(scrub_input[0],2)

print(generator*scrubber)
