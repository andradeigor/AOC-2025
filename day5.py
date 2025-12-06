from math import sqrt
text = open("text.txt", "r+")

lines = text.readlines()

i=0
total =0
ranges = []
line = lines[i]
while(line!='\n'):
    line = line.replace('\n', '')
    leftInterval, rightInteval = line.split('-')
    ranges.append((int(leftInterval), int(rightInteval)))
    i+=1
    line = lines[i]
i+=1



ranges.sort(key=lambda x: x[0])

merged = []
for interval in ranges:
    if not merged or interval[0] > merged[-1][1]:
        merged.append(list(interval))
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])



for range1 in merged:
    numberOfNumbers = abs(range1[1] - range1[0]) +1
    total+= numberOfNumbers

print(total)



