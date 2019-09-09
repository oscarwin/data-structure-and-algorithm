#!/usr/bin/python
# -*- coding:utf-8 -*-

# 题目描述
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        
        num = 0
        count = 0
        for i in range(len(numbers)):
            if count == 0:
                num = numbers[i]
                count = 1
            else:
                if num == numbers[i]:
                    count += 1
                else:
                    count -= 1
        
        count = 0
        for i in range(len(numbers)):
            if num == numbers[i]:
                count += 1
        
        return num if count > len(numbers) / 2 else 0

if __name__ == "__main__":
    so = Solution()

    numbers = []
    print(so.MoreThanHalfNum_Solution(numbers))

    numbers = [1,2,3,2,2,2,5,4,2]
    print(so.MoreThanHalfNum_Solution(numbers))

    numbers = [1,2,3,2,5,4,5]
    print(so.MoreThanHalfNum_Solution(numbers))

    numbers = [2,2,2,2,2,1,3,4,5]
    print(so.MoreThanHalfNum_Solution(numbers))