position = 50


text = open("text.txt", "r+")

text = text.readlines()
total=0
for line in text:
    line = line.replace('\n', '')
    direction = line[:1]
    number = int(line[1:])
    numberOfZeros = number//100
    originalPosition = position
    #print(f'aqui {numberOfZeros}')
    number = number%100
    
    position = position - number if direction=="L" else  position + number
    if(position<0):
        if(originalPosition!=0):
            total+=1
        position = 100+(position)
    
    if(position>100):
        if(originalPosition!=0):
            total+=1
        
    position = position%100
    total+=numberOfZeros
    if(position==0):
        total+=1
    #print(position)
print(total)
    