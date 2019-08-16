# -*- coding:utf-8 -*-

# 题目描述：
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

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