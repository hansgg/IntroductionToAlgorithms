'''
Created on 2017. 2. 05.

@author: hansgg
@summary: �� ���� �˰��� 
'''
def getLeftChild(idx):
    return int(idx << 1)

def getRightChild(idx):
    return int(idx << 1) + 1

#�ִ��� Ư�� �ο� (�� �θ� Ʈ���� �ڽĺ��� ū���� �̷���� ����Ʈ��)
def maxHeapify(array, arrayLen, idx):
    leftChild = getLeftChild(idx)
    rightChild = getRightChild(idx)
    
    largest = 0
    
    #�θ����� ���� �ڽĳ�� ���� ���� ��
    if(leftChild < arrayLen and array[leftChild] > array[idx]) :
        largest = leftChild
    else :
        largest = idx
    
    #������ ��� �߿� ������ �ڽĳ������ ���� ��
    if rightChild < arrayLen and array[rightChild] > array[largest] :
        largest = rightChild
    
    #���� ����� �θ� �ڸ��� �ű�.
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
    #�ִ� �� Ư���� �̿��Ͽ� ����ū ��Ʈ ������ �迭�� ���� ������ �κ����� �̵��� �ݺ��Ͽ� ����.
    for i in range(arrayLen, 0, -1):
        tmp = array[0]
        array[0] = array[i]
        array[i] = tmp
        maxHeapify(array, i, 0)


array = [1, 0, 3, 6, 2, 5, 7, 10, 32, 23, 42, 53, 65, 12, 18, 9, 22, 4]

heapSort(array)
print(array)        