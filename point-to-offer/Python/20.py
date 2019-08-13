# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if len(self.minStack) == 0:
            self.minStack.append(node)
        else:
            if self.minStack[-1] > node:
                self.minStack.append(node)
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minStack[-1]

if __name__ == "__main__":
    l = [1, 3, 4, 3, 1, 2]
    s = Solution()
    for x in l:
        s.push(x)
    
    for i in range(len(l)):
        print(s.min())
        s.pop()