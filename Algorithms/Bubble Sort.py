arrayData = [10,5,6,7,1,12,13,15,21,8]


def bubbleSort(arrayData):
    temp = 0
    n = len(arrayData) - 1
    noMoreSwaps = False

    while noMoreSwaps == False:
        for x in range(n):
            if arrayData[x] > arrayData[x+1]:
                temp = arrayData[x]
                arrayData[x] = arrayData[x+1]
                arrayData[x+1] = temp
                noMoreSwaps = False
            else:
                noMoreSwaps = True
        n -= 1
        
    
        

            
