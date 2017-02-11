'''
Created on 2017. 2. 05.

@author: hansgg
@summary: 최대 부분 집합 검색 알고리즘 
'''

def findMaxCrossingSubArray (array, lowIdx, midIdx, highIdx):
    leftSum = -9999999
    iSum = 0
    maxLeft = 0
    for i in range(midIdx, lowIdx - 1, -1):
        iSum = iSum + array[i]
        if iSum > leftSum :
            leftSum = iSum
            maxLeft = i
            
    rightSum = -9999999
    iSum = 0
    maxRight = 0
    for j in range(midIdx + 1, highIdx + 1, 1):
        iSum = iSum + array[j]
        if iSum > rightSum :
            rightSum = iSum
            maxRight = j
            
    return maxLeft, maxRight, leftSum + rightSum

def findMaximumSubArray(array, lowIdx, highIdx):
    if highIdx == lowIdx :
        return lowIdx, highIdx, array[lowIdx]
    
    else :
        midIdx = int((lowIdx + highIdx) / 2)
        leftLowIdx, leftHighIdx, leftSum = findMaximumSubArray(array, lowIdx, midIdx)
        rightLowIdx, rightHighIdx, rightSum = findMaximumSubArray(array, midIdx + 1, highIdx)
        crossLowIdx, crossHighIdx, crossSum = findMaxCrossingSubArray(array, lowIdx, midIdx, highIdx)
        
        if leftSum >= rightSum and leftSum >= crossSum :
            return leftLowIdx, leftHighIdx, leftSum
        elif rightSum >=leftSum and rightSum >= crossSum :
            return rightLowIdx, rightHighIdx, rightSum
        else :
            return crossLowIdx, crossHighIdx, crossSum
        
if __name__ == '__main__':
    array = [1, -3, 2, -4, 5, 8, -10, 9,-7, 6]
    maxLowIdx, maxHighIdx, maxSum = findMaximumSubArray(array, 0, len(array) - 1)
    print("maxLowIdx = " + str(maxLowIdx) + ", maxHighIdx = " + str(maxHighIdx) + ", maxSum = " + str(maxSum))
