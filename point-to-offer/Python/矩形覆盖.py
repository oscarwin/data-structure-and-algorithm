# -*- coding:utf-8 -*-

# 题目描述
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

class Solution:
    def __init__(self):
        self.mapVal = {}

    def rectCover(self, number):
        if number == 0:
            return 0
        
        if number == 1:
            return 1
        
        if number == 2:
            return 2
        
        if not self.mapVal.get(number):
            self.mapVal[number] = self.rectCover(number - 1) + self.rectCover(number - 2)
            
        return self.mapVal[number]


if __name__ == "__main__":
    so = Solution()
    print(so.rectCover(1))
    print(so.rectCover(2))
    print(so.rectCover(3))
    print(so.rectCover(4))