arrayData = [53,21,60,18,42,19]

def insertionSort(arrayData):
    n = len(arrayData)-1

    for x in range(n):
        itemToBeInserted = arrayData[x]
        currentItem = x - 1
        while (arrayData[currentItem] > itemToBeInserted) and (currentItem = -1):
            arrayData[currentItem + 1] = arrayData[currentItem]
            currentItem -= 1
        arrayData[currentItem + 1] = itemToBeInserted

        
