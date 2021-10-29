#question 2)a)

arrayData = [10,5,6,7,1,12,13,15,21,8]

#question 2)b)

a = int(input("Input parameter: "))

def linearSearch(a):
    for x in range(10):
        x += 1
        if a == arrayData[x]:
            return(print("Number found"))
        else:
            return(print("Number not found"))


linearSearch(a)


            
        
