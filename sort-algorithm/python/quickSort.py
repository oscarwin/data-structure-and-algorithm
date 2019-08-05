#!/usr/bin/python
#-*- coding:utf-8 -*-

def RecursiveSort(arr, start, end):
    if start == end:
        return
    # 取三个元素的中间元素作为枢纽元
    mid = int((start + end) / 2)
    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[start], arr[end]
    if arr[end] > arr[mid]:
        arr[end], arr[mid] = arr[mid], arr[end]

    i = start
    j = end - 1;
    while i < j:
        while arr[i] < arr[end]:
            i += 1
        while arr[j] >= arr[end] and j:
            j -= 1

        if i < j and arr[i] > arr[j]:
            arr[i], arr[j] == arr[j], arr[i]
    
    # 把最后的那个元素换过来
    arr[i], arr[end] = arr[end], arr[i]

    # 递归调用
    RecursiveSort(arr, start, i - 1)
    RecursiveSort(arr, i + 1, end)

def quickSort(arr):
    # 取第一个元素作为中间元素
    start = 0
    end = len(arr) - 1
    RecursiveSort(arr, start, end)

if __name__ == "__main__":
    arr = [5, 8, 6, 5, 7, 2, 5, 1, 6, 9, 3, 4, 11, 25, 14]
    print(arr)
    quickSort(arr)
    print(arr)