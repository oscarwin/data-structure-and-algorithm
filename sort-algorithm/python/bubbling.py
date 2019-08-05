#!/usr/bin/python
#-*- coding:utf-8 -*- 

def bubbling(arr):
    arrlen = len(arr)
    if arrlen <= 1:
        return

    for i in range(arrlen):
        for j in range(arrlen - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    arr = [5, 8, 6, 5, 7, 2, 5, 1, 6, 9, 3, 4, 11, 25, 14]
    print(arr)
    bubbling(arr)
    print(arr)