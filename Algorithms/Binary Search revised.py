#DECLARE arrayData: 1D ARRAY
arrayData = [10,5,6,7,1,12,13,15,21,8]

#DECLARE number: INTEGER as input
number = int(input("Number for search: "))

def linearSearch(number):
    for i in range(0, len(arrayData)):
        if  number == arrayData[i]:
            return(print("number found"),True)
    return(print("number not found"), False)



def bubbleSort(arrayData):
    temp = 0
    
    for i in range(len(arrayData)):
        for j in range(len(arrayData)-1):
            if arrayData[j] > arrayData[j+1]:
                temp = arrayData[j]
                arrayData[j] = arrayData[j+1]
                arrayData[j+1] = temp

    print(arrayData)

bubbleSort(arrayData)
                
            
        



    
