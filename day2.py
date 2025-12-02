from math import sqrt
text = open("text.txt", "r+")

text = text.readline()

ranges = text.split(',')
total =0
for range1 in ranges:
    valuesInRange = range1.split('-')
    initial_value = int(valuesInRange[0])
    final_value = int(valuesInRange[1])
    for currentID in range(initial_value, final_value+1):
        stringID = str(currentID)
        sizeCurrentId = len(stringID)
        itsAnId = False
        stepsToCheck = [i for i in range(1, sizeCurrentId//2 + 1) if sizeCurrentId % i == 0]
        #print("-"*10)
        #print(stringID)
        #print(stepsToCheck)
        for step in stepsToCheck:#1188511885 = [1,2,5]
            i=0
            f = step
            currentLooking=stringID[0:step]
            itsAnId = False
            while(i<sizeCurrentId):
                newLooking = stringID[i:f]
                #print(f'{currentLooking} - {newLooking}')
                if(currentLooking!=newLooking):
                    break
                if(f==sizeCurrentId):
                    #print("OLA")
                    itsAnId=True
                    break
                i+=step
                f+=step
            if(itsAnId):
                total+=currentID    
                break
        #print("-"*10)
            
        
print(total)