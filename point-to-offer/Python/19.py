# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.retList = []

    def recursivePrint(self, matrix, up, down, left, right):
        if up > down or left > right:
            return

        if up == down:
            self.retList.extend(matrix[up][left:(right + 1)])
            return
        if left == right:
            for x in range(up, down + 1):
                self.retList.append(matrix[x][left])
            return

        for x in range(left, right):
            self.retList.append(matrix[up][x])

        for x in range(up, down):
            self.retList.append(matrix[x][right])
        
        for x in range(right, left, -1):
            self.retList.append(matrix[down][x])
        
        for x in range(down, up, -1):
            self.retList.append(matrix[x][left])
        
        self.recursivePrint(matrix, up + 1, down - 1, left + 1, right - 1)

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        self.retList = []
        if not len(matrix):
            return
        
        if type(matrix[0]) is int:
            return matrix

        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        self.recursivePrint(matrix, up, down, left, right)
        return self.retList
    
if __name__ == "__main__":
    s = Solution()
    l = []
    print(s.printMatrix(l))

    l = [1, 2, 3]
    print(s.printMatrix(l))

    l = [[1],[2],[3]]
    print(s.printMatrix(l))

    l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(s.printMatrix(l))
    