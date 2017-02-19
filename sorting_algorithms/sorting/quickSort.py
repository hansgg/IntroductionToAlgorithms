'''
Created on 2017. 2. 19.

@author: Administrator
'''
import random

def quickSort(array, startIdx, length):
    
    if startIdx < length-1:
        centerIdx = partition(array, startIdx, length)
        quickSort(array, startIdx, centerIdx)
        quickSort(array, centerIdx + 1, length)

def partition(array, startIdx, length):
    x = array[length - 1]
    i = startIdx - 1
    for j in range(startIdx, length-1):
        if array[j] <= x:
            i = i + 1
            tmp = array[j]
            array[j] = array[i]
            array[i] = tmp
    
    tmp = array[i + 1]
    array[i + 1] = array[length - 1]
    array[length - 1] = tmp
    
    return i + 1

def randomized_partition(array, startIdx, length):
    i = random.randrange(startIdx, length)
    tmp = array[length - 1]
    array[length - 1] = array[i]
    array[i] = tmp
    
    return partition(array, startIdx, length)
    
def randomized_quickSort(array, startIdx, length):
    
    if startIdx < length - 1:
        centerIdx = randomized_partition(array, startIdx, length)
        randomized_quickSort(array, startIdx, centerIdx)
        randomized_quickSort(array, centerIdx + 1, length)

def three_pick_partition(array, startIdx, length):
    
    first = random.randrange(startIdx, length)
    second = random.randrange(startIdx, length)
    third = random.randrange(startIdx, length)
    while second == first :
        second = random.randrange(startIdx, length)
    
    while third == second and third == first :
        third = random.randrange(startIdx, length)
    
    i = first
    if array[third] > array[first]:
        i = third
    
    if array[second] > array[first]:
        if array[second] <= array[third]:
            i = second
    
    tmp = array[length - 1]
    array[length - 1] = array[i]
    array[i] = tmp
            
    return partition(array, startIdx, length)
        

def three_pick_quickSort(array, startIdx, length):
    
    if startIdx < length - 1:
        centerIdx = 0
        if length - startIdx > 3 :
            centerIdx = three_pick_partition(array, startIdx, length)
        else :
            centerIdx = randomized_partition(array, startIdx, length)
        three_pick_quickSort(array, startIdx, centerIdx)
        three_pick_quickSort(array, centerIdx + 1, length)

if __name__ == '__main__':
    
    array = [1, 4, 3, 6, 2, 3, 5, 7, 19]
    quickSort(array, 0, len(array))
    print(array)
    
    array2 = [1, 4, 2, 5, 7, 5, 3, 10, 1, 23, 53, 42]
    randomized_quickSort(array2, 0, len(array2))
    print(array2)
    
    array3 = [1, 2, 3, 5, 2, 3, 7, 9, 10, 32, 12]
    three_pick_quickSort(array3, 0, len(array3))
    print(array3)