# -*- coding:utf-8 -*-

# 题目描述
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

class Solution:
    def __init__(self):
        self.mapValue = {}
    
    def Cal(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        if self.mapValue.get(exponent):
            return self.mapValue.get(exponent)
            
        if exponent % 2:
            result = self.Cal(base, exponent - 1) * base
        else:
            temp = self.Cal(base, int(exponent / 2))
            result = temp * temp
        
        self.mapValue[exponent] = result
        return result
    
    def Power(self, base, exponent):
        if exponent < 0:
            return 1 / self.Cal(base, exponent * -1)
        else:
            return self.Cal(base, exponent)

if __name__ == "__main__":
    so = Solution()
    print(so.Power(1.2, 0))
    print(so.Power(1.2, -1))
    print(so.Power(1.2, 2))
    print(so.Power(1.2, 3))

