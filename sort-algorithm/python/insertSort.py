#/usr/bin/python
#-*- coding:utf-8 -*-

def insertSort(arr):
    lenth = len(arr)
    for i in range(1, lenth):
        val = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > val:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                arr[j] = val; 
                break;

if __name__ == "__main__":
    arr = [5, 8, 6, 5, 7, 2, 5, 1, 6, 9, 3, 4, 11, 25, 14]
    print(arr)
    insertSort(arr)
    print(arr, "\n")

    arr = [5, 5, 5, 5, 5]
    print(arr)
    insertSort(arr)
    print(arr, "\n")

    arr = [1, 2, 3, 4, 5, 6]
    print(arr)
    insertSort(arr)
    print(arr, "\n")

    arr = [6, 5, 4, 3, 2, 1]
    print(arr)
    insertSort(arr)
    print(arr, "\n")
    
    arr = [-6, -5, -4, -3, -2, -1]
    print(arr)
    insertSort(arr)
    print(arr, "\n")