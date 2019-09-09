#!/usr/bin/python
# -*- coding:utf-8 -*-

# 题目描述
# HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
# 今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
# 但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
# 例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
# 给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return 0

        maxValue = array[0]
        curValue = array[0]
        for i in range(1, len(array)):
            if curValue > 0 and curValue + array[i] > 0:
                curValue += array[i]
            else:
                curValue = array[i]
            
            if curValue > maxValue:
                maxValue = curValue
        
        return maxValue

if __name__ == "__main__":
    so = Solution()
    array = [6,-3,-2,7,-15,1,2,2]
    print(so.FindGreatestSumOfSubArray(array))

    array = []
    print(so.FindGreatestSumOfSubArray(array))

    array = [-1,-3,-5,-8]
    print(so.FindGreatestSumOfSubArray(array))

    array = [1,-2,3,10,-4,7,2,-5]
    print(so.FindGreatestSumOfSubArray(array))