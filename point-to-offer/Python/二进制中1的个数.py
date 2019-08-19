# -*- coding:utf-8 -*-

# 题目描述
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

class Solution:
    def NumberOf1(self, n):
        count = 0
        flag = 1
        for x in range(32):
            if n & flag:
                count += 1
            flag = flag << 1
        
        return count

if __name__ == "__main__":
    so = Solution()
    print(so.NumberOf1(1))
    print(so.NumberOf1(3))