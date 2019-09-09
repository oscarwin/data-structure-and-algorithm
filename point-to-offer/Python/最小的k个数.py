#!/usr/bin/python
# -*- coding:utf-8 -*-

# 题目描述
# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

import heapq

class BtmkHeap:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def Push(self, item):
        item = -item
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, item)
        else:
            if item > self.heap[0]:
                heapq.heapreplace(self.heap, item)
    
    def Btmk(self):
        return sorted([-x for x in self.heap])

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k == 0 or len(tinput) < k:
            return []
        
        if len(tinput) == k:
            return sorted(tinput)
        
        heap = BtmkHeap(k)
        for x in tinput:
            heap.Push(x)
        
        return heap.Btmk()

if __name__ == "__main__":
    input_list = [4,5,1,6,2,7,3,8]
    so = Solution()
    print(so.GetLeastNumbers_Solution(input_list, 0))