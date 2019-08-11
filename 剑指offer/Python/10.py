# -*- coding:utf-8 -*-
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