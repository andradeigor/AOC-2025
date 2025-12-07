from collections import deque
text = open("text.txt", "r+")

lines = text.readlines()

mapa = []
for line in lines:
    line = line.replace('\n', '')
    mapa.append(list(line))

locationsAdded = set()
locationsToMove = deque()


def addedLocation(location):
    if(location in locationsAdded):
        return
    locationsAdded.add(location)
    locationsToMove.append(location)

beens = 0

for lineIndex in range(len(mapa)):
    for columnIndes in range(len(mapa[0])):
        if(mapa[lineIndex][columnIndes]=='S'):
            locationsToMove.append((lineIndex,columnIndes))
            locationsAdded.add((lineIndex,columnIndes))
            break

def possibleMoves(i,j):
    global beens
    if(i+1 == len(mapa)):
        return []
    char = mapa[i+1][j]
    if((char )=='.'):
        return [(i+1,j)]
    if(char =='^'):
        beens+=1
        moves = []
        if(j!=0):
            moves.append((i+1,j-1))
        if(j<len(mapa[0])-1):
            moves.append((i+1,j+1))
        return moves


#print(locationsToMove)
while locationsToMove:
    currentPossition = locationsToMove.popleft()
    #print(currentPossition)
    x,y = currentPossition
    possibleNewMovesList = possibleMoves(x,y)
    #mapa[x][y] = "|"
    #print(possibleNewMovesList)
    for move in possibleNewMovesList:
        #print(move)
        addedLocation(move)


print(len(locationsAdded))
print(beens)    

