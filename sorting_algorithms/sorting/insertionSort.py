def insertion_sort(array):
    key = -1
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i > -1 and array[i] > key:
            array[i  + 1] = array[i]
            i = i - 1
        array[i + 1] = key
        
if __name__ == '__main__':
    a = [10, 3, 15, 8, 28, 13]
    insertion_sort(a)
    print(a)