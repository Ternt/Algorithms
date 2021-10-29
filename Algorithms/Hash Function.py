arrayData = [""]*100

item = input("Item: ")

def insertItem(item):
    if item == int:
        index = hash(item)%10
        arrayData[index] = item
        print(arrayData)
    else:
        index = hash(item)%10
        arrayData[index] = item
        print(arrayData)

insertItem(item)
        
        
    
