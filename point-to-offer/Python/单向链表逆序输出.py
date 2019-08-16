# -*- coding:utf-8 -*-

# 题目描述：
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        listRet = []
        if listNode.next:
            listRet = self.printListFromTailToHead(listNode.next)
            listRet.append(listNode.val)
        else:
            listRet.append(listNode.val)
        
        return listRet

if __name__ == "__main__":
    s1 = ListNode(1)
    s2 = ListNode(2)
    s3 = ListNode(3)
    s1.next = s2
    s2.next = s3

    so = Solution()
    ret = so.printListFromTailToHead(s1)
    print(ret)
