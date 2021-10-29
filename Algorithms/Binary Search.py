arrayData = [1,10,21,35,36,50,69,70,74,98]

searchItem = int(input("Input search item: "))
                 
def binarySearch(searchItem):
    Found = False
    searchFailed = False
    First = 0
    Last = len(arrayData) - 1

    while Found == False and searchFailed == False:
        middle = (First + Last) // 2
        if arrayData[middle] == searchItem:
            Found = True

        else:
            if First >= Last:
                searchFailed = True

            else:
                if arrayData[middle] > searchItem:
                    Last = middle - 1
                    First = middle + 1


    if Found == True:
        print(middle)
    else:
        print("Item is not in array")


binarySearch(searchItem)
