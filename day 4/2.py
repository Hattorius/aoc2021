
# get input into list
with open('./input.txt') as f:
    input = f.read().splitlines()

drawn = list(map(int, input[0].split(',')))
input = input[2:]
boards = []

board = []
for line in input:
    line = list(map(int, line.split()))
    if len(line) == 0:
        boards.append(board)
        board = []
        continue
    row = []
    for number in line:
        row.append({
            'number': number,
            'picked': False
        })
    board.append(row)
if len(board) > 0:
    boards.append(board)

won = []
for number in drawn:
    for iii in range(len(boards)):
        board = boards[iii]
        for row in board:
            for i in range(len(row)):
                n = row[i]
                if n['number'] == number:
                    n['picked'] = True
                    rowMatch = 0
                    colMatch = 0
                    win = False
                    for nn in row:
                        if nn['picked']:
                            rowMatch += 1
                    if rowMatch == len(row):
                        win = True
                    else:
                        for row in board:
                            nn = row[i]
                            if nn['picked']:
                                colMatch += 1
                        if colMatch == len(board):
                            win = True
                    if win:
                        if iii in won or len(won) < len(boards) - 1:
                            if iii not in won:
                                won.append(iii)
                            continue
                        winValue = 0
                        for roww in board:
                            for nnn in roww:
                                if not nnn['picked']:
                                    winValue += nnn['number']
                        print(winValue*number)
                        exit()