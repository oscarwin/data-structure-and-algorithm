# 题目描述
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None and pHead2 is None:
            return

        result = ListNode(0)
        curNode = result

        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                tempNode = pHead1
                pHead1 = pHead1.next
            else:
                tempNode = pHead2
                pHead2 = pHead2.next

            curNode.next = tempNode
            curNode = tempNode
        
        while pHead1:
            curNode.next = pHead1
            pHead1 = pHead1.next
            curNode = curNode.next
        
        while pHead2:
            curNode.next = pHead2
            pHead2 = pHead2.next
            curNode = curNode.next
        
        return result.next