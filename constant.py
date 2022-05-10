import copy

def convert(list): 
    # Converting integer list to string list
    s = [str(i) for i in list] 
    # Join list items using join()
    res = int("".join(s))
    return(res)

def kaprConst(number):
    return kaprConstRun(number,0)



def kaprConstRun(number, count):
    newList = [int(x) for x in str(number)]
    idx = len(newList)
    while idx <= 3:
        newList.insert(0, 0)
        idx += 1
    
    highestToLowest = copy.deepcopy(newList)
    lowestToHighest = copy.deepcopy(newList)
    
    #print("The number is", number)
    #We know it is 4 digit number. 
    #Greatest to lowest
    highestToLowest.sort(reverse = True)
    #lowest to greatest.
    lowestToHighest.sort(reverse = False)
    highest = convert(highestToLowest)
    lowest = convert(lowestToHighest)


    #Todo, just highest from lowers
    #nextValue = abs(num - highest - lowest)
    #TODO maybe no abs value is needed.
    #TODO this what I did is a nice idea to go see another pattern. 
    
    nextValue = highest - lowest
    

    #print("THis is the next value being sent", nextValue)
    # using list comprehension
    # to convert number to list of integers
    # res = [int(x) for x in str(nextValue)]
    #print("Count is, " , count)
    if count == 6:
        return nextValue

    newCount = count + 1
    return kaprConstRun(nextValue, newCount)
    
    
    
    
    
    # print("arrays after.", highestToLowest, lowestToHighest)



for x in range(1000, 9999):
    if x in [1111,2222,3333,4444,5555,6666,7777,8888,9999]:
        continue
    print(f"THe constant after 7 tries is {kaprConst(x)} for a number {x}" )
    

print("When i Do it on 6174:", kaprConst(6174))

    

