'''
Created on 2017. 2. 05.

@author: hansgg
@summary: 힙 정렬 알고리즘 
'''
def getLeftChild(idx):
    return int(idx << 1)

def getRightChild(idx):
    return int(idx << 1) + 1

#최대힙 특성 부여 (각 부모 트리가 자식보다 큰수로 이루어진 이진트리)
def maxHeapify(array, arrayLen, idx):
    leftChild = getLeftChild(idx)
    rightChild = getRightChild(idx)
    
    largest = 0
    
    #부모리프와 왼쪽 자식놈과 누가 쎈지 비교
    if(leftChild < arrayLen and array[leftChild] > array[idx]) :
        largest = leftChild
    else :
        largest = idx
    
    #위에서 쎈놈 중에 오른쪽 자식놈과누가 쎈지 비교
    if rightChild < arrayLen and array[rightChild] > array[largest] :
        largest = rightChild
    
    #가장 쎈놈을 부모 자리로 옮김.
    if largest != idx:
        tmp = array[idx]
        array[idx] = array[largest]
        array[largest] = tmp 
        maxHeapify(array, arrayLen, largest)

def buildMaxHeap(array):
    for i in range(int(len(array) / 2), -1, -1):
        maxHeapify(array, len(array), i)
        
def heapSort(array):
    buildMaxHeap(array)
    
    arrayLen = len(array)-1
    #최대 힙 특성을 이용하여 가장큰 루트 리프를 배열의 제일 마지막 부분으로 이동을 반복하여 정렬.
    for i in range(arrayLen, 0, -1):
        tmp = array[0]
        array[0] = array[i]
        array[i] = tmp
        maxHeapify(array, i, 0)


array = [1, 0, 3, 6, 2, 5, 7, 10, 32, 23, 42, 53, 65, 12, 18, 9, 22, 4]

heapSort(array)
print(array)        