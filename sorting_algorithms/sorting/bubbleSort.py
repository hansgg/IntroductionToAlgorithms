'''
Created on 2017. 1. 29.

@author: hansgg
@summary: 버블 정렬 알고리즘 
'''

def bubble_sort(array):
    for i in range(0, len(array) - 1):
        j = len(array) - 1
        while(j > i):
            if array[j] < array[j - 1]:
                tmp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tmp
            
            j = j - 1

if __name__ == '__main__':
    array = [3, 2, 8, 5, 10, 1]
    bubble_sort(array)
    print(array)
