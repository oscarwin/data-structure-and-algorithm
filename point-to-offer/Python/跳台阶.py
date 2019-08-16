# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.mapVal = {}

    def jumpFloor(self, number):
        if number == 0:
            return 1
        
        if number == 1:
            return 1

        if not self.mapVal.get(number):
            self.mapVal[number] = self.jumpFloor(number - 1) + self.jumpFloor(number - 2)

        return self.mapVal[number]

if __name__ == "__main__":
    so = Solution()
    print(so.jumpFloor(0))
    print(so.jumpFloor(1))
    print(so.jumpFloor(2))
    print(so.jumpFloor(10))
    print(so.jumpFloor(20))