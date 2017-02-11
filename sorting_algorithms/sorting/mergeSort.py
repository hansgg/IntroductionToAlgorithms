'''
Created on 2017. 1. 29.

@author: hansgg
@summary: 병합 정렬 알고리즘 
'''

def merge(array, leftidx, halfidx, rightidx):
    leftlen = halfidx - leftidx + 1
    rightlen = rightidx - halfidx
    left_array = []
    right_array = []
    
    for i in range(0, leftlen-1):
        left_array.append(array[leftidx + i])
    for j in range(rightlen):
        right_array.append(array[halfidx + j])
    left_array.append(99999)
    right_array.append(99999)
    
    i = 0
    j = 0
        
    for k in range(leftidx, rightidx):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i = i + 1
        else:
            array[k] = right_array[j]
            j = j + 1
        
    
def merge_sort(array, leftidx, rightidx):
    if leftidx < rightidx :
        halfidx = int((leftidx + rightidx) / 2)
        merge_sort(array, leftidx, halfidx)
        merge_sort(array, halfidx + 1, rightidx)
        merge(array, leftidx, halfidx, rightidx)
        
if __name__ == '__main__':
    array = [8, 3, 14, 10, 28, 15]
    merge_sort(array, 0, len(array))
    print(array)
