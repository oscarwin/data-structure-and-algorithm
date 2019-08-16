# -*- coding:utf-8 -*-

# 题目描述：
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n <= 39

# 斐波那契数列的递归写法很简洁，但是递归写法中会有很多重复计算导致耗时较长。
# 有两种方法来解决这个问题：
# 1是空间换时间，用一个 map 存储已经计算过的结果，这样避免重复计算
# 2是使用非递归的方法来计算

class Solution:
    def __init__(self):
        self.mapVal = {}

    # 方法1
    def Fibonacci(self, n):
        if n == 0:
            return 0

        if n == 1:
            return 1
        
        if not self.mapVal.get(n):
            self.mapVal[n] = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

        return self.mapVal[n]

    # 方法2
    def Fibonacci2(self, n):
        if n == 0:
            return 0

        i, a, b = 1, 0, 1
        while i < n:
            a, b = b, a + b
            i += 1
        return b

if __name__ == "__main__":
    so = Solution()
    print(so.Fibonacci2(0))
    print(so.Fibonacci2(1))
    print(so.Fibonacci2(2))
    print(so.Fibonacci2(10))
    print(so.Fibonacci2(20))