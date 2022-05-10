import copy

from numpy import append
#Method to convert a integer list into one integer. 
def convert(list): 
    # Converting integer list to string list
    s = [str(i) for i in list] 
    # Join list items using join()
    #Cast it to int. 
    res = int("".join(s))
    return res


#For user to call.
#Abstracted away the count. 
def kaprConst(number):
    return kaprConstRun(number,1)


#Main constant calculation method.
def kaprConstRun(number, count):
    newList = [int(x) for x in str(number)]
    idx = len(newList)
    while idx <= 3:
        newList.insert(0, 0)
        idx += 1
    #Make copy of the newList, that is a list of integers.
    highestToLowest = copy.deepcopy(newList)
    lowestToHighest = copy.deepcopy(newList)
    #Sort the lists.
    highestToLowest.sort(reverse = True)
    lowestToHighest.sort(reverse = False)
    #Convert the lists into integers using util method I wrote. 
    highest = convert(highestToLowest)
    lowest = convert(lowestToHighest)

    #Calculation
    nextValue = highest - lowest
    #If count total is 7. Count begins from 1. 
    if count == 7:
        return nextValue

    newCount = count + 1
    #Recursion. 
    return kaprConstRun(nextValue, newCount)

#Driver code
if __name__ == "__main__":

    satisfied = []
    notSatisfied = []
    for x in range(1000, 9999):
        if x in [1111,2222,3333,4444,5555,6666,7777,8888,9999]:
            continue

        if kaprConst(x) == 6174:
            satisfied.append(x)
        else: 
            notSatisfied.append(x)

    print("Satisfied for total of ", len(satisfied))
    print("Not satisifed for total of ", len(notSatisfied))


