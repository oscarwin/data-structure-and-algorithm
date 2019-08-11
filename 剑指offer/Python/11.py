# -*- coding:utf-8 -*-
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