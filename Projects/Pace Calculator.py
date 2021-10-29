avgmile = 0
avgpace = 0
mile = 0
km = 0
h = 0
m = 0

km = float(input("How many km did u run u stpid person?: "))
while km < 0:
    km = float(input("please retype your value: "))
    if km >= 0:
        break
h = int(input("How many hours did u run u stpid person?: "))
while h < 0:
    h = float(input("please retype your value: "))
    if h >= 0:
        break
m = int(input("How many minutes did u run u stpid person?: "))
while m < 0:
    m = float(input("please retype your value: "))
    if m >= 0:
        break
mile = km * 0.621
print("You have ran: " ,round(mile, 2),"miles")

avgpace = ((h*60)+m)/mile
print("Your average pace is: " ,round(avgpace, 2),"minutes/mile")

avgmile = mile/(h+(m/60))
print("Your average mile is:" ,round(avgmile, 2),"miles/hours")


