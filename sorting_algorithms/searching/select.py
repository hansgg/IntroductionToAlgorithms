from sorting.quickSort import randomized_partition

def getMin(array):
    
    minValue = array[0]
    for i in range(1, len(array)) :
        if minValue > array[i] :
            minValue = array[i]
    
    return minValue

def getMinAndMax(array):
    
    minValue = array[0]
    maxValue = array[0]
    for i in range(1, len(array)) :
        if minValue > array[i] :
            minValue = array[i]
        
        if maxValue < array[i] :
            maxValue = array[i]
    
    return minValue, maxValue

def randomized_select(array, startIdx, length, target):
    
    if startIdx >= length - 1 :
        return array[startIdx]
    
    centerIdx = randomized_partition(array, startIdx, length)
    k = centerIdx - startIdx + 1
    
    if target == k :
        return array[centerIdx]
    elif target < k :
        return randomized_select(array, startIdx, centerIdx, target)
    else :
        return randomized_select(array, centerIdx + 1, length, target - k)
    

if __name__ == '__main__' :
    retArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    print("----------getMin--------------")
    ret = getMin(retArray)
    print("min : " + str(ret))
    
    print("\n-------getMinAndMax-------")
    retMin, retMax = getMinAndMax(retArray)
    print("min : " + str(retMin))
    print("max : " + str(retMax))

    print("\n--------randomized_select---------")
    retVal = randomized_select(retArray, 0, len(retArray), 3)
    print("targetIdx : " + str(retVal))