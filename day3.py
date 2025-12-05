from math import sqrt
text = open("text.txt", "r+")

lines = text.readlines()

total =0
"""
for line in lines:
    line = line.replace('\n', '')
    currentBigestNumber = 0
    currentBigestBateryPower = 0
    for numberStr in line:
        number = int(numberStr)
        #print(f'{number} - {currentBigestNumber} - {currentBigestBateryPower}')
        
        currentBigestBateryPower = number if currentBigestBateryPower==0 else max(int(str(currentBigestNumber) + str(number)), currentBigestBateryPower)
        currentBigestNumber = max(number, currentBigestNumber)
        
    total+=currentBigestBateryPower

"""
for line in lines:
    line = line.replace('\n', '')
    currentBigestBateryPower = ""
    digitsLeft = 12
    i=0
    for numberStr in line:
        currentBigestNumberLeft = 0
        currentBigestIndex = 0
        if(len(currentBigestBateryPower)==12):
            break
        while(len(line) -i>=digitsLeft and digitsLeft>0):
            #print(f'{i} - {digitsLeft}')
            if(int(line[i]) > currentBigestNumberLeft):
                currentBigestNumberLeft = int(line[i])
                currentBigestIndex = i+1
            i+=1
        i=currentBigestIndex
        currentBigestBateryPower += str(currentBigestNumberLeft)
        digitsLeft-=1
        
    #print(currentBigestBateryPower)
    total+=int(currentBigestBateryPower)
print(total)