# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.list1 = []
        self.list2 = []

    def push(self, node):
        self.list1.append(node)

    def pop(self):
        if len(self.list2) == 0:
            while self.list1:
                self.list2.append(self.list1.pop())

        return self.list2.pop()