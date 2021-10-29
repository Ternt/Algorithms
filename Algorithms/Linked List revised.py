#DECLARE the node of linkedlist as a class
class Node:
    def __init__(self, data, nextNode = None):
        #DECLARE data and nextNode: INTEGER
        self.data = data
        self.nextNode = nextNode


#DECLARE LinkedList as a 1D array of type Node
LinkedList = [Node(1,1), Node(5,4), Node(6,7), Node(7,-1), Node(2,2), Node(0,6), Node(0,8), Node(56,3), Node(0,9), Node(0,-1)]
startPointer = LinkedList[0]
emptySpace = 5


def outputNodes(LinkedList, startPointer):
    #DECLARE Current as the current address and current pointer
    Current = startPointer
    while Current.nextNode != -1:
        print(Current.data)
        Current = LinkedList[Current.nextNode]
        
    print(Current.data)
        
#outputNodes(LinkedList, startPointer)


def addNode(LinkedList, startPointer,emptySpace):
    #DECLARE nextEmpty, emptySpace: INTEGER
    #DECLARE newData: INTEGER as input data
    newData = int(input("Input data to be added: "))
    Current = startPointer
    if emptySpace == -1:
        return(False)
    else:
        while Current.nextNode != -1:
            Current = LinkedList[Current.nextNode]
        Current.nextNode = emptySpace
        nextEmpty = LinkedList[emptySpace].nextNode
        LinkedList[emptySpace].data = newData
        LinkedList[emptySpace].nextNode = -1
        emptySpace = nextEmpty
        return(True)

outputNodes(LinkedList, startPointer)
if addNode(LinkedList,startPointer, emptySpace) == True:
    print("")
    outputNodes(LinkedList, startPointer)
    print("Node succesfully added!")
else:
    print("Cannot add node. No empty spaces.")
    






    


    
    
        
        
