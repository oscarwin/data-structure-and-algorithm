#!/usr/bin/python
# -*- coding:utf-8 -*-

# 题目描述
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

# -*- coding:utf-8 -*-
class Solution:
    def fun(self, sequence):
        if sequence is None:
            return False
        
        if len(sequence) <= 1:
            return True
        
        # 找到第一个大于最后一个元素的位置
        firstLargePos = 0
        for firstLargePos in range(len(sequence)):
            if sequence[firstLargePos] > sequence[-1]:
                break
        
        # 判断后面所有的元素都大于
        for i in range(firstLargePos, len(sequence) - 1):
            if sequence[i] < sequence[-1]:
                return False
        
        return self.fun(sequence[0:firstLargePos]) and self.fun(sequence[firstLargePos:-1])

    def VerifySquenceOfBST(self, sequence):
        if sequence is None or len(sequence) == 0:
            return False
        
        return self.fun(sequence)

if __name__ == "__main__":
    so = Solution()

    s = [7, 4, 6, 5]
    print(so.VerifySquenceOfBST(s))

    s = [5, 7, 6, 9, 11, 10, 8]
    print(so.VerifySquenceOfBST(s))

    s = [4, 6, 7, 5]
    print(so.VerifySquenceOfBST(s))