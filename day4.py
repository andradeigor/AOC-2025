from math import sqrt
text = open("text.txt", "r+")

lines = text.readlines()

mapa = []

def possibleMoves(i,j,x,y):
    possibleMoves = [[i+1,j], [i,j+1], [i+1,j+1], [i-1,j],[i,j-1], [i-1,j-1], [i-1,j+1], [i+1,j-1]]
    return list(filter(lambda k: k[0]<x and k[0]>=0 and k[1]<y and k[1]>=0, possibleMoves))


for line in lines:
    line = line.replace('\n', '')
    mapa.append(list(line))

total =0
removed = True
while(removed):
    removed = False

    for i in range(len(mapa)):

        for j in range(len(mapa[i])):
            if(mapa[i][j]!='@'):
                continue
            count=0
            moves = possibleMoves(i,j,len(mapa), len(mapa[i]))
            #print('*'*10)
            #print(f'[{i},{j}]')
            for move in moves:
                if(mapa[move[0]][move[1]]=='@'):
                    #print(move)
                    count+=1
            if(count<4):
                mapa[i][j] = '.'
                removed = True
                total+=1
         
print(total)
