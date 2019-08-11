# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.mapVal = {}

    def Fibonacci(self, n):
        if n == 0:
            return 0

        if n == 1:
            return 1
        
        if not self.mapVal.get(n):
            self.mapVal[n] = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

        return self.mapVal[n]

    def Fibonacci2(self, n):
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        first = 0
        second = 1
        for x in range(2, n, 1):
            temp = first + second
            first, second = second, temp
        
        return first + second

if __name__ == "__main__":
    so = Solution()
    print(so.Fibonacci(0))
    print(so.Fibonacci(1))
    print(so.Fibonacci(2))
    print(so.Fibonacci(10))
    print(so.Fibonacci(20))