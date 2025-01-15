unsortList = [4,5,2,6,69,47,8,1,9,2,21,63,63,0]


def myInsertion(lists):
    myList = lists
    for x in range(len(myList)):
        if x > 0:
            for y in range(x):
                if myList[x-y] < myList[x-y-1]:
                    tempNumber = myList[x-y-1]
                    myList[x-y-1] = myList[x-y] 
                    myList[x-y] = tempNumber
    
    return myList
                
print(myInsertion(unsortList))


