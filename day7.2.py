from collections import deque, defaultdict

text = open("text.txt", "r+")
lines = text.readlines()

mapa = []
for line in lines:
    line = line.replace('\n', '')
    mapa.append(list(line))

altura = len(mapa)
largura = len(mapa[0])


timelines = defaultdict(int)

beens = 0


start_pos = None
for i in range(altura):
    for j in range(largura):
        if mapa[i][j] == 'S':
            start_pos = (i, j)
            timelines[(i, j)] = 1
            break

def possibleMoves(i, j):
    global beens

    if i + 1 == altura:
        return []

    char = mapa[i + 1][j]
    if char == '.':
        return [(i + 1, j)]

    if char == '^':
        beens += 1
        moves = []
        if j != 0:
            moves.append((i + 1, j - 1))
        if j < largura - 1:
            moves.append((i + 1, j + 1))
        return moves

    return []

for i in range(altura):
    for j in range(largura):
        if (i, j) not in timelines:
            continue

        count_here = timelines[(i, j)]
        if count_here == 0:
            continue

        next_moves = possibleMoves(i, j)

        if not next_moves:
            continue

        for ni, nj in next_moves:
            timelines[(ni, nj)] += count_here


total_timelines = 0
last_row = altura - 1

for j in range(largura):
    if mapa[last_row][j] in ['.', '^', '|']:
        total_timelines += timelines[(last_row, j)]

print(total_timelines)
