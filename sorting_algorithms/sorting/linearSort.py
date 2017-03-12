import math
from sorting.insertionSort import insertion_sort

def countingSort(srcArray, maxValue):
    
    tmpArray = [i * 0 for i in range(0, maxValue + 1)]
    
    for i in range(0, len(srcArray)) :
        tmpArray[srcArray[i]] = tmpArray[srcArray[i]] + 1
        
    for i in range(1, len(tmpArray)) :
        tmpArray[i] = tmpArray[i] + tmpArray[i - 1]
    
    retArray = [i * 0 for i in range(0, len(srcArray))]
    for i in range(len(srcArray)-1, -1, -1) :
        retArray[tmpArray[srcArray[i]]-1] = srcArray[i]
        tmpArray[srcArray[i]] = tmpArray[srcArray[i]] - 1
    
    return retArray

def countingSortForRadix(srcArray, decimal):
    
    tmpArray = [i * 0 for i in range(0, 10)]
    
    for i in range(0, len(srcArray)) :
        tmpIdx = int(srcArray[i] / decimal % 10)
        tmpArray[tmpIdx] = tmpArray[tmpIdx] + 1
        
    for i in range(1, len(tmpArray)) :
        tmpArray[i] = tmpArray[i] + tmpArray[i - 1]
        
    retArray = [i * 0 for i in range(0, len(srcArray))]
    for i in range(len(srcArray) - 1, -1, -1) :
        tmpIdx = int(srcArray[i] / decimal % 10)
        retArray[tmpArray[tmpIdx] - 1] = srcArray[i]
        tmpArray[tmpIdx] = tmpArray[tmpIdx] - 1
        
    return retArray

def radixSort(srcArray, decimal):
    
    retArray = srcArray
    for i in range(0, decimal) :
        d = math.pow(10, i);
        retArray = countingSortForRadix(retArray, d)
        print(retArray)

    return retArray

def bucketSort(srcArray):
    
    srcLen = len(srcArray)
    hashTable = [[] for i in range(0, srcLen)]
    retArray = []
    
    for i in range(0, srcLen) :
        tmpIdx = int(srcLen * srcArray[i])
        hashTable[tmpIdx].append(srcArray[i])
        
    for i in range(0, srcLen) :
        if len(hashTable[i]) == 0 : 
            continue;
        
        insertion_sort(hashTable[i])
        
        for j in range(0, len(hashTable[i])) :
            retArray.append(hashTable[i][j])
            
    return retArray

if __name__ == '__main__':
    
    array = [2, 1, 3, 4, 6, 6, 2, 9, 5, 2, 3, 5, 1]
    
    retArray = countingSort(array, 9)
    print(retArray)
    
    array2 = [123, 321, 235, 253, 577, 576, 234, 546, 753, 853, 913, 324]
    retArray2 = radixSort(array2, 3)
    print(retArray2)
    
    array3 = [0.123, 0.321, 0.234, 0.919, 0.283, 0.181, 0.182, 0.328, 0.248, 0.324]
    retArray3 = bucketSort(array3)
    print(retArray3)